#Code by @masacr3
from os import path

class ARCHIVO:
	"Implement TDas CRUD"

	#init
	def __init__(self,nombre):
		self.nombre = nombre+".txt"

	#crud
	def create(self):
		if self.existe():
			return
		with open(self.nombre,"w") as nuevoarchivo:
			nuevoarchivo.write("")

	def delete(self):
		if self.existe():
			return
		os.remove(self.nombre)


	#check
	def existe(self):
		return path.exists(self.nombre)
