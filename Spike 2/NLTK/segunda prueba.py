from nltk.chat.util import Chat, reflections

#Modelo para añadir una nueva pregunta
'''[
    r"(.*)acceder a un link(.*)",#
    ["Cual de los siguientes es su problema con la plataforma de matricula:",]
],'''#no te olvides de la  coma



pairs = [			#MATRICULA GENERAL
    [		 	#ANTES	
        r"(.*)reglamento de matricula(.*) ",#None
        ["El reglamento es una base importante. Acceda al iguiente link:",]	
    ],														
    [
     	r"(.*)requisitos para la matricula(.*)",#funciona-
     	["Los requisitos son los siguientes. Para mas información ingrese al siguiente enlace",]
    ],
    [
    	r"(.*)proceso de matricula(.*)",#funciona-
    	["Para matricularte primero debes acceder a la pagina oficial de la Unsa",]
    ],
        [	
    	r"(.*)cuando(.*)matricular(.*)",#Es para  fecha, funciona-
    	["Puedes matricularte  hasta dos semanas despues del examen",]
    ],
    [			#EN PLENA MATRICULA
    	r"(.*)talon de pago(.*)",#funciona-
    	["Cual de los siguientes es su  problema con el talon de pago:",]
    ],
    [
    	r"(.*)acceder a un link(.*)",#redirecion plataforma de matricular   ||(.*)ingresar a un link(.*)||(.*)ingresar a un enlace(.*)
    	["Cual de los siguientes es su problema con la plataforma de matricula:",]
    ],
    [
    	r"(.*)plataforma de matricula(.*)",#funciona-
    	["Cual de los siguientes es su problema con la plataforma de matricula:",]
    ],
    [
    	r"(.*)creditos(.*)aprobar(.*)",#redirecciona plataforma de MATRICULA   ||(.*)creditos(.*)pasar(.*)
    	["Cual de los siguientes es su problema con la plataforma de matricula:",]
    ],
    [			#DESPUES DE LA MATRICULA
    	r"(.*)hoja de matricula(.*)",#funciona-
    	["Cual de los siguientes es su  problema con la hoja de matricula:",]
    ],
    [			#Saludos
    	r"Hola(.*)",
    	["Hola igualmente",]
    ],
    [
    	r"buenos dias(.*)",#	||buenas tardes
    	["Buenos dias",]
    ],
    [			#Despedidas
    	r"muchas gracias", 
    	["No te preocupes, es mi trabajo"]
    ],
]
def firstChatBot():
 	print("Hola soy tu  assistente virtual")
 	chatbot = Chat(pairs, reflections)
 	chatbot.converse()

if __name__=='__main__':
	firstChatBot()