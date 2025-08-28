<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">

</head>
<body>

<h1>Trip Planner AI & Weather Report</h1>

<h2>Trip Planner AI Setup</h2>
<ol>
  <li>Clone the repository:
    <pre>git clone https://github.com/piyushghughu-superteams-dotcom/trip_planner_weather_report_ai_agent.git
cd trip_planner_weather_report_ai_agent</pre>
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
  <li>Get your Weather API key:
    <p>Sign up and get an API key from <a href="https://www.weatherapi.com/" target="_blank">https://www.weatherapi.com/</a></p>
  </li>
  <li>Make sure your <code>.env</code> file contains <code>OPENAI_API_KEY</code> and <code>WEATHER_API_KEY</code>.</li>
  <li>Run the weather report script:
    <pre>python backend/weather_report.py</pre>
  </li>
</ol>

<h2>Notes</h2>
<ul>
  <li>Trip planner stores data in Qdrant and prints a human-readable trip summary.</li>
  <li>Weather report prints forecasts or historical data in a human-readable format.</li>
  <li>Ensure all required API keys are in <code>.env</code> before running the scripts.</li>
</ul>

</body>
</html>
