import mysql.connector as sql 
import json


#Esats dos van juntas
mapeo={
    ord('á'):'a',
    ord('é'):'e',
    ord('í'):'i',
    ord('ó'):'o',
    ord('ú'):'u',
    ord('Â'):'',
    ord('Ã'):'',
    ord('¡'):'á',#creo q lo bajamos a sin tilde
    ord('©'):'é',
    ord('Ã'):'í', 
    ord('³'):'ó',
    ord('º'):'ú', 
    ord('‘'):'Ñ',
    ord('±'):'ñ'

}
def clean(text):#aqui peude meter string o texto
    text=text.translate(mapeo)
    return text

from arbol import MatrizTree,Node
db=sql.connect(
    host="localhost",
    user="root",
    passwd="admin_1572003_jesc",
    database="chatbot"
)
#id=0, fatherLevel=1, fathernumber=2, question=3,  chatbotQuestion=4, answer=5, link=6
#id=0, fatherLevel=1, fathernumber=2, tag=3,  questions=4, answer=5, link=6
cursor = db.cursor()
cursor.execute("SELECT * FROM chatbot_tree WHERE fatherLevel=0 AND fatherNumber=0")
r=cursor.fetchall()
#print(r)
tmp1=r[0][4].split("-")
tmp2=r[0][5].split("-")
firstNode=Node(tmp1[0],tmp2[0],r[0][6])#el padre de la base de datos solo debe tener
tree=MatrizTree(firstNode)

cursor.execute("SELECT * FROM chatbot_tree")
r=cursor.fetchall()

#esto es para la creacion del archivo json que almacenara  preguntas y respuestas

data={}#esto se convertira en json para el entranamiento del bot

data['intents']=[]


#esto es para el chat
pairs=[]

for i in r:
    '''
    listQuesAns=[i[4]]
    answer=[i[5]]
    listQuesAns.append(answer)
    pairs.append(listQuesAns)
    '''
    apoyo1=clean(i[4])
    apoyo2=clean(i[5])
    #preguntas=i[4].split("-")
    #respuestas=i[5].split("-")
    preguntas=apoyo1.split("-")
    respuestas=apoyo2.split("-")

    data['intents'].append({'tag':preguntas[0],'patterns':preguntas, 'responses':respuestas})

    #tree.addNode(Node(i[3],i[5],i[6]),i[1],i[2])
    if(i[1]>0 and i[2]>0):
        tree.addNode(Node(preguntas,respuestas,i[6]),i[1],i[2])

#tree.print()
#print(pairs)
#para crear el archivo json
#print(data)
with open('intents.json', 'w') as  file:
    json.dump(data, file, indent=4)#este 4 es la cantidad de espacios que llevara la identacion

#esto es para la limpieza
from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize

spanish=SpellChecker(language='es')

def correctSentence(text):
    newtext=""
    words=word_tokenize(text)
    for word in words:
        newtext+= spanish.correction(word)
        newtext+=" "
    return newtext

#Esats dos van juntas
mapeo={
    ord('á'):'a',
    ord('é'):'e',
    ord('í'):'i',
    ord('ó'):'o',
    ord('ú'):'u',
    ord('Â'):'',
    ord('Ã'):'',
    ord('¡'):'á',#creo q lo bajamos a sin tilde
    ord('©'):'é',
    ord('Ã'):'í', 
    ord('³'):'ó',
    ord('º'):'ú', 
    ord('‘'):'Ñ',
    ord('±'):'ñ'

}
def clean(text):#aqui peude meter string o texto
    text=text.translate(mapeo)
    return text

#pruebas
'''
texto="desde cuando es la mátricual?"
print(texto)
texto=texto.translate(mapeo)
print(texto)
newTexto=correctSentence(texto)
print(newTexto)
'''