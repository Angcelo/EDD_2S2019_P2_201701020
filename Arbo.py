import os

class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.izquierda=None
        self.derecha=None
        self.equilibrio=0

class Arbol():

    aumentar=False
    NodoColocar=None
    Noaumentar=False

    def __init__(self):
        self.padre=None   

    def comprobarpadre(self):
        return self.padre!=None

    def insertarPadre(self,dato):
        global aumentar
        global NodoColocar
        if self.padre==None:
            self.padre=Nodo(dato)
        else: 
            if self.comparar(self.padre.dato) > self.comparar(dato):
                if self.padre.izquierda==None:
                    self.padre.izquierda=Nodo(dato)
                    self.padre.equilibrio-=1
                else:
                    self.insertar(dato,self.padre.izquierda)
                    if aumentar:
                        self.padre.equilibrio-=1
                        if self.padre.equilibrio<=-2 and self.padre.izquierda.equilibrio<0:
                            print("EqSimpleIzq")
                            temp=self.padre.izquierda

                            temp.equilibrio=0
                            self.padre.equilibrio=0

                            self.padre.izquierda=temp.derecha
                            temp.derecha=self.padre
                            self.padre=temp
                            aumentar=False

                        elif self.padre.equilibrio<-1:
                            print("EqDobleIzq")
                            temp1=self.padre.izquierda
                            temp2=self.padre.izquierda.derecha
                            n=temp2.equilibrio

                            temp1.derecha=temp2.izquierda
                            temp2.izquierda=temp1
                            self.padre.izquierda=temp2.derecha
                            temp2.derecha=self.padre
                            self.padre=temp2

                            if n==-1:
                                self.padre.derecha.equilibrio=1
                            else:
                                self.padre.derecha.equilibrio=0
                            pass
                            if n==1:
                                self.padre.izquierda.equilibrio=-1
                            else:
                                self.padre.izquierda.equilibrio=0
                            pass
                            self.padre.equilibrio=0

                            aumentar=False
                        pass
                    elif NodoColocar!=None:
                        self.padre.izquierda=NodoColocar
                        NodoColocar=None
                    pass
                pass
            else:
                if self.padre.derecha==None:
                    self.padre.derecha=Nodo(dato)
                    self.padre.equilibrio+=1
                else:
                    self.insertar(dato,self.padre.derecha)
                    if aumentar:
                        self.padre.equilibrio+=1
                        if self.padre.equilibrio>1 and self.padre.derecha.equilibrio>0:
                            print("EqSimpleDer")
                            temp=self.padre.derecha
                            temp.equilibrio=0
                            self.padre.equilibrio=0
                            self.padre.derecha=temp.izquierda
                            temp.izquierda=self.padre
                            self.padre=temp
                            aumentar=False

                        elif self.padre.equilibrio>1:
                            print("EqDobleDer")
                            temp1=self.padre.derecha
                            temp2=self.padre.derecha.izquierda
                            n=temp2.equilibrio

                            temp1.izquierda=temp2.derecha
                            temp2.derecha=temp1
                            self.padre.derecha=temp2.izquierda
                            temp2.izquierda=self.padre
                            self.padre=temp2

                            if n==-1:
                                self.padre.derecha.equilibrio=1
                            else:
                                self.padre.derecha.equilibrio=0
                            pass
                            if n==1:
                                self.padre.izquierda.equilibrio=-1
                            else:
                                self.padre.izquierda.equilibrio=0
                            pass
                            self.padre.equilibrio=0

                            aumentar=False
                        pass
                    elif NodoColocar!=None:
                        self.padre.derecha=NodoColocar
                        NodoColocar=None
                    pass
                pass
            pass
        pass
        aumentar=False

    def insertar(self,dato,nodoA):
        global aumentar
        global NodoColocar
        if self.comparar(nodoA.dato) > self.comparar(dato):
            if nodoA.izquierda==None:
                nodoA.izquierda=Nodo(dato)
                nodoA.equilibrio-=1
                if nodoA.derecha==None:
                    aumentar=True
                else:
                    NodoColocar=None
                pass
            else:
                self.insertar(dato,nodoA.izquierda)
                if aumentar:
                    nodoA.equilibrio-=1
                    if nodoA.equilibrio<-1 and nodoA.izquierda.equilibrio<0:
                        print("EqSimpleIzq2")
                        temp=nodoA.izquierda
                        temp.equilibrio=0
                        nodoA.equilibrio=0

                        nodoA.izquierda=temp.derecha
                        temp.derecha=nodoA
                        nodoA=temp
                        NodoColocar=nodoA
                        aumentar=False

                    elif nodoA.equilibrio<-1:
                        print("EqDobleIzq2")
                        temp1=nodoA.izquierda
                        temp2=nodoA.izquierda.derecha
                        n=temp2.equilibrio

                        temp1.derecha=temp2.izquierda
                        temp2.izquierda=temp1
                        nodoA.izquierda=temp2.derecha
                        temp2.derecha=nodoA
                        nodoA=temp2
                        
                        if n==-1:
                            nodoA.derecha.equilibrio=1
                        else:
                            nodoA.derecha.equilibrio=0
                        pass
                        if n==1:
                            nodoA.izquierda.equilibrio=-1
                        else:
                            nodoA.izquierda.equilibrio=0
                        pass
                        nodoA.equilibrio=0

                        NodoColocar=nodoA
                        aumentar=False
                    pass
                elif NodoColocar!=None:
                    nodoA.izquierda=NodoColocar
                    NodoColocar=None
                pass
            pass
        else:
            if nodoA.derecha==None:
                nodoA.derecha=Nodo(dato)
                nodoA.equilibrio+=1
                if nodoA.izquierda==None:
                    aumentar=True
                else:
                    NodoColocar=None
                pass
            else: 
                self.insertar(dato,nodoA.derecha)
                if aumentar:
                    nodoA.equilibrio+=1
                    if nodoA.equilibrio>1 and nodoA.derecha.equilibrio>0:
                        print("EqSimpleDer2")
                        temp=nodoA.derecha

                        temp.equilibrio=0
                        nodoA.equilibrio=0

                        nodoA.derecha=temp.izquierda
                        temp.izquierda=nodoA
                        nodoA=temp

                        NodoColocar=nodoA
                        aumentar=False

                    elif nodoA.equilibrio>1:
                        print("EqDobleDer2")
                        temp1=nodoA.derecha
                        temp2=nodoA.derecha.izquierda
                        n=temp2.equilibrio

                        temp1.izquierda=temp2.derecha
                        temp2.derecha=temp1
                        nodoA.derecha=temp2.izquierda
                        temp2.izquierda=nodoA
                        nodoA=temp2

                        if n==-1:
                            nodoA.derecha.equilibrio=1
                        else:
                            nodoA.derecha.equilibrio=0
                        pass
                        if n==1:
                            nodoA.izquierda.equilibrio=-1
                        else:
                            nodoA.izquierda.equilibrio=0
                        pass
                        nodoA.equilibrio=0

                        NodoColocar=nodoA
                        aumentar=False
                    pass
                elif NodoColocar!=None:
                    nodoA.derecha=NodoColocar
                    NodoColocar=None
                pass
            pass
        pass

    def comparar(self,dato):
        letra=dato[0].lower()
        switcher={
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'a': 10,
            'b': 11,
            'c': 12,
            'd': 13,
            'e': 14,
            'f': 15,
            'g': 16,
            'h': 17,
            'i': 18,
            'j': 19,
            'k': 20,
            'l': 21,
            'm': 22,
            'n': 23,
            'o': 24,
            'p': 25,
            'q': 26,
            'r': 27,
            's': 28,
            't': 29,
            'u': 30,
            'v': 31,
            'w': 32,
            'x': 33,
            'y': 34,
            'z': 35,
        }
        return switcher.get(letra,0)

    def EqSimpleIzq(self,Nodo1,Nodo2):
        Nodo1.izquierda=Nodo2.derecha
        Nodo2.derecha=Nodo1
        Nodo1=Nodo2

    def EqSimpleDer(self,Nodo1,Nodo2):
        Nodo1.derecha=Nodo2.izquierda
        Nodo2.izquierda=Nodo1
        Nodo1=Nodo2

    def EqDobleIzq(self,Nodo1,Nodo2,Nodo3):
        Nodo2.derecha=Nodo3.izquierda
        Nodo3.izquierda=Nodo2
        Nodo1.izquierda=Nodo3.derecha
        Nodo3.derecha=Nodo1
        Nodo1=Nodo3

    def EqDobleDer(self,Nodo1,Nodo2,Nodo3):
        Nodo2.izquierda=Nodo3.derecha
        Nodo3.derecha=Nodo2
        Nodo1.derecha=Nodo3.izquierda
        Nodo3.izquierda=Nodo1
        Nodo1=Nodo3

    def graficar1(self,nodo,f):
        if nodo.izquierda!=None:
            f.write(nodo.dato+"->"+nodo.izquierda.dato+"\n")
            self.graficar1(nodo.izquierda,f)
            pass
        if nodo.derecha!=None:
            f.write(nodo.dato+"->"+nodo.derecha.dato+"\n")
            self.graficar1(nodo.derecha,f) 
            pass

    def graficar2(self,nodo,f):
        f.write(nodo.dato+" [ label = \"{"+nodo.dato+"|"+str(nodo.equilibrio)+"}\"];\n")
        if nodo.izquierda!=None:
            self.graficar2(nodo.izquierda,f)
            pass
        if nodo.derecha!=None:
            self.graficar2(nodo.derecha,f)
            pass

    def graficar(self):
        f=open("arbol.dot","w")
        f.write("digraph pila{\n")
        f.write("node [shape=\"record\"];\n")
        f.write(self.padre.dato+" [ label = \"{"+self.padre.dato+"|"+str(self.padre.equilibrio)+"}\"];\n")
        if self.padre.izquierda!=None:
            self.graficar2(self.padre.izquierda,f)
            pass
        if self.padre.derecha!=None:
            self.graficar2(self.padre.derecha,f)
            pass
        if self.padre.izquierda!=None:
            f.write(self.padre.dato+"->"+self.padre.izquierda.dato+";\n")
            self.graficar1(self.padre.izquierda,f)
            pass
        if self.padre.derecha!=None:
            f.write(self.padre.dato+"->"+self.padre.derecha.dato+";\n")
            self.graficar1(self.padre.derecha,f)
            pass
        f.write("}")
        f.close()
        os.system("dot -Tjpg arbol.dot -o imagena.jpg")
        os.system("imagena.jpg")