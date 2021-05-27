from nltk.chat.util import Chat, reflections
my_reflexions = {
    "ir":"fui",
    "hola":"hey"
    }
pares = [			#tienes q copiar la primera frase tal y como esta
    [				#el simbolo (.*) significa que puede ir en esa parte otra palabra o palabras. No es obligatorio que vaya algo
        r"se me ha caido el hosting (.*)",#fijate que entre hosting y (.*) hay un espacio
        ["sentimos ese fallo para inicarlo entre en panel",]#	eso hace que si no le pones espacio cuando preguntes no lo entendera
    ],														#si indicas la frase en mayusculas no hay problema igual la detecta
     [
     	r"cuando hay que pagar la factura(.*)",
     	["se paga el 15 de cada mes por tarjeta de crédito",]
    ],
    [
    	r"(.*)ampliar el servicio",#si funciona
    	["Para ampliar el servicio hay q concetar con facturacion",]
    ],
    [
    	r"disculpa(.*)",#palabras cortas con el simbolo, SI las detecta
    	["No pasa nada",]
    ],
    [
    	r"hola || hey || buenas", #si le metes cualquier de estos te responde igual
    	["Hola","Que tal",]
    ],
    [
    	r"que (.*) quieres",#aun no funciona
    	["Nada gracias",]
    ],
    [
    	r"(.*) fuiste creado",#no funciona
    	["Fui creado hoy",]
    ],
    [
    	r"finalizar", #palabras cortas sin uso del simbolo NO las detecta
    	["Chao","Fue bueno hablar contigo"]
    ],
]



def chatear():
    print("hola soy el servicio de hosting")#Primer mensaje  por defecto
    chat = Chat(pares,my_reflexions)
    chat.converse()


if __name__=="__main__":
    chatear()

chatear()
