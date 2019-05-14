import pyttsx3
import speech_recognition as sr
from WSM.sound import Sound
import re
import webbrowser
import time


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
        # r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print('Думаю...')
        command = r.recognize_google(audio, language="ru-RU").lower()
        print('Вы сказали: ' + command + '\n')

    # Возвращаемся к началу, чтобы продолжить слушать команды, если получена неузнаваемая речь
    except sr.UnknownValueError:
        talkToMe('Вас не слышно, попробуйте еще раз...')
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

    elif 'выход' in command:
        talkToMe('До свидания')
        exit()


engine = pyttsx3.init()
# Sound.init()

talkToMe('Приветствую вас')

# Цикл для продолжения выполнения нескольких команд
while True:
    assistant(myCommand())
