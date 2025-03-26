class YahooWeather:
    def request_weather(self, city):
        return {"city": city, "temp": "+25°C"}

class OpenWeather:
    def get_weather(self, location):
        return {"location": location, "temperature": "25°C"}

class WeatherAdapter:
    def __init__(self, weather_service):
        self.weather_service = weather_service

    def get_weather(self, city):
        data = self.weather_service.request_weather(city)
        return {"location": data['city'], "temperature": data['temp'][1:]}


class WeatherAdapterService(YahooWeather, OpenWeather):
    def get_weather(self, city):
        data = self.request_weather(city)
        return {"location": data['city'], "temperature": data['temp'][1:]}


def main():
    # Использование метода композиции
    yahoo = YahooWeather()
    adapter = WeatherAdapter(yahoo)
    print(adapter.get_weather("Москва"))  # {'temperature': '+25°C'}

    # Использование метода наследования 
    adapter = WeatherAdapterService()
    print(adapter.get_weather("Москва"))      # "Температура в Москва: +25°C"

if __name__ == '__main__':
    main()