from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os 
intello = ChatBot('intl')
intello.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/User/Desktop/py Projects/datasets chatbott/chatterbot-corpus/chatterbot_corpus/data/english/'):
    f = open('C:/Users/User/Desktop/py Projects/datasets chatbott/chatterbot-corpus/chatterbot_corpus/data/english/' + files ,'r').readlines()

    intello.train(f)
while 1 :
    username = input("Enter Your Name: \t")
    message = input(username + ': ')
    if message.strip() != 'Bye' or message.strip() != "See You" :
        reply = intello.get_response(message)
        print("Intello :",reply)
    if message.strip() == 'Bye' or message.strip() == "See You" :
        print("Intello : Bye "+ username)
        break



