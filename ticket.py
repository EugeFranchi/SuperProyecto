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
