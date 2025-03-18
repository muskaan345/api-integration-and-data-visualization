import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "bf9eb8a010a12772bad67d5f7f785a2c"  # Replace with the API key you copied
CITY = "Mumbai"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    # Extract and print weather details
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather = data['weather'][0]['description']

    print(f"City: {CITY}")  
    print(f"Temperature: {temperature}°C")  
    print(f"Humidity: {humidity}%")  
    print(f"Weather: {weather}")  
else:
    print(f"Failed to get data for {CITY}. Status code: {response.status_code}")

# Now for the temperature comparison across cities
cities = ["Mumbai", "Delhi", "New York", "London", "Tokyo"]
temps = []

for city in cities:
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        temps.append(data['main']['temp'])
    else:
        print(f"Failed to get data for {city}. Status code: {response.status_code}")
        temps.append(None)  # Append None if data is unavailable for a city

# Create a bar plot
sns.barplot(x=cities, y=temps)
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Comparison Across Cities")
plt.show()
