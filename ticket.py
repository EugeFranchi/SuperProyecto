from archivo import ARCHIVO
from BD import BD
import time
import csv
from nodo import CLIENTE

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
        
        self.database.add([cliente.nombre,deuda,pagado,fecha,vendedor])
    
    
    def get_all(self):
        """
        Devuelve una lista con las lineas del archivo.
        """
 
        return self.database.select_all()
    
    
    def get_ultimo(self, cliente):
        """
        Devuelve la ultima linea del archivo en una lista.
        """
        
        
        return self.consultar(cliente.nombre)[-1]
    
    
    def consultar(self, nombre):
        """
        Devuelva los datos correspondientes al nombre.
        """
        pagos = []
        
        with open(self.nombre) as file:
            arch_csv = csv.reader(file)
            for datos in arch_csv:
                if datos[0].lower() == nombre.lower():
                    pagos.append(datos)
        
        return pagos
