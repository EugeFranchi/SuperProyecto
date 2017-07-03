import cmd
import csv
import os
from BaseDeDatos import BaseDeDatos
from nodo import CLIENTE
from ticket import Ticket

class Shell(cmd.Cmd):
    intro = 'Bienvenido a mi programa.\nIngrese help o ? para listar los comandos.\n'
    prompt = '--> '
    
    
    def abrir(self):
        """
        Inicia el programa.
        """
        self.resumen = BaseDeDatos("resumen")
        self.ticket = Ticket("tickets")
        self.cmdloop()
    
    
    def do_resumen(self, parametros):
        """
        Imprime el resumen.
        """
        deudas = self.database.get_all()
        for deuda in deudas:
            print("{}: {}".format(deuda[0], deuda[1]))
    
    
    def do_agregar(self, nombreYmonto):
        """
        Recibe un nombre y monto. Los agrega al resumen y su archivo la deuda.
        """
        nombre, monto = nombreYmonto.split(" ")
        
        
        
        print("Se han agregado $" + str(monto) + " de deuda a " + nombre + ".")
    
    
    def do_quitar(self, nombreYmonto):
        """
        Recibe un nombre y elimina du deuda de los archivos.
        """
        nombre, monto = nombreYmonto.split(" ")
        
        
        
        print("Se han eliminado $" + str(monto) + " de la deuda de " + nombre)
    
    
    def do_mostrar(self,nombre):
        """
        Recibe un nombre y muestra en detalle la deuda del cliente.
        """
        
        

    
    
    def do_imprimir(self,parametros):
        """
        Imprime el ticket.
        """
    
    
    def do_salir(self,parametros):
        """
        Sale del programa.
        """
        return True

    
    def emptyline(self):
        """
        Deja la flecha limpia.
        """
        return None

Shell().abrir()    
