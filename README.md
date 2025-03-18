# api-integration-and-data-visualization
COMPANY:CODTECH IT SOLUTIONS

NAME:FOUZIYA MUSKAAN

INTERN ID:CT04WK175

DOMAIN:PYTHON PROGRAMMING

DURATION:4 WEEKS

MENTOR:NEELA SANTOSH

Tools and Technologies Used

1. Python  
   - Python is the programming language used for this task due to its simplicity and powerful ecosystem of libraries. Python makes it easy to work with APIs, process data, and create visualizations.

2. Public APIs 
   - *API (Application Programming Interface):* APIs are used to fetch data from external sources. For this task, a public API like OpenWeatherMap is utilized to retrieve weather-related data (e.g., temperature, humidity, and forecast details). These APIs often provide data in a structured format like JSON, which can be easily parsed and processed in Python.

3. Requests Library  
   - The requests library in Python is a simple and effective tool for sending HTTP requests. It is used to interact with the API by sending requests and receiving data. For example, we use requests.get() to fetch weather data from OpenWeatherMap.

4. JSON (JavaScript Object Notation) 
   - APIs often return data in JSON format. JSON is a lightweight data-interchange format that is easy to read and write. Python provides built-in support for parsing and handling JSON data, making it straightforward to extract relevant information like temperatures, dates, or weather descriptions.

5. Matplotlib
   - *Matplotlib* is a popular Python library for creating static, interactive, and animated visualizations. It is used to design graphs and charts. In this task, Matplotlib helps in plotting the temperature trends over time.

6. Seaborn  
   - *Seaborn* is a Python library built on top of Matplotlib. It simplifies the process of creating aesthetically pleasing and informative visualizations. For this task, Seaborn is used to create a clean and professional-looking line chart that represents the temperature changes over a specified period.

7. Datetime Module  
   - The datetime module is used to handle date and time data. This is essential when working with time-series data, such as weather forecasts, where each data point is associated with a specific timestamp.

---

How the Task is Accomplished

1. Fetch Data from the API 
   - The Python script starts by connecting to a public API (e.g., OpenWeatherMap) using the requests library. A unique API key is required to authenticate the request. The API returns data in JSON format, containing weather details such as temperature, humidity, and time of forecast.

2. Extract and Process Data  
   - The JSON data is parsed using Python’s built-in tools. Relevant fields (e.g., temp, dt_txt) are extracted and stored in lists for easy manipulation. This ensures that only useful data is used for visualization.

3. Create Visualizations 
   - The extracted data is visualized using Matplotlib and Seaborn. A line chart is created to show the temperature trend over time:
     - *X-axis*: Timestamps (dates and times).
     - *Y-axis*: Temperatures (in Celsius).
   - The chart is customized with titles, labels, and markers to enhance readability and presentation.

4. Display the Visualization 
   - Finally, the visualization is displayed to the user. The result is a graph that provides insights into weather patterns, making it easier to interpret the forecast.

