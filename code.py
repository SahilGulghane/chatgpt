
import speech_recognition as s_r
from gtts import gTTS
import openai
from pygame import mixer
import time
import smtplib, ssl


#key
openai.api_key = "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"
#input form mike
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=0) #my device index is 1, you have to put your device index
with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source) #reduce noise
    audio = r.listen(source) #take voice input from the microphone

#print promt query
print(r.recognize_google(audio))
my_string = r.recognize_google(audio)
#module usage
model_engine = "text-davinci-003"
prompt = r.recognize_google(audio)
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.5,
)
#collect responce
response = completion.choices[0].text

language = 'en'
#convert  text to mp3 file
myobj = gTTS(text=response, lang=language, slow=False)
myobj.save("welcome.mp3")


# Playing the converted file

mixer.init()
mixer.music.load("welcome.mp3")
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)
#print responce

import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "sahilgulghane22@gmail.com"
receiver_email = "tanishawadibhasme520@gmail.com"
password = 'kmdzkhzoxzypwltw'
message = response
Subject: "Hi there"


context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
print(response)
