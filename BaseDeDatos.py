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
        
        nombres = nombre.lower().split(" ")
        nombre_arch = "".join(nombres)
        
        with open(nombre_arch + ".txt", "w") as file:
            archivo_csv = csv.writer(file)
            archivo_csv.writerow([0,time.strftime("%d/%m/%y")])
        with open(self.resumen, "r+") as resumen:
            linea = resumen.readline()
            while linea:
                linea = resumen.readline()
            resumen.write("{},{}".format(nombre, "0" + "\n"))
    
    
    def get_montototal(self, nombre):
        """
        Recibe un nombre y devuelve el monto total de su deuda.
        """
        with open(self.resumen) as resumen:
            archivo_csv = csv.reader(resumen)
            for cliente,monto in archivo_csv:
                if cliente.lower() == nombre.lower():
                    return int(monto)
            return 0    
    
    def agregar_deuda(self, nombre, monto):
        """
        Recibe el nombre de un cliente y el monto de su deuda. Agrega estos
        a los archivos correspondientes.
        """
        self.crear_cliente(nombre)
        nueva = []
        nombres = nombre.lower().split(" ")
        nombre_arch = "".join(nombres)
        
        #guardo los datos de los clientes
        with open(self.resumen) as resumen:
            archivo_csv = csv.reader(resumen)
            for datos in archivo_csv:
                if nombre.lower() == datos[0].lower():
                    datos[1] = str(int(datos[1]) + monto)
                nueva.append(datos)
        
        #sobreescribo el resumen
        with open(self.resumen, "w") as resum:
            for elem in nueva:
                resum.write("{},{}".format(elem[0], elem[1] + "\n"))
        
        #modifico el archivo del cliente
        with open(nombre_arch + ".txt", "r+") as file:
            linea = file.readline()
            while linea:
                linea = file.readline()
            file.write("{},{}".format(monto, time.strftime("%d/%m/%y") + "\n"))