import csv
import time
import os
from os import path

class BaseDeDatos:
    
    ###INITS
    def __init__(self):
        self.create_resumen()
        self.resumen = "resumen.txt"
    
    def create_resumen(self):
        """
        En caso de no existir el archivo "resumen.txt", lo crea.
        """
        if not path.exists("resumen.txt"):
            with open("resumen.txt","w") as resumen:
                resumen.write("")
    
    def create_cliente(self, nombre):
        """
        En caso de que un cliente no esté registrado, lo inicializa.
        """
        if self.is_cliente(nombre):
            return
        
        nombres = nombre.lower().split(" ")
        nombre_arch = "".join(nombres)
        
        with open(nombre_arch + ".txt", "w") as file:
            file.write("{},{}".format("0",time.strftime("%d/%m/%y" + "\n")))
        with open(self.resumen, "r+") as resumen:
            linea = resumen.readline()
            while linea:
                linea = resumen.readline()
            resumen.write("{},{}".format(nombre, "0" + "\n"))

    ###CRUD
    
    
    def change(self, lista, nombre_arch, monto):
        """
        Modifica el resumen y el archivo del cliente.
        """
        self.change_resumen(lista)
        self.change_ArchCliente(nombre_arch, monto)


    def change_resumen(self, lista):
        """
        Sobre escribe el resumen con la lista.
        """
        try:
            with open(self.resumen, "w") as resum:
                for elem in lista:
                    resum.write("{},{}".format(elem[0], elem[1] + "\n"))
        
        except ValueError:
            print("Error rescribiendo resumen.")
    
    
    def change_ArchCliente(self, archivo, submonto):
        """
        Agrega la deuda al archivo del cliente.
        """
        try:
            with open(archivo + ".txt", "r+") as file:
                linea = file.readline()
                while linea:
                    linea = file.readline()
                file.write("{},{}".format(submonto, time.strftime("%d/%m/%y") + "\n"))
        
        except FileNotFoundError:
            print("Carpeta de cliente no encontrada")    
    
    
    def add(self, nombre, submonto):
        """
        Recibe el nombre de un cliente y el monto de su deuda. Agrega estos
        a los archivos correspondientes.
        """
        self.create_cliente(nombre)
        nombre_arch = self.get_nombreArchivo(nombre)
        
        try:
            nueva = self.get_listaResumen(nombre,submonto)
        
            self.change(nueva, nombre_arch, submonto)
        
        except ValueError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)

    
    
    def remove(self, nombre, submonto):
        """
        Recibe el nombre del cliente y un submonto. En caso de que el 
        monto cubra la deuda, se elimina el archivo del cliente y su
        registro en el resumen. De lo contrario, se disminuye la deuda
        registrada.
        """
        if not self.is_cliente(nombre):
            print("{} no tiene deudas.".format(nombre))
        
        with open(self.resumen, "r+") as resumen:
            arch_csv = csv.reader(resumen)
            for cliente,monto in arch_csv:
                if cliente.lower() == nombre.lower():
                    if int(monto) == submonto:
                        self.remove_deudaTotal(nombre, submonto)
                    else:
                        self.remove_deudaParcial(nombre,submonto)
                    return
    
    
    def remove_deudaTotal(self, nombre, submonto):
        """
        Recibe el nombre de un cliente y elimina su deuda.
        """
        
        nombre_arch = self.get_nombreArchivo(nombre)
        os.remove(nombre_arch + ".txt")
        
        nueva = self.get_listaResumen(nombre, -submonto)
        
        self.change_resumen(nueva)
    
    
    def remove_deudaParcial(self,nombre,cantidad):
        """Recibe el nombre del cliente y la cantidad pagada por el cliente.
        Modifica el archivo 'resumen.txt' con la nueva cantidad que debe y 
        su respectivo archivo.
        """
        
        nuevos_montos = self.get_listaResumen(nombre,-cantidad)
        nombre_archivo = self.get_nombreArchivo(nombre)
        self.change(nuevos_montos, nombre_archivo, -cantidad)
    
    ###CHECK
    
    
    def is_cliente(self, nombre):
        """
        Recibe el nombre del cliente y devuelve si se encuentra en el resumen.
        """
        nombre = nombre.lower()
        
        try:
            with open(self.resumen) as file:
                archivo_csv = csv.reader(file)
                for cliente,monto in archivo_csv:
                    if cliente.lower() == nombre:
                        return True
                return False
        
        except ValueError:
            print("Error en el resumen.")
    
    ###GET
    
    
    def get_deudas(self, nombre):
        """
        Imprime en detalle la deuda del cliente por pantalla.
        """
        if not self.is_cliente(nombre):
            print(nombre + " no tiene deudas.")
            return
        
        try:
            nombre_arch = self.get_nombreArchivo(nombre)
            with open(nombre_arch + ".txt") as file:
                arch_csv = csv.reader(file)
                for monto,fecha in arch_csv:
                    print("{} - {}".format(fecha, monto))
        
        except FileNotFoundError:
            print("El cliente no posee archivo de deudas personal.")
        except IOError:
            print("Error en el archivo del cliente.")
    
    
    def get_listaResumen(self, nombre, submonto):
        """
        Recibe el nombre del cliente al q se desea agregar un monto en el
        archivo resumen. Si se desea agregar una deuda, signo del submonto
        debe ser positivo. En caso contrario, debe ser negativo.
        """
        nueva = []
        
        try:
            with open(self.resumen) as resumen:
                archivo_csv = csv.reader(resumen)
                for datos in archivo_csv:
                    if nombre.lower() == datos[0].lower():
                        datos[1] = str(int(datos[1]) + int(submonto))
                    if int(datos[1]) == 0:
                        continue
                    nueva.append(datos)
            return nueva
        
        except ValueError:
            print("Error en el resumen.")
    
    
    def get_nombreArchivo(self, nombre):
        """
        Recibe un nombre y devuelve el nombre del archivo correspondiente.
        """
        nombres = nombre.lower().split(" ")
        nombre_arch = "".join(nombres)
        return nombre_arch

