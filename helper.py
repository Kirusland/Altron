import pyaudio
import speech_recognition as sr
import random



r = sr.Recognizer()
greetings = ["Здравствуйте!","Приветик!", "Привет, пупсик!", "Привет, как дела?"]
films = ["Кухня","Смешарики","Джуманджи"]
while True:
    with sr.Microphone(device_index=1) as source: 
        print("Скажите что-нибудь ...")
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio, language="ru_RU").lower()
        print("Вы сказали: " + speech)

        if "привет" in speech:  
            print(random.choice(greetings))
        elif "фильм" in speech:  
                print("Посмотрите "+random.choice(films))
        elif "открой файл" in speech:
            os.startfile("C:/Users/Ученик/Downloads/inecraft_death.wav")
        elif "youtube" in speech:
            webbrowser.open_new("https://www.youtube.com/?gl=RU&hl=ru")
        elif speech == "пока" in speech:  
            print("До свидания")
            break
        else:
            print("Я вас не понимаю, повторите пожалуйста")
    except:
        print("Ошибка")
