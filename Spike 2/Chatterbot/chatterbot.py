from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chat = ChatBot('cctmx')
trainer = ChatterBotCorpusTrainer(chat)
trainer.train("chatterbot.corpus.spanish.greetings")
while True:
    peticion = input('Tu: ')
    respuesta = chat.get_response(peticion)
    print('Bot: ', respuesta)