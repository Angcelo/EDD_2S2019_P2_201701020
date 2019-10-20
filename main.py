import Block
import os

bloque=Block.ListaDoble()
continuar=True
while continuar:	
	print("Para insertar Bloque------1")
	print("Seleccionar Bloque--------2")
	print("Reportes------------------3")
	entrada=input('Escoge un numero')
	os.system("CLS")
	if entrada=="1":
		entrada=input("Nombre de archivo \n")
		f=open(entrada)
		valor=f.read()
		valores=valor.split("\n",1)
		for elements in valores:
			datos=elements.split(",",1)
		pass
		bloque.insertar_final(datos[0],datos[1])
	elif entrada=="2":
		print("2")
	elif entrada=="3":
		print("3")
	else:
		continuar=False
	pass


