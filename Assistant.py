import pyttsx3
import speech_recognition as sr
from WSM.sound import Sound


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
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="ru-RU").lower()
        print('Вы сказали: ' + command + '\n')

    # Возвращаемся к началу, чтобы продолжить слушать команды, если получена неузнаваемая речь
    except sr.UnknownValueError:
        talkToMe('Вас не слышно, попробуйте еще раз...')
        command = myCommand()

    return command


def assistant(command):
    # Усолвия длявыполнения команд

    if 'без звука' in command:
        Sound.mute()


engine = pyttsx3.init()

talkToMe('Приветствую вас')

# Цикл для продолжения выполнения нескольких команд
while True:
    assistant(myCommand())