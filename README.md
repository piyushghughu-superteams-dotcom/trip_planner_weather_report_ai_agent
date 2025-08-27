<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">

</head>
<body>

<h1>Trip Planner AI Agent with Weather Integration</h1>

<p>This project allows users to input natural language trip requests and generates structured trip plans, including itinerary, budget breakdown, and tips. It also integrates weather data for requested locations and dates. All trip and weather data are stored in <strong>Qdrant vector database</strong> for retrieval and analysis.</p>

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
  <li>Fetch weather data (forecast & history) using <code>WeatherAPI</code>.</li>
  <li>Store trip data and embeddings in Qdrant.</li>
  <li>Convert structured trip plans and weather reports to human-readable summaries.</li>
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
  <li>Run the main trip planner script:
    <pre>python backend/data_loading.py</pre>
  </li>
  <li>Enter a natural language trip request, e.g.:
    <pre>Give me a total trip plan of Goa for 5 days from 5th Sep to 10th Sep.</pre>
  </li>
  <li>Run the weather report script:
    <pre>python backend/weather_report.py</pre>
  </li>
  <li>Enter a weather query, e.g.:
    <pre>Give me the weather report of today, yesterday, tomorrow, and 2nd September in Kolkata.</pre>
  </li>
  <li>Output examples:
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

Weather report for Kolkata:
Date: 2023-09-04
Temperature: 32°C
Condition: Partly cloudy
Humidity: 70%
Wind: 15 kph
...
    </pre>
  </li>
</ol>

<h2>File Structure</h2>
<ul>
  <li><code>backend/data_loading.py</code> – Main trip planner script.</li>
  <li><code>backend/weather_report.py</code> – Weather API integration script.</li>
  <li><code>.env</code> – Environment variables (API keys).</li>
  <li><code>requirements.txt</code> – Python dependencies.</li>
</ul>

<h2>Notes</h2>
<ul>
  <li>Budget fields may be <code>null</code> if not provided in the request.</li>
  <li>The AI agent uses <code>pydantic-ai</code> with GPT-4o-mini for structured trip plan generation.</li>
  <li>Weather data is fetched for requested dates; "today", "tomorrow", and "yesterday" are converted to actual dates.</li>
  <li>Human-readable summaries are generated via <code>trip_plan_to_text</code> and <code>json_report_to_nlq</code> functions.</li>
</ul>

<h2>Docker Command for Qdrant</h2>
<pre>docker run -p 6333:6333 qdrant/qdrant</pre>

<h2>License</h2>
<p>MIT License</p>

</body>
</html>
