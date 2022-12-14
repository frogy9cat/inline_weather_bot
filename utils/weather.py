import translate
from pyowm import OWM
from data.config import API_KEY

def get_weather(place):

    owm = OWM('a9bb79421a0c8f4356078b8fe54d4911')
    owm = OWM('API_KEY')
    mgr = owm.weather_manager()

    translator = translate.Translator("ru")
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    status = w.detailed_status
    wind = w.wind()["speed"]
    tstatus = translator.translate(status)
    temp = str(temp)

    return f"Город/страна {place}:\n\nТемпература: {temp} градусов по цельсию.\nСтатус: {tstatus}\nВетер: {wind} м/сек."
