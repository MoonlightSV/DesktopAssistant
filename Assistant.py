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
                Assistant.handle_action(command)
                print('Вы сказали: ' + command)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service: %s", e)
            except Exception as e:
                print("Could not process text: %s", e)


def main():
    Assistant.talkToMe('Приветствую вас')
    run_transcription_loop()


if __name__ == '__main__':
    main()
