
class WeatherDataFetcher:
    def __init__(self, city):
        self.city = city
        
        print(f"Fetching weather data for {city}...")
        
    

class DataParser:
    def __init__(self, weather_data):

        self.weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }
        city = weather_data["city"] = city
        temperature = weather_data["temperature"] = temperature
        condition = weather_data["condition"] = condition
        humidity = weather_data["humidity"] = humidity
        return (f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%")
        

class UserInterface:
    def __init__(self, city, temperature, condition):
        self.city = city
        self.temperature = temperature
        self.condition = condition

        weather_report = (f" {city} is {temperature} degress and {condition}")
        return weather_report

print("Welcome to our Weather Forecast Application!")

def main():
    while True:
        city = input("Enter your chosen city, type 'exit' to quit: ").lower()
        if city == 'exit':
            print("Exiting system")
            break
        else:
            WeatherDataFetcher(city)
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == "no":
                print(UserInterface)
            elif detailed == 'yes':
                print(DataParser.__dict__)
            else:
                print("No weather data for that city available")

if __name__ == "__main__":
    main()