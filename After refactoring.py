
class WeatherDataFetcher:
    def __init__(self):
        self.weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }
        
    def fetch_weather_data(self, city):
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})

class DataParser:
    def __init__(self):
        pass

    def parse_weather_data(self, data):
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
        #return (f"Weather in {self.city}: {self.temperature} degrees, {self.condition}, Humidity: {self.humidity}%")
        

class UserInterface:
    def __init__(self):
        self.data_fetcher = WeatherDataFetcher()
        self.data_parser = DataParser()

    def get_detailed_forecast(self, city): #get a detailed weather forecast for a city
        data = self.data_fetcher.fetch_weather_data(city)
        return self.data_parser.parse_weather_data(data)
      
    def display_weather(self, city): #display basic weather forecast for a city
        data = self.data_fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.data_parser.parse_weather_data(data)
            print(weather_report)
    


print("Welcome to our Weather Forecast Application!")

def main():

    user_interface = UserInterface()

    while True:
        city = input("Enter your chosen city, type 'exit' to quit: ")
        if city == 'exit':
            print("Exiting system")
            break
        else:
            WeatherDataFetcher()
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == "no":
                print(user_interface.display_weather(city))
            elif detailed == 'yes':
                print(user_interface.get_detailed_forecast(city))
            else:
                print("No weather data for that city available")

if __name__ == "__main__":
    main()