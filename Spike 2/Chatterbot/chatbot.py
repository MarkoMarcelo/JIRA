from chatterbot import ChatBot
import chatterbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging 
logging.basicConfig(filename='archivarlog.log',level=logging.DEBUG)

chatbot = ChatBot('ChaloBot')

entrenador = ChatterBotCorpusTrainer(chatbot)

entrenador.train('chatterbot.corpus.spanish')

while True:
    solicitud = input('Yo: ')
    respuesta = chatbot.get_response(solicitud)
    print('ChatBot: ',respuesta)