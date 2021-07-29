from nltk.chat.util import Chat, reflections

#Modelo para añadir una nueva pregunta
'''[
    r"(.*)acceder a un link(.*)",#
    ["Cual de los siguientes es su problema con la plataforma de matricula:",]Para mas información ingrese al siguiente enlace
],'''#no te olvides de la  coma



pairs = [			#MATRICULA GENERAL
    [		 	#ANTES	
        r"(.*)reglamento de matricula(.*)",#None
        ["El reglamento es muy importante de conocer. Que desea saber sobre el reglamento de matricula :",]	
    ],														
    [
     	r"(.*)requisitos para la matricula(.*)",#funciona-
     	["Los requisitos para la matricula son los siguientes: copia de DNI y recibo de luz. Sobre que requisito tiene dudas:",]
    ],
    [
     	r"(.*)sobre la matricula(.*)",#funciona-
     	["La matricula es muy importante. En que parte tiene problemas:",]
    ],
    [
     	r"(.*)antes de la matricula(.*)",#funciona-
     	["Estas son las  opciones antes de la matricula",]
    ],
    [
     	r"(.*)plena matricula(.*)",#funciona-
     	["Estas son las  opciones en plena matricula",]
    ],
    [
     	r"(.*)despues de la matricula(.*)",#funciona-
     	["Estas son las  opciones despues de la matricula",]
    ],
    [
    	r"(.*)proceso de matricula(.*)",#funciona-
    	["Para matricularte primero debes acceder a la pagina oficial de la Unsa, luego realizar...",]
    ],
        [	
    	r"(.*)cuando(.*)matricular(.*)",#Es para  fecha, funciona-
    	["Las matriculas comienzan dos semanas despues del examen de admision",]
    ],
    [			#EN PLENA MATRICULA
    	r"(.*)talon de pago(.*)",#funciona-
    	["Cual de los siguientes es su  problema con el talon de pago:",]
    ],
    [
    	r"(.*)acceder a un link(.*)",#   ||(.*)ingresar a un link(.*)||(.*)ingresar a un enlace(.*)
    	["Estos son los enlaces disponibles:",]
    ],
    [
    	r"(.*)plataforma de matricula(.*)",#funciona-
    	["Cual de los siguientes es su problema con la plataforma de matricula:",]
    ],
    [
    	r"(.*)creditos(.*)aprobar(.*)",#  ||(.*)creditos(.*)pasar(.*)
    	["Se necesitan 15 creditos para rpobar el semestre",]
    ],
    [			#DESPUES DE LA MATRICULA
    	r"(.*)hoja de matricula(.*)",#funciona-
    	["Cual de los siguientes es su  problema con la hoja de matricula:",]
    ],
    [			#MATRICULA POR EXEPCION
    	r"(.*)matricula por excepcion(.*)",#funciona
    	["La matricula por excepcion es para:",]
    ],
    [			#Saludos
    	r"Hola(.*)",
    	["Hola igualmente",]
    ],
    [			#Saludos
    	r"(.*)",
    	["No entendi tu pregunta",]
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
#print(pairs)

'''def ChatBot():
    print("Hola soy tu  assistente virtual")
    chatbot = Chat(pairs, reflections)
    respuesta= chatbot.respond("hola como estas")
    print(respuesta)'''

'''if __name__=='__main__':
	ChatBot()'''