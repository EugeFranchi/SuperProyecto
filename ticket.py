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
