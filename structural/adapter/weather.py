class YahooWeather:
    def request_weather(self, city):
        return {"city": city, "temp": "+25°C"}

class OpenWeatherMap:
    def get_weather(self, location):
        return {"location": location, "temperature": "25°C"}

class WeatherAdapter:
    def __init__(self, weather_service):
        self.weather_service = weather_service

    def get_weather(self, city):
        data = self.weather_service.request_weather(city)
        return {"location": data['city'], "temperature": data['temp'][1:]}



class YahooWeatherService:
    def get_temp(self, city):
        return f"Температура в {city}: +25°C"

class OpenWeatherService:
    def fetch_weather(self, location):
        return {"location": location, "temp": "25°C"}


class WeatherAdapterService(YahooWeatherService, OpenWeatherService):
    def get_weather(self, city):
        # Если нужно, можно выбрать, какой метод вызывать
        if len(city) < 10:  # Условная логика
            return self.get_temp(city)
        else:
            data = self.fetch_weather(city)
            return f"Температура: {data['temp']}"


def main():
    # Использование метода композиции
    yahoo = YahooWeather()
    adapter = WeatherAdapter(yahoo)
    print(adapter.get_weather("Москва"))  # {'temperature': '+25°C'}

    # Использование метода наследования 
    adapter = WeatherAdapterService()
    print(adapter.get_weather("Москва"))      # "Температура в Москва: +25°C"
    print(adapter.get_weather("Санкт-Петербург"))  # "Температура: 25°C"

if __name__ == '__main__':
    main()