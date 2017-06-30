import cmd
import csv
import os
from os import path

class Shell(cmd.Cmd):
    intro = 'Bienvenido a mi programa.\nIngrese help o ? para listar los comandos.\n'
    prompt = '--> '
    
    
    def abrir(self):
        """
        Inicia el programa.
        """
        system('cls')
        self.cmdloop()
    
    
    def do_resumen(self, parametros):
        """
        Imprime el resumen.
        """
        with open("resumen.txt") as f:
            arch_csv = csv.reader(f)
            for cliente,monto in arch_csv:
                print("{}: {}".format(cliente, monto))
        self.do_clear("p")
    
    
    def do_agregar(self, nombre, monto):
        """
        Recibe un nombre y monto. Los agrega al resumen y su archivo la deuda.
        """
    
    
    def do_quitar(self, nombre):
        """
        Recibe un nombre y elimina du deuda de los archivos.
        """
    
    
    def do_mostrar(self,nombre):
        """
        Recibe un nombre y muestra en detalle la deuda del cliente.
        """
    
    
    def do_leoPuto(self,parametros):
        """
        Prueba si leo esta leyendo lo q hago.. e.e
        """
    
    
    def do_salir(self,parametros):
        """
        Sale del programa.
        """
        system('cls')
        return True

    
    def emptyline(self):
        """
        Deja la flecha limpia.
        """
        return None

Shell().abrir() 
