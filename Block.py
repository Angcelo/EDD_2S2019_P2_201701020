import os
import Arbo
import json
import time
import hashlib
import binascii

class NodoDoble:  
    def __init__(self, Index,Timestap,clase,data,previusHash,Hash):
       	self.Index=Index
       	self.Time=Timestap
       	self.Clase=clase
       	self.Data=data
       	self.PHash=previusHash
       	self.Hash=Hash

class ListaDoble:
	"""docstring for ClassName"""
	def __init__(self):
		self.primero=None
		self.ultimo=None
		self.indice=0

	def estaVacia(self):
		return self.primero==None

	def insertar_final(self,nombre,dataJson):
		data=Arbo.Arbol()
		#data.insertarJson(dataJson)
		self.indice = self.indice+1
		if self.estaVacia():
			time_string = time.strftime("%d/%m/%Y;%H:%M"+":00")
			st = str(self.indice)+time_string+nombre+dataJson+"0000"
			var=str.encode(st)
			m = hashlib.sha256()
			m.update(var)
			hasha=m.hexdigest()
			print(hasha)
			nuevo=NodoDoble(self.indice,time.strftime("%d/%m/%y")+" "+time.strftime("%X"),nombre,data,"0000",hasha)
			self.primero=nuevo
			self.ultimo=nuevo
		pass

	