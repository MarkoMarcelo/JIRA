from flask import Flask, render_template, request
import jyserver.Flask as jsf
import chatbot as ch


class Respuesta:
    def get_response(self, text):
        chatbot = ch.Chat(ch.pairs, ch.reflections)
        respuesta=chatbot.respond(text)
        while True:
            return respuesta#La matricula es apra el viernes .¿ asdasdaas¿asdasdasd¿asdaasdasd¿

app=Flask(__name__)
bot=Respuesta()



@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get")
def get_response():
    userText=request.args.get('msg')#para recibir el mensaje
    return bot.get_response(userText)

if __name__ == '__main__':
    app.run(debug=True)


# para cerrar el servidor control+c en la terminal