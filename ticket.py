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
    
    
    def add(self, cliente, pagado, vendedor):
        """
        Agrega una linea de texto al ticket.
        """
        if not self.database.esta_id(cliente):
            return
        
        datos = self.database.consulta(cliente)
        deuda = datos[1]
        data = ",".join([cliente.lower(), str(deuda), str(pagado), time.strftime("%d/%m/%y"), vendedor])
        
        with open(self.nombre, "r+") as file:
            linea = file.readline()
            while linea:
                linea = file.readline()
            file.write(data + "\n")
    
    
    def remove(self,nombre):
		"""
        Borra la linea que contenga le nombre dentro del ticket,
        si aparace mas de una vez borra su ultima aparicion.
		"""
        lineas = []
        with open(self_nombre) as archivo:
            archivo_csv = csv.reader(archivo)
            for linea in archivo_csv:
                lineas.append(linea)

        contador = len(lineas) -1
        while contador >= 0:
            if lineas[contador][0].lower() == nombre.lower():
                lineas.pop(contador)
                break
            contador -=1

        with open(self_nombre,"w") as arch_escribir:
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
    
    
    def change(self, cliente, fecha, col, valor):
        """
        Cambia la primer linea con el nombre y fecha ingresada con 
        los valores ingresados.
        """
        
        ticket = self.get_all()
        for datos in ticket:
            if datos[0].lower() == cliente.lower() and datos[3] == fecha:
                datos[col] = str(valor)
        
        with open(self.nombre, "w") as file:
            for datos in ticket:
                file.write(",".join(datos) + "\n")
                
                
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
    
    
    def get_id(self, nombre):
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

