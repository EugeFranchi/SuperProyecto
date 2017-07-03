import cmd
import csv
import os
from BD import BD
from nodo import CLIENTE
from ticket import Ticket

class Shell(cmd.Cmd):
    intro = 'Bienvenido a mi programa.\nIngrese help o ? para listar los comandos.\n'
    prompt = '--> '
    
    
    def abrir(self):
        """
        Inicia el programa.
        """
        self.resumen = BD("resumen")
        self.ticket = Ticket("tickets")
        self.cmdloop()
    
    
    def do_resumen(self, parametros):
        """
        Imprime el resumen.
        """
        deudas = self.resumen.select_all()
        for deuda in deudas:
            print("{}: {}".format(deuda[0], deuda[1]))
    
    
    def do_agregar(self, nombreYmonto):
        """
        Recibe un nombre y monto. Los agrega al resumen y su archivo la deuda.
        """
        nombre, monto = nombreYmonto.split(" ")
        
        
        
        print("Se han agregado $" + str(monto) + " de deuda a " + nombre + ".")
    
    
    def do_quitar(self, parametros):
        """
        Recibe un nombre y elimina du deuda de los archivos.
        """
        nombre, monto, vendedor = parametros.split(" ")
        monto = int(monto)
        
        #Se asegura que el cliente tenga deudas
        if not self.resumen.esta_id(nombre):
            print( nombre + " no tiene deudas.")
            return
        
        cliente = CLIENTE(nombre)
        arch_cliente = ARCHIVO(nombre)
        nombre, deuda = self.resumen.consulta(nombre)
        saldo = int(deuda) - monto
        fecha = time.strftime("%d/%m/%y")
        
        #En caso que pague toda la deuda
        if int(deuda) == monto:
            self.resumen.remove(nombre)
            arch_cliente.delete()
        
        #En caso que pague parte de ella
        else:
            self.resumen.update(nombre, [1], saldo)
            with open(arch_cliente.nombre) as file:
                linea = file.readline()
                while linea:
                    linea = file.readline()
                file.writerow("{},{},{}\n".format(-monto,fecha,vendedor))
        
        #Agrego a ticket
        self.ticket.add(cliente,deuda,monto,vendedor)
    
    
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
