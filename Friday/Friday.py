import pyttsx3
from WSM.sound import Sound
import re
import time
import pyowm


class Friday(object):
    engine = pyttsx3.init()

    @classmethod
    def talkToMe(cls, text):
        # Произносит переданный текст

        print(text)
        cls.engine.say(text)
        cls.engine.runAndWait()

    @classmethod
    def handle_action(cls, command):
        # Условия для выполнения команд
        command = command.lower()

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
                cls.talkToMe('Все говорят ' + comm + ', а ты купи слона')
                # comm = myCommand()
            cls.talkToMe('Сразу бы сказали, что не купите')

        elif 'погода в городе' or 'в городе' in command:  # Иногда не слышит слово "погода"
            reg_ex = re.search('(погода )?в городе (.+)', command)
            if reg_ex:
                from pyowm.exceptions import api_response_error
                try:
                    place = reg_ex.group(2)
                    owm = pyowm.OWM('fd3ef8f70c1f9039e62de497f7fe7375', language='ru')
                    observation = owm.weather_at_place(place)
                    w = observation.get_weather()
                    cls.talkToMe('В городе ' + place.title() + ' сейчас ' + w.get_detailed_status()
                             + ' температура ' + str(int(w.get_temperature('celsius')['temp'])) + ' градусов')
                except api_response_error.NotFoundError:
                    cls.talkToMe('Такого города нет')
            else:
                cls.talkToMe('Вы не назвали город, скажите еще раз')

        elif 'выход' in command:
            cls.talkToMe('До свидания')
            exit()

        else:
            cls.talkToMe('Такого я еще не умею')