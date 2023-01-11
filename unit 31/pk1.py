import pyttsx3
print('talking friend')
vtf=pyttsx3.init()
vtf = pyttsx3.init()
voices = vtf.getProperty('voices')
vtf.setProperty('voice', voices[1].id)
rate = vtf.getProperty('rate')
print(rate)
vtf.setProperty('rate', 140)
vtf.say("hello durgarao")
vtf.runAndWait()

def vtf_speak():
    print('speaking......')
    vtf.say(txt)
    vtf.runAndWait()
txt='heyfriend,i am your varitual taking friend'
vtf_speak()
txt=input('what should i say:')
vtf_speak()
while txt!='bye':
    txt=input('what should i say')
    txt=txt.lower()
    vtf_speak()