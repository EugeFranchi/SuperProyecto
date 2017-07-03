from archivo import ARCHIVO
from BD import BD
import time
import csv

class Ticket:
    
    def __init__(self, nombre):
        """
        Inicializa el Ticket.
        """

        self.database = BD(nombre)
        self.nombre = self.database.nombre
    
    
    def add(self, cliente, deuda, pagado, vendedor):
        """
        Agrega una linea de texto al ticket.
        """
        deuda = str(deuda)
        pagado = str(pagado)
        fecha = time.strftime("%d/%m/%y")
        
        with open(self.nombre,"r+") as file:
            linea = file.readline()
            while linea:
                linea = file.readline()
            file.write("{}\n".format(",".join([cliente, deuda, pagado, fecha, vendedor])))
    
    
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
        
        with open(self.nombre) as file:
            arch_csv = csv.reader(file)
            for linea in arch_csv:
                ultimo = linea
        
        return ultimo
    
    
    def consultar(self, nombre):
        """
        Devuelva los datos correspondientes al nombre.
        """
        cliente = []
        
        with open(self.nombre) as file:
            arch_csv = csv.reader(file)
            for datos in arch_csv:
                if datos[0].lower() == nombre.lower():
                    cliente.append(datos)
        
        return cliente
