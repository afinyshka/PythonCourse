from pyowm import OWM
from pyowm.utils.config import get_default_config
from os import getenv
from sys import exit


pyowm_api = getenv('PYOWM_API')
if not pyowm_api:
    exit("Error: no API provided")

owm = OWM(pyowm_api)
mgr = owm.weather_manager()
config_dict = get_default_config()
config_dict['language'] = 'ru'


def weather(place: str='Москва') -> str:
    observation = mgr.weather_at_place(place)  # the observation object is a box containing a weather object
    w = observation.weather
    # temperature
    t = w.temperature("celsius")
    t1 = t['temp']
    t2 = t['feels_like']
    t3 = t['temp_max']
    t4 = t['temp_min']
    # wind speed
    wi = w.wind()['speed']
    # humidity
    humi = w.humidity
    # cloudness
    cl = w.clouds
    # status (detailed)
    current_status = w.detailed_status  # detailed version of status (eg. 'light rain')
    # pressure
    pr = w.pressure['press']
    # visibility
    vd = w.visibility_distance

    show_weather = (f'Погода в городе {place}:\n\nтемпература {int(t1)}ºC\nощущается как {int(t2)}ºC\nмаксимальная температура {int(t3)}ºC\nминимальная температура {int(t4)}ºC\n'          
          f"cкорость ветра {wi} м/с\nвлажность {humi}%\nоблачность {cl}%\nстатус погоды {current_status}\nдавление {pr} мм рт.ст\nвидимость {vd} м")
    return show_weather

weather()
# daily_forecast = mgr.forecast_at_place(place, 'daily').forecast
# three_h_forecast = mgr.forecast_at_place(place, '3h').forecast
