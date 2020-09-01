from chatterbot import ChatBot
bot = ChatBot("Gedion")
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
engine=pp.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(word):
    engine.say(word)
    engine.runAndWait()

conversation = [
    "Hello",
    "Hi there!",
    "what is your name ?",
    "My name is bot",
    "How are you?",
    "I am doing great these days",
    "Thank you",
    "In which city you live?",
    "I live in pune",
    "In which language you talk?",
    "I talk mostly in English",
    "I have a query",
    "tell me the query",
    "what is corona?",
    "It is type of a virus causing infectious disease ",
    "how many positive corona cases are currently in India? ",
    "There are over 5 Lakhs positive cases in India "

]
trainer = ListTrainer(bot)
trainer.train(conversation)
#answer=bot.generate_response("How are you doing?")
#print(answer)
#print("Talk to bot")
'''while True:
    query=input()
    if query=="exit":
        break
    answer=bot.get_response(query)
    print("Bot: ",answer)'''
main=Tk()
main.geometry("560x650")
main.title("My ChatBot")
img=PhotoImage(file="bot1.png")
photolabel=Label(main,image=img)
photolabel.pack(pady=5)
'''def take_query():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("Your Bot is Listening..try to speak")
    with s.Microphone() as source:
        try:
            audio=sr.listen(source)
            query=sr.recognize_google(audio,language='eng-in')
            print(query)
            texF.delete(0,END)
            texF.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("Not recognized")'''


def ask_from_bot():
    query=texF.get()
    answer_from_bot=bot.get_response(query)
    msg.insert(END,"You: "+query)
    msg.insert(END,"Bot: "+str(answer_from_bot))
    speak(answer_from_bot)
    texF.delete(0,END)
    msg.yview(END)
    #print("clicked")

frame=Frame(main)
sc=Scrollbar(frame)
msg=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msg.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
#creating text field
texF=Entry(main,font=("Verdana",20))
texF.pack(fill=X,pady=10)
btn=Button(main,text="Ask from bot",font=("Verdana",20),command=ask_from_bot)
btn.pack()
def enter_function(event):
    btn.invoke()


#going to bind main window with enter key
main.bind('<Return>',enter_function)

'''def repeatl():
    while True:
        take_query()
t=threading.Thread(target=repeatl())
t.start()'''
main.mainloop()
