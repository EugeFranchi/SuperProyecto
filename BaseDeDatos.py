import csv
import time
import os
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
    
    
    
    def resumen_a_lista(self, nombre, submonto):
        """
        Recibe el nombre del cliente al q se desea agregar un monto en el
        archivo resumen. Si se desea agregar una deuda, signo del submonto
        debe ser positivo. En caso contrario, debe ser negativo.
        """
        nueva = []
        with open(self.resumen) as resumen:
            archivo_csv = csv.reader(resumen)
            for datos in archivo_csv:
                if nombre.lower() == datos[0].lower():
                    datos[1] = str(int(datos[1]) + submonto)
                if int(datos[1]) == 0:
                    continue
                nueva.append(datos)
        return nueva
    
    
    def lista_a_resumen(self, lista):
        """
        Sobre escribe el resumen con la lista.
        """
        with open(self.resumen, "w") as resum:
            for elem in lista:
                resum.write("{},{}".format(elem[0], elem[1] + "\n"))
    
    
    def deuda_a_cliente(self, archivo, submonto):
        """
        Agrega la deuda al archivo del cliente.
        """
        with open(archivo + ".txt", "r+") as file:
            linea = file.readline()
            while linea:
                linea = file.readline()
            file.write("{},{}".format(submonto, time.strftime("%d/%m/%y") + "\n"))
    
    
    def nombre_archivo_cliente(self, nombre):
        """
        Recibe un nombre y devuelve el nombre del archivo correspondiente.
        """
        nombres = nombre.lower().split(" ")
        nombre_arch = "".join(nombres)
        return nombre_arch
    
    
    def agregar_deuda(self, nombre, submonto):
        """
        Recibe el nombre de un cliente y el monto de su deuda. Agrega estos
        a los archivos correspondientes.
        """
        self.crear_cliente(nombre)
        nombre_arch = self.nombre_archivo_cliente(nombre)
        
        nueva = self.resumen_a_lista(nombre,submonto)
        
        self.lista_a_resumen(nueva)
        
        self.deuda_a_cliente(nombre_arch, submonto)
    
    
    def sacar_deuda_total(self, nombre, submonto):
        """
        Recibe el nombre de un cliente y elimina su deuda.
        """
        
        nombre_arch = self.nombre_archivo_cliente(nombre)
        os.remove(nombre_arch + ".txt")
        
        nueva = self.resumen_a_lista(nombre, -submonto)
        
        self.lista_a_resumen(nueva)


    def pagar_deuda_parcial(self,nombre,cantidad):
        """Recibe el nombre del cliente y la cantidad pagada por el cliente.
        Modifica el archivo 'resumen.txt' con la nueva cantidad que debe y 
        su respectivo archivo.
        """
        
        nuevos_montos = self.resumen_a_lista(nombre,-cantidad)
        self.lista_a_resumen(nuevos_montos)
        nombre_archivo = self.nombre_archivo_cliente(nombre)
        self.deuda_a_cliente(nombre_archivo,-cantidad)


    def sacar_deuda(self, nombre, submonto):
        """
        Recibe el nombre del cliente y un submonto. En caso de que el 
        monto cubra la deuda, se elimina el archivo del cliente y su
        registro en el resumen. De lo contrario, se disminuye la deuda
        registrada.
        """
        if not self.existe(nombre):
            print("{} no tiene deudas.".format(nombre))
        
        with open(self.resumen, "r+") as resumen:
            arch_csv = csv.reader(resumen)
            for cliente,monto in arch_csv:
                if cliente.lower() == nombre.lower():
                    if int(monto) == submonto:
                        self.sacar_deuda_total(nombre, submonto)
                    else:
                        self.pagar_deuda_parcial(nombre,submonto)
                    return
