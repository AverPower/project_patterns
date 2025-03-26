from subjects import WeatherStation
from observers import PhoneDisplay, TVDisplay

weather_station = WeatherStation()

phone = PhoneDisplay()
tv = TVDisplay()

weather_station.attach(phone)
weather_station.attach(tv)

weather_station.temperature = 25  # Автоматические уведомления!