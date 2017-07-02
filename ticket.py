from archivo import ARCHIVO
import time

class Ticket:
    
    def __init__(self, nombre):
        """
        Inicializa el Ticket.
        """
        self.archivo = ARCHIVO(nombre)
        self.archivo.create()
        self.nombre = self.archivo.nombre
