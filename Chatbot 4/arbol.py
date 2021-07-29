'''class Node():
    def __init__(self, pregunta,respuesta):
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.sons=[]

class FatherNode(Node):
    def __init__(self,pregunta,respuesta):
        Node.__init__(self,pregunta,respuesta)
        self.diagram=[1]
    def addNode(self,pregunta,respuesta,fatherLevel,fatherPosition):
        newnode=Node(pregunta,respuesta,fatherLevel,fatherPosition)
        if fatherLevel>len(self.sons):
            self.diagram.append(1)
        r=self.sons
        for i in range(fatherLevel-2):
            r=self.sons
        r.append(newnode)
        son=SonNode(pregunta,respuesta,fatherLevel,fatherPosition)


class SonNode(Node):
    def __init__(self,pregunta,respuesta,fatherLevel,fatherPosition):
        Node.__init__(self,pregunta,respuesta)
        self.fatherLevel=fatherLevel
        self.fatherPosition=fatherPosition

'''
'''class Arbol(Node):
    def __init__(self,pregunta,respuesta):
        Node.__init__(self,pregunta,respuesta)
        self.nodes=[1]
    def addNode(self,level,position):
        if level>len(self.lista):

        for i in range(col):
'''
'''
class Node():
    def __init__(self,pregunta,respuesta,fatherLevel,fatherPosition):
        self.pregunta=pregunta
        self.respuesta=respuesta
        self.fatherLevel=fatherLevel
        self.fatherPosition=fatherPosition
'''
class MatrizTree():
    def __init__(self,cabeza):
        self.rows=1#esto significa que el padre de todos se encuentra en el nivel 1 y fila 1 para el usuario
        self.columns=1#no se si servira por el momento
        self.matriz=[[cabeza]]
    def addNode(self,Node,row,column):
        if(row+1>self.rows):
            helper=[]
            self.matriz.append(helper)
            self.rows+=1

        con=0
        temp=self.matriz[row-1]#no para el programador
        for j in range (column):
            con+=temp[j].sons

        self.matriz[row].insert(con,Node)
        self.matriz[row-1][column-1].sons+=1
    def getSons(self,answer):#devuelve una lista con las preguntas de los hijos
        sons=[]#almacenar las preguntas de los hijos
        con=0#se encuentras a  la izquierda  del hijo o padre
        fathernivel=0#nivel del padre del q buscamos
        numberSons=0#numeros de hijos del padre q buscamos
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                #if self.matriz[i][j].respuesta==answer:
                if answer in self.matriz[i][j].respuesta:
                    fathernivel=i
                    numberSons=self.matriz[i][j].sons
                    for k in range(j):
                        con+=self.matriz[i][k].sons
        for i in range(numberSons):
            sons.append(self.matriz[fathernivel+1][i+con].pregunta[0])#le puse  un corchete con cero porque la primera pregunta es la q debe devolver ya q es  la mas importante
        return sons
    
    def getLinkByAnswer(self,answer):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j].respuesta==answer:
                    return self.matriz[i][j].link
        return None



    def print(self):
        for i in range(self.rows):
            if len(self.matriz[i])==0:
                print("[vacio]")
            else:
                for j in self.matriz[i]:
                    print(j)


class Node():
    def __init__(self, pregunta,respuesta,link):#pregunta de ser una lista de preguntas, respuesta deb ser una lista de posibles respuestas
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.link=link
        self.sons=0#numero de hijos q tiene
    def __str__(self):
        return (self.pregunta+" - "+self.respuesta)


'''node=Node("Hola","Hola igualmente")
arbol=MatrizTree(node)
node1=Node("(*)cuando(*)se puede matricular","Se puede matricular despues de dos semans del examen")
arbol.addNode(node1,1,1)
arbol.addNode(Node("Derecha","Este es el q buscamos"),1,1)
arbol.addNode(Node("Izquierda","Izquierda"),2,1)
arbol.addNode(Node("Izquierda","Derecha"),2,1)
arbol.addNode(Node("Derecha","Izquierda"),2,2)
arbol.addNode(Node("Derecha","Derecha"),2,2)
arbol.print()
print(arbol.getSons("Este es el q buscamos"))'''