
import speech_recognition as s_r
from gtts import gTTS
import openai
import os
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
#module usage
model_engine = "text-davinci-003"
prompt = r.recognize_google(audio)
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=10,
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
os.system(" welcome.mp3")

#print responce
print(response)
