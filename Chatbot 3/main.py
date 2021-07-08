from flask import Flask, render_template, request
#import jyserver.Flask as jsf
#import chatbot as ch
from nltk.chat.util import Chat, reflections

import db_connector as db



chatbot = Chat(db.pairs, reflections)


class Respuesta:
    def get_response(self, text):
        text=db.clean(text)
        text=db.correctSentence(text)
        respuesta=chatbot.respond(text)
        if respuesta==None:
            return "No entendi tu pregunta. Cambiala por favor"
        else:
            link=db.tree.getLinkByAnswer(respuesta)
            if link==None:
                return respuesta
            else:
                respuesta+="&"
                respuesta+=link
                #respuesta+=" https://www.unsa.edu.pe/"
                return respuesta#La matricula es apra el viernes .¿ asdasdaas¿asdasdasd¿asdaasdasd¿
    def get_alternatives(self,answer):
        answersList=db.tree.getSons(answer)
        concatenate=""
        for i in answersList:
            concatenate+=i
            concatenate+="-"
        return concatenate

app=Flask(__name__)
bot=Respuesta()



@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get")
def get_response():
    userText=request.args.get('msg')#para recibir el mensaje busca msg en html atributo name=msg
    return bot.get_response(userText)

@app.route("/create")
def get_buttons():
    userText=request.args.get('answer')
    '''if userText=="hola":
        user="hola entre al if-por si acaso"
    else:
        user="hola entre al else-no se como te llamas-pero esta bienb-"'''
    #user=["hola soy el boton","no me des mas problemas"]
    return bot.get_alternatives(userText)


if __name__ == '__main__':
    app.run(debug=True)


# para cerrar el servidor control+c en la terminal