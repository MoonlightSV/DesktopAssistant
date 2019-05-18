from Friday.Friday import Friday as Assistant
import speech_recognition as sr


def run_transcription_loop(type):
    # Слушает команды
    if type == 'текст':
        while True:
            command = input('Жду команду: ')
            Assistant.handle_action(command)

    elif type == 'голос':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            while True:
                Assistant.talkToMe('Слушаю...')
                r.pause_threshold = 0.5
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source)
                print('Думаю...')

                try:
                    command = r.recognize_google(audio, language="ru-RU")
                    print('Вы сказали: ' + command)
                    Assistant.handle_action(command)
                except sr.UnknownValueError:
                    Assistant.talkToMe("Не поняла что вы сказали, попробуйте еще раз...")
                except sr.RequestError as e:
                    print("Не могу получить результат из сервисов Google Speech Recognition: {}".format(e))
                except Exception as e:
                    print("Не могу обработать текст: {}".format(e))


def main():
    Assistant.talkToMe('Приветствую вас')
    type = input('Как вы хотите вводить команды голос/текст: ')
    run_transcription_loop(type)


if __name__ == '__main__':
    main()
