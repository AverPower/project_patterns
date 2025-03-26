import requests

class WeatherService:
    def get_weather(self, city):
        url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_KEY&q={city}"
        response = requests.get(url)
        return response.json()

class WeatherProxy:
    def __init__(self):
        self._service = WeatherService()
        self._cache = {}

    def get_weather(self, city):
        if city not in self._cache:
            print(f"Запрос к API для {city}")
            self._cache[city] = self._service.get_weather(city)
        else:
            print(f"Данные из кеша для {city}")
        return self._cache[city]

# Клиентский код
proxy = WeatherProxy()
print(proxy.get_weather("Moscow"))  # Запрос к API
print(proxy.get_weather("Moscow"))  # Данные из кеша