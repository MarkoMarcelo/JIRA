import mysql.connector as sql 
from arbol import MatrizTree,Node
db=sql.connect(
    host="localhost",
    user="root",
    passwd="admin_1572003_jesc",
    database="chatbot"
)
#id=0, fatherLevel=1, fathernumber=2, question=3,  chatbotQuestion=4, answer=5, link=6

cursor = db.cursor()
cursor.execute("SELECT * FROM tree WHERE idtree=1")
r=cursor.fetchall()
firstNode=Node(r[0][3],r[0][5],r[0][6])
tree=MatrizTree(firstNode)

cursor.execute("SELECT * FROM tree WHERE idtree>1")
r=cursor.fetchall()

for i in r:
    tree.addNode(Node(i[3],i[5],i[6]),i[1],i[2])

#tree.print()


#esto es para el chat
pairs=[]


for i in r:
    listQuesAns=[i[4]]
    answer=[i[5]]
    listQuesAns.append(answer)
    pairs.append(listQuesAns)

#print(pairs)


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
    ord('ú'):'u'
}
def clean(text):
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