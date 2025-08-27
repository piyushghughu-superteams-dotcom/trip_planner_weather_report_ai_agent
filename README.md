<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Trip Planner AI & Weather Report</title>
</head>
<body>

<h1>Trip Planner AI & Weather Report</h1>

<h2>Trip Planner AI Setup</h2>
<ol>
  <li>Clone the repository:
    <pre>git clone https://github.com/&lt;your-username&gt;/trip_planner_weather_report_ai_agent.git
cd trip_planner_project</pre>
  </li>
  <li>Run Qdrant using Docker:
    <pre>docker run -p 6333:6333 qdrant/qdrant</pre>
  </li>
  <li>Create and activate a virtual environment:
    <pre>python -m venv venv
source venv/bin/activate</pre>
  </li>
  <li>Install dependencies:
    <pre>pip install -r requirements.txt</pre>
  </li>
  <li>Run the trip planner:
    <pre>python backend/data_loading.py</pre>
  </li>
</ol>

<h2>Weather Report Setup</h2>
<ol>
  <li>Activate the same virtual environment (if not already active):
    <pre>source venv/bin/activate</pre>
  </li>
  <li>Run the weather report script:
    <pre>python backend/weather_report.py</pre>
  </li>
</ol>

<h2>Notes</h2>
<ul>
  <li>Make sure <code>.env</code> contains your <code>OPENAI_API_KEY</code> and <code>WEATHER_API_KEY</code>.</li>
  <li>Trip planner stores data in Qdrant and prints a human-readable trip summary.</li>
  <li>Weather report prints forecasts or historical data in human-readable format.</li>
</ul>

</body>
</html>
