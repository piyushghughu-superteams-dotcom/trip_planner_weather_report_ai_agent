import os
import asyncio
import uuid
from qdrant_client.http import models
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_ai import Agent
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from sentence_transformers import SentenceTransformer
import json

load_dotenv()

user_input_example = input("Enter your trip request: ")
client = QdrantClient(host="localhost", port=6333)
model = SentenceTransformer("all-MiniLM-L6-v2")

if not client.collection_exists("trips"):
    client.create_collection(
        collection_name="trips",
        vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
    )

def get_embedding(text: str):
    return model.encode(text).tolist()


class TripBooking(BaseModel):
    destination: str
    date: str
    travelers: int
    budget: str | None = None
    notes: str | None = None
    duration_days: int | None = None


class ItineraryDay(BaseModel):
    day: int
    title: str
    activities: list[str]


class TripPlan(BaseModel):
    destination: str
    date: dict  # {"start": str, "end": str}
    travelers: int
    budget: int |   None
    duration_days: int
    overview: str
    itinerary: list[ItineraryDay]
    budget_breakdown: dict  # {"flights": int, "accommodation": int, "attractions": int, "dining": int, "total": int}
    tips: list[str]


def save_trip(trip: TripBooking, plan: TripPlan):
    client.upsert(
        collection_name="trips",
        points=[
            models.PointStruct(
                id=str(uuid.uuid4()),
                vector=get_embedding(trip.destination),
                payload={
                    "destination": trip.destination,
                    "date": trip.date,
                    "travelers": trip.travelers,
                    "budget": trip.budget,
                    "notes": trip.notes,
                    "duration_days": trip.duration_days,
                    "plan": plan.model_dump()  # ✅ Save clean structured plan
                }
            )
        ]
    )
    print(f"Trip for {trip.destination} saved in Qdrant")

booking_agent = Agent("openai:gpt-4o-mini")

user_input = user_input_example

async def main():
    # Step 1: Extract trip details
    structured_prompt = f"""
    Extract trip details from the following request and return **only valid JSON** 
    matching this schema:
    {{
      "destination": str,
      "date": str,
      "travelers": int,
      "budget": str,
      "notes": str,
      "duration_days": int
    }}

    Request: "{user_input}"
    """

    result = await booking_agent.run(structured_prompt)
    raw_text = result.output.strip()

    try:
        trip = TripBooking.model_validate_json(raw_text)
    except Exception:
        json_str = raw_text[raw_text.find("{"): raw_text.rfind("}")+1]
        trip = TripBooking.model_validate_json(json_str)

    # Step 2: Generate structured plan
    itinerary_prompt = f"""
    Create a structured JSON itinerary with this schema:
    {{
      "destination": str,
      "date": {{"start": str, "end": str}},
      "travelers": int,
      "budget": int,
      "duration_days": int,
      "overview": str,
      "itinerary": [{{"day": int, "title": str, "activities": [str]}}],
      "budget_breakdown": {{"flights": int, "accommodation": int, "attractions": int, "dining": int, "total": int}},
      "tips": [str]
    }}

    Details:
    Destination: {trip.destination}
    Date: {trip.date}
    Travelers: {trip.travelers}
    Budget: {trip.budget}
    Duration: {trip.duration_days or "N/A"} days
    Notes: {trip.notes or "N/A"}
    """

    response = await booking_agent.run(itinerary_prompt)
    raw_plan = response.output.strip()

    try:
        plan = TripPlan.model_validate_json(raw_plan)
    except Exception:
        json_str = raw_plan[raw_plan.find("{"): raw_plan.rfind("}")+1]
        plan = TripPlan.model_validate_json(json_str)
        
    save_trip(trip, plan)

    # print("\n Trip saved in Qdrant!")
    # print(json.dumps(plan.model_dump(), indent=2))

    def trip_plan_to_text(plan: TripPlan) -> str:
        summary = f"Trip to {plan.destination}\n"
        summary += f"Dates: {plan.date['start']} to {plan.date['end']}\n"
        summary += f"Travelers: {plan.travelers}\n"
        summary += f"Duration: {plan.duration_days} days\n"
        summary += f"Budget: {plan.budget or 'Not provided'}\n\n"
        summary += "Overview:\n"
        summary += f"{plan.overview}\n\n"

        summary += "Itinerary:\n"
        for day in plan.itinerary:
            summary += f"Day {day.day}: {day.title}\n"
            for act in day.activities:
                summary += f"  - {act}\n"
            summary += "\n"

        summary += "Budget Breakdown:\n"
        for key, value in plan.budget_breakdown.items():
            summary += f"  {key.capitalize()}: {value if value is not None else 'N/A'}\n"
        summary += "\n"

        summary += "Tips:\n"
        for tip in plan.tips:
            summary += f"  - {tip}\n"

        return summary

    text_summary = trip_plan_to_text(plan)
    print(text_summary)

if __name__ == "__main__":
    asyncio.run(main())
