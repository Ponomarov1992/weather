from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
# Ставим в программу наш ключ API полученый из мета-центра
owm = OWM('6e4b8415e08ed825a1f35afe82f7cc50', config_dict)
reg = owm.city_id_registry()
version_tuple = (major, minor, patch) = owm.version
mgr = owm.weather_manager()



# Получаем от пользователя место его положения Город/Страна
place = input("Укажите в каком городе/стране Вы находитесь: ")

observation = mgr.weather_at_place(place)
observation.weather.detailed_status

w = observation.weather

temp = w.temperature('celsius')["temp"]



print("Температура сейчас в " + place + " в районе " + str(temp))

if temp < 10:
    print("Сейчас очень холодно.\nОденься потеплее")
elif temp > 15 and temp < 20:
    print("На улице прохладно.\nНакинь легкую кофту")
else:
    print("Можешь одеться легко.\nНа улице прекрасная погода!")