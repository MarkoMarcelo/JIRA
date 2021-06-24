from nltk.chat.util import Chat, reflections

#Modelo para añadir una nueva pregunta
'''
[
    r"(.*)acceder a un link(.*)",#
    ["Cual de los siguientes es su problema con la plataforma de matricula:",]
],
'''#no te olvides de la  coma



pairs = [			#MATRICULA GENERAL
    [		 	#ANTES	
        r"(.*)reglamento de matricula(.*) ",#None
        ["El reglamento es una base importante. Acceda al iguiente link:",]	
    ],														
    [
     	r"(.*)requisitos para la matricula(.*)",#funciona-
     	["Los requisitos son los siguientes. Para mas información ingrese al siguiente enlace: ",]
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
    	r"(.*)link(.*)",   
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
    	["Hola igualmente.",]
    ],
    [			#Saludos
    	r"(.*)",
    	["No entendi tu pregunta,intenta de nuevo.",]
    ],
    [
    	r"buenos dias(.*)",#	||buenas tardes
    	["Buenos dias",]
    ],
    [			#Despedidas
    	r"muchas gracias", 
    	["No te preocupes, es mi trabajo."]
    ],
]