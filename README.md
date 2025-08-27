<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Trip Planner AI Agent</title>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; background-color: #f9f9f9; }
    h1, h2, h3 { color: #2c3e50; }
    pre { background-color: #ecf0f1; padding: 10px; border-radius: 5px; overflow-x: auto; }
    code { background-color: #ecf0f1; padding: 2px 5px; border-radius: 3px; }
    ul { margin: 0 0 10px 20px; }
    .note { color: #c0392b; font-weight: bold; }
  </style>
</head>
<body>

<h1>Trip Planner AI Agent</h1>

<p>This project allows users to input natural language trip requests and generates a structured trip plan, including itinerary, budget breakdown, and tips. The plan is stored in a <strong>Qdrant vector database</strong> for retrieval and analysis. It also supports weather integration if needed.</p>

<h2>Features</h2>
<ul>
  <li>Extract trip details from user input using <code>pydantic-ai</code>.</li>
  <li>Generate structured trip plans with:
    <ul>
      <li>Daily itinerary</li>
      <li>Budget breakdown</li>
      <li>Travel tips</li>
    </ul>
  </li>
  <li>Store trip data in Qdrant with vector embeddings.</li>
  <li>Convert structured trip plan to human-readable summary.</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python 3.12+</li>
  <li>Docker</li>
  <li>Python libraries:
    <pre>pip install pydantic pydantic-ai qdrant-client sentence-transformers python-dotenv requests</pre>
  </li>
</ul>

<h2>Setup Instructions</h2>
<ol>
  <li>Clone the repository:
    <pre>git clone https://github.com/&lt;your-username&gt;/trip_planner_weather_report_ai_agent.git
cd trip_planner_project</pre>
  </li>
  <li>Create <code>.env</code> file with your API keys:
    <pre>
OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_weatherapi_key
    </pre>
  </li>
  <li>Run Qdrant using Docker:
    <pre>docker run -p 6333:6333 qdrant/qdrant</pre>
  </li>
  <li>Install Python dependencies:
    <pre>pip install -r requirements.txt</pre>
  </li>
</ol>

<h2>Usage</h2>
<ol>
  <li>Run the main Python script:
    <pre>python backend/data_loading.py</pre>
  </li>
  <li>Enter your trip request in natural language, e.g.:
    <pre>Give me a total trip plan of Goa for 5 days from 5th Sep to 10th Sep.</pre>
  </li>
  <li>Output:
    <ul>
      <li>Trip plan stored in Qdrant</li>
      <li>Human-readable summary printed to console:</li>
    </ul>
    <pre>
Trip to Goa
Dates: 2023-09-05 to 2023-09-10
Travelers: 1
Duration: 5 days
Budget: Not provided

Overview:
A relaxing 5-day trip to Goa, exploring beautiful beaches, local culture, and vibrant nightlife.

Itinerary:
Day 1: Arrival in Goa
  - Check into the hotel
  - Visit Calangute Beach
  - Enjoy a beachside dinner at a local restaurant
...

Budget Breakdown:
  Flights: N/A
  Accommodation: N/A
  Attractions: N/A
  Dining: N/A
  Total: N/A

Tips:
  - Stay hydrated and apply sunscreen during beach activities.
  - Explore local cuisine; try Xacuti and Vindaloo.
  - Negotiate prices at flea markets.
  - Use local transport or rent a scooter for easy commuting.
    </pre>
  </li>
</ol>

<h2>File Structure</h2>
<ul>
  <li><code>backend/data_loading.py</code> – Main script to process trip requests and store plans.</li>
  <li><code>backend/weather_report.py</code> – Weather API integration.</li>
  <li><code>.env</code> – Environment variables (API keys).</li>
  <li><code>requirements.txt</code> – Python dependencies.</li>
</ul>

<h2>Docker Command for Qdrant</h2>
<pre>docker run -p 6333:6333 qdrant/qdrant</pre>

<h2>Notes</h2>
<ul>
  <li>Budget fields may be <code>null</code> if not provided in the request.</li>
  <li>The AI agent uses <code>pydantic-ai</code> with GPT-4o-mini for structured trip plan generation.</li>
  <li>Human-readable summaries are generated via <code>trip_plan_to_text</code> function.</li>
</ul>

<h2>License</h2>
<p>MIT License</p>

</body>
</html>
