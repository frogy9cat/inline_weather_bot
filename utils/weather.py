import translate
from pyowm import OWM

def get_weather(place):

    owm = OWM('d6f20a20e277ffd2730c9abe97e35fbc')
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
