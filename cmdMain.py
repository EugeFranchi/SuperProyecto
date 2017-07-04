import cmd
import csv
import os
from BD import BD
from nodo import CLIENTE
from ticket import Ticket

class Shell(cmd.Cmd):
    intro = 'Bienvenido a mi programa.\nIngrese help o ? para listar los comandos.\n'
    prompt = '--> '
    doc_header="Comandos:"
    
    
    def abrir(self):
        """
        Inicia el programa.
        """
        self.resumen = BD("resumen")
        self.ticket = Ticket("tickets")
        vendedor = input("Ingrese su nombre: ")
        while not vendedor:
            vendedor = input("Ingrese su nombre: ")
        self.vendedor = vendedor
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
        nombre, monto = nombreYmonto.split()[0],nombreYmonto.split()[-1]
        if not monto.isdigit():
            print("El monto ingresado no es valido, {} ;)".format(self.vendedor))
            return
        #Crea archivo y si no exciste lo crea
        archivo_cliente = ARCHIVO(nombre)
        if not archivo_cliente.existe():
            archivo_cliente.create()
            self.resumen.add(nombre, int(monto))
        else:
            cliente,deuda_vieja = self.resumen.consulta(nombre)
            deuda_total = int(deuda_vieja) + int(monto)
            self.resumen.update(nombre,[1],[deuda_total])
            
        fecha = time.strftime("%d/%m/%y")
        #agrega lineas al final de archivo
        with open(archivo_cliente.nombre,"a") as archivo:
            archivo.write("{},{},{}\n".format(monto,fecha,self.vendedor))
            
        print("Se han agregado ${} de deuda a {}.".format(monto,nombre))
    
    
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
        
        if not monto.isdigit():
            print("El monto ingresado no es valido.".format(self.vendedor))
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
        
        print("Se han eliminado $" + str(monto) + " de la deuda de " + nombre)
    
    
    def do_mostrar(self,nombre):
        """
        Recibe un nombre y muestra en detalle la deuda del cliente.
        """
        if not self.resumen.esta_id(nombre):
            print( str(nombre) + " no tiene deudas.")
            return
        
        arch_cliente = ARCHIVO(nombre)
        with open(arch_cliente.nombre) as file:
            for linea in file:
                print(linea.rstrip())
        
        nombre,deuda = self.resumen.consulta(nombre)
        print("Deuda total: " + str(deuda))
    
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
