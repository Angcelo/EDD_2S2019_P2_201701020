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

    def comprobar(self,dato):
        return dato=="+" or dato=="-" or dato=="*" or dato=="/"    

    def insertar(self,dato,nodoA):
        nuevo =Nodo(dato)
        if nodoA==None:
            nodoA=nuevo
        else 
            if self.comparar(padre.dato[0].lower())<self.comparar(nuevo.dato[0].lower()):
                self.insertar(dato,nodoA.izquierda)
            else
                self.insertar(dato,nodoA.derecha)
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
        print switcher.get(letra,0)
        return switcher.get(letra,0)