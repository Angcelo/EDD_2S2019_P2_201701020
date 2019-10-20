import os

class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.izquierda=None
        self.derecha=None
        self.equilibrio=0

class Arbol():

    def __init__(self):
        self.padre=None   

    def comprobarpadre(self):
        return self.padre!=None

    def insertarPadre(self,dato):
        if self.padre==None:
            self.padre=Nodo(dato)
        else: 
            if self.comparar(self.padre.dato) > self.comparar(dato):
                if self.padre.izquierda==None:
                    self.padre.izquierda=Nodo(dato)
                    self.padre.equilibrio-=1
                else:
                    if self.insertar(dato,self.padre.izquierda):
                        self.padre.equilibrio-=1
                    pass
                pass
            else:
                if self.padre.derecha==None:
                    self.padre.derecha=Nodo(dato)
                    self.padre.equilibrio+=1
                else:
                    if self.insertar(dato,self.padre.derecha):
                        self.padre.equilibrio+=1
                    pass
                pass
            pass
        pass


    def insertar(self,dato,nodoA):
        if self.comparar(nodoA.dato) > self.comparar(dato):
            if nodoA.izquierda==None:
                nodoA.izquierda=Nodo(dato)
                nodoA.equilibrio-=1
                if nodoA.derecha==None:
                    return True
                pass
                return False
            else:
                if insertar(dato,nodoA.izquierda):
                    nodoA.equilibrio-=1
                    return True
                pass
                return False
            pass
        else:
            if nodoA.derecha==None:
                nodoA.derecha=Nodo(dato)
                nodoA.equilibrio+=1
                if nodoA.izquierda==None:
                    return True
                pass
                return False
            else: 
                if insertar(dato,nodoA.derecha):
                    nodoA.equilibrio-=1
                    return True
                pass
                return False
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
