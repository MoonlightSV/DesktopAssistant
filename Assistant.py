import pyttsx3
import speech_recognition as sr
from WSM.sound import Sound
import re
import time
import pyowm


def talkToMe(text):
    # Произносит переданный текст

    print(text)
    engine.say(text)
    engine.runAndWait()


def myCommand():
    # Слушает команды

    r = sr.Recognizer()

    with sr.Microphone() as source:
        talkToMe('Слушаю...')
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        print('Думаю...')
        command = r.recognize_google(audio, language="ru-RU").lower()
        print('Вы сказали: ' + command)

    # Возвращаемся к началу, чтобы продолжить слушать команды, если получена неузнаваемая речь
    except sr.UnknownValueError:
        talkToMe('Не поняла что вы сказали, попробуйте еще раз...')
        command = myCommand()

    return command


def assistant(command):
    # Условия для выполнения команд

    if 'без звука' in command:
        Sound.mute()

    elif 'включи звук' in command:
        Sound.mute()

    elif 'громче' in command:
        for i in range(5):
            Sound.volume_up()
            time.sleep(0.2)

    elif 'тише' in command:
        for i in range(5):
            Sound.volume_down()
            time.sleep(0.2)

    elif 'купи слона' in command:
        comm = command
        while 'не куплю' not in comm:
            talkToMe('Все говорят ' + comm + ', а ты купи слона')
            comm = myCommand()
        talkToMe('Сразу бы сказали, что не купите')

    elif 'погода в городе' or 'в городе' in command:  # Иногда не слышит слово "погода"
        reg_ex = re.search('(погода )?в городе (.+)', command)
        if reg_ex:
            from pyowm.exceptions import api_response_error
            try:
                place = reg_ex.group(2)
                owm = pyowm.OWM('fd3ef8f70c1f9039e62de497f7fe7375', language='ru')
                observation = owm.weather_at_place(place)
                w = observation.get_weather()
                talkToMe('В городе ' + place.title() + ' сейчас ' + w.get_detailed_status()
                         + ' температура ' + str(int(w.get_temperature('celsius')['temp'])) + ' градусов')
            except api_response_error.NotFoundError:
                talkToMe('Такого города нет')
        else:
            talkToMe('Вы не назвали город, скажите еще раз')

    elif 'выход' in command:
        talkToMe('До свидания')
        exit()

    else:
        talkToMe('Такого я еще не умею')


engine = pyttsx3.init()

talkToMe('Приветствую вас')

# Цикл для продолжения выполнения нескольких команд
while True:
    assistant(myCommand())
