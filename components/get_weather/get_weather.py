import requests

def read_api_key():
    api_config_file_path = 'File_Management/config/api.config'
    try:
        with open(api_config_file_path, 'r') as f:
            api_keys = {}
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    api_keys[key.strip()] = value.strip()
            return api_keys.get('openweathermap_api')
    except FileNotFoundError:
        print(f"API config file '{api_config_file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading API config file: {e}")
        return None

def get_weather(lat, lon):
    api_key=read_api_key()
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"Weather: {weather_description}, Temperature: {temperature}°C"
    else:
        return "Failed to get weather data"
