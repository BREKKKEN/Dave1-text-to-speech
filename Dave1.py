import pyttsx3
print("""██████╗░░█████╗░██╗░░░██╗███████╗░░███╗░░
██╔══██╗██╔══██╗██║░░░██║██╔════╝░████║░░
██║░░██║███████║╚██╗░██╔╝█████╗░░██╔██║░░
██║░░██║██╔══██║░╚████╔╝░██╔══╝░░╚═╝██║░░
██████╔╝██║░░██║░░╚██╔╝░░███████╗███████╗
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝ """)
print("Loading...")
while True:
   text_speech = pyttsx3.init()
   awnser = input("> ")
   text_speech.say(awnser)
   text_speech.runAndWait()
   if awnser == 'exit':
      break