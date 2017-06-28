# SuperProyecto
Mega genial proyecto hiper fabuloso

import csv
import time
from os import path

class BaseDeDatos:
    
    def __init__(self):
        self.crear_resumen()
        self.resumen = "resumen.txt"


    def crear_resumen(self):
        """
        En caso de no existir el archivo "resumen.txt", lo crea.
        """
        if not path.exists("resumen.txt"):
            with open("resumen.txt","w") as resumen:
                resumen.write("")


    def existe(self, nombre):
        """
        Recibe el nombre del cliente y devuelve si se encuentra en el resumen.
        """
        nombre = nombre.lower()
        with open(self.resumen) as file:
            archivo_csv = csv.reader(file)
            for cliente,monto in archivo_csv:
                if cliente.lower() == nombre:
                    return True
            return False


    def crear_cliente(self, nombre):
        """
        En caso de que un cliente no esté registrado, lo inicializa.
        """
        if self.existe(nombre):
            return
        else:
            with open(nombre + ".txt", "w") as file:
                archivo_csv = csv.writer(file)
                archivo_csv.writerow([0,time.strftime("%d/%m/%y")])
            with open(self.resumen, "r+") as resumen:
                linea = resumen.readline()
                while linea:
                    linea = resumen.readline()
                resumen.write("{},{}".format("\n" + nombre, 0))
