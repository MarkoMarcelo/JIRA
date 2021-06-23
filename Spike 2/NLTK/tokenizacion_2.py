from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
text = "God is Great! I won a lottery."
print(word_tokenize(text))#esta funcion devuelve una lista separando 
print(sent_tokenize(text))#esta funcion devuelve una lista con suboraciones

text2="Hola mi nombre es John. Soy ingresante a CPCC. Estoy feliz!" #funciona en español o ingles
print(word_tokenize(text2))
print(sent_tokenize(text2))

#haciendo pruibas dentro de github para

