from archivo import ARCHIVO
from BD import BD
import time
import csv

class Ticket:
    
    def __init__(self, nombre, database):
        """
        Inicializa el Ticket.
        """
        self.archivo = ARCHIVO(nombre)
        self.archivo.create()
        self.nombre = self.archivo.nombre
        self.database = BD(database)
    
    
    def add(self, cliente, col, pagado, vendedor):
        """
        Agrega una linea de texto al ticket.
        """
        
        datos = self.database.consulta(cliente)
        deuda = datos[int(col)]
        data = ",".join([cliente.lower(), str(deuda), str(pagado), time.strftime("%d/%m/%y"), vendedor])
        
        with open(self.nombre, "r+") as file:
            linea = file.readline()
            while linea:
                linea = file.readline()
            file.write(data + "\n")
            
            
    def remove(self,nombre):
	"""
        Borra la linea que contenga dentro del ticket.
	"""

	lineas = []
	with open(self.nombre) as archivo:
		archivo_csv = csv.reader(archivo)
		for linea in archivo_csv:
			if linea[0] != nombre:
				lineas.append(archivo_csv)

	with open(self.nombre,"w") as arch_escribir:
		for linea in lineas:
			arch_escribir.write("{}\n".format(",".join(linea)))
    
    
    def get_all(self):
        """
        Devuelve una lista con las lineas del archivo.
        """
        
        ticket = []
        
        with open(self.nombre) as file:
            arch_csv = csv.reader(file)
            for linea in arch_csv:
                ticket.append(linea)
        
        return ticket

	def get_ultimo(self):
		"""
		Devuelve la ultima linea del archivo en una lista.
		"""
		ultimo = []
		with open(self.nombre) as archivo:
			archivo_csv = csv.reader(archivo)
			ultimo = archivo_scv[-1]
		return ultimo
