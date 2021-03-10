# This is the graphical user interface for the chatbot
# library
from tkinter import *
import TrainingData
import Bot_Applications
import numpy as np
import random


def send():
    global res
    special_functions = ["BMI", "Calorie", "Body Fat"]
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)
    if msg != "":
        chatWindow.config(state=NORMAL)
        chatWindow.insert(END, "You: " + msg + '\n\n')
        chatWindow.config(foreground="#442265", font=("Verdana", 12))
        if msg == "quit":
            exit()
        results = TrainingData.model.predict([TrainingData.bag_of_words(msg, TrainingData.words)])[0]
        results_index = np.argmax(results)
        tag = TrainingData.labels[results_index]
        if not special_functions.__contains__(tag):
            if results[results_index] > 0.7:
                for tg in TrainingData.data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']
                res = random.choice(responses)
            else:
                res = "I didn't get that, try again"
        else:
            if results[results_index] > 0.7:
                if tag == "BMI":
                    res = Bot_Applications.cal_bmi()
                elif tag == "Calorie":
                    res= Bot_Applications.set_goal()
                elif tag == "Body Fat":
                    res = Bot_Applications.cal_bodyfat()
            else:
                res = "I didn't get that, try again"
        if res is None:
            res = "Hi! What can I do for you?(type 'quit' to stop)"
        chatWindow.insert(END, "Bot: " + str(res) + '\n\n')
        chatWindow.config(state=DISABLED)
        chatWindow.yview(END)


# Creating GUI with tkinter
# tkinter object
root = Tk()

# window title
root.title("Fitness Bot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

chatWindow = Text(root, bd=0, bg="white", height="8", width="50", font="Arial", )
chatWindow.config(state=DISABLED)

# Bind scrollbar to Chat window
scrollbar = Scrollbar(root, command=chatWindow.yview, cursor="plus")
chatWindow['yscrollcommand'] = scrollbar.set

# create a message window
messageWindow = Text(root, bd=0, bg="grey", width="30", height="4", font=("Arial", 23), foreground="#00ffff")
messageWindow.place(x=128, y=400, height=88, width=260)
scrollbar = Scrollbar(root, command=chatWindow.yview, cursor="plus")
chatWindow['yscrollcommand'] = scrollbar.set

# send button with function send()
Button = Button(root, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                bd=0, bg="grey", activebackground="black", activeforeground="black", fg='#ffffff',
                command=send)

EntryBox = Text(root, bd=0, bg="white", width="29", height="5", font="Arial")

scrollbar.place(x=376, y=6, height=386)
chatWindow.place(x=6, y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
Button.place(x=6, y=401, height=90)


# initial greeting
chatWindow.config(state=NORMAL)
chatWindow.insert(END, "Bot: Hi! What can I do for you?(type 'quit' to stop)" + '\n\n')
chatWindow.config(foreground="#442265", font=("Verdana", 12))
chatWindow.config(state=DISABLED)
chatWindow.yview(END)

