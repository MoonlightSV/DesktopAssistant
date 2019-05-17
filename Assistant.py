from Friday.Friday import Friday as Assistant
import speech_recognition as sr


def run_transcription_loop():
    # Слушает команды

    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            Assistant.talkToMe('Слушаю...')
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
    run_transcription_loop()


if __name__ == '__main__':
    main()
