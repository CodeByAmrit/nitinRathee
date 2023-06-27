import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from multiprocessing import Process

class alexa:
   listener = sr.Recognizer()

   engine = pyttsx3.init()
   voices = engine.getProperty("voices")
   engine.setProperty('voice', voices[1].id)

   def engine_talk(self, text):
      self.engine.say(text)
      self.engine.runAndWait()

   def user_commands(self):
      try:
         with sr.Microphone() as source:
            print("Start Speaking!!")
            voice = self.listener.listen(source)
            command = self.listener.recognize_google(voice)
            command = command.lower()
         if 'alexa' in command:
               command = command.replace('alexa', '')
               print(command)

      except:
         pass
      return command 
   
   def run_alexa(self):
      command = self.user_commands()
      if 'play' in command:
         song = command.replace('play', '')
         print(command)
         self.engine_talk('playing' +command)
         pywhatkit.playonyt(song)

      elif 'time' in command:
         time = datetime.datetime.now() .strftime('%I:M %p')
         self.engine_talk('The current time is' +time)
      elif 'who is' in command:
         name = command.replace('who is', '')
         info = wikipedia.summary(name, 3)
         print(info)
      elif 'joke' in command:
         self.engine_talk(pyjokes.get_joke())
      else:
         self.engine_talk('i could not hear you properly')

assistant1 = alexa()
def run1():
   assistant1.run_alexa() 
 

if __name__ == "__main__":
   
   process1 = Process(target=run1)  
   process1.start()      
 
        
