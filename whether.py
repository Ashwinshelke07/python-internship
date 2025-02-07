import requests

def get_weather(api_key, city_name, units='metric'):
    """
    Fetches weather data for a given city using the OpenWeatherMap API.

    Parameters:
        api_key (str): Your OpenWeatherMap API key.
        city_name (str): The name of the city to fetch weather data for.
        units (str): The unit of measurement for temperature ('metric' or 'imperial').

    Returns:
        dict: Weather data if the request is successful, None otherwise.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': units
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        if data.get('cod') != 200:
            print(f"Error: {data.get('message')}")
            return None
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except ValueError as json_err:
        print(f"JSON decoding error: {json_err}")
    return None

def display_weather(data, units='metric'):
    """
    Displays the weather information in a user-friendly format.

    Parameters:
        data (dict): The weather data to display.
        units (str): The unit of measurement for temperature ('metric' or 'imperial').
    """
    if data:
        city = data.get('name')
        country = data.get('sys', {}).get('country')
        temperature = data.get('main', {}).get('temp')
        humidity = data.get('main', {}).get('humidity')
        pressure = data.get('main', {}).get('pressure')
        wind_speed = data.get('wind', {}).get('speed')
        weather_description = data.get('weather', [])[0].get('description')

        temp_unit = '°C' if units == 'metric' else '°F'
        wind_unit = 'm/s' if units == 'metric' else 'mph'

        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temperature}{temp_unit}")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind Speed: {wind_speed} {wind_unit}")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print("Weather data not available.")

def main():
    """
    Main function to execute the weather application.
    Prompts the user for input and displays the weather information.
    """
    api_key = input("Enter your OpenWeatherMap API key: ")
    city_name = input("Enter the city name: ")
    units_input = input("Enter the unit of measurement ('metric' for Celsius, 'imperial' for Fahrenheit): ").strip().lower()
    units = 'metric' if units_input == 'metric' else 'imperial'

    weather_data = get_weather(api_key, city_name, units)
    display_weather(weather_data, units)

if __name__ == "__main__":
    main()
