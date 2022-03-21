import speech_recognition as sr 

r = sr.Recognizer() # recognizer to recognize my audio

temp = input("specify source. do you want to speak: [y/n] ")
if(temp == 'y'):
	# use microphone as source
	with sr.Microphone() as source:  
		print('Speak anything: ')
		audio = r.listen(source)
else:
	harvard_audio = sr.AudioFile('audio_files/harvard.wav') 
	with harvard_audio as source: #using audio file as source
		audio = r.record(source) 

try: 
	# do below
	text = r.recognize_google(audio) 
	print("You said: {}".format(text))
except:
	# if try does not work properly. 
	print("Sorry. Could not recognize your voice.")
