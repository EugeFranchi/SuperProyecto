import cmd
import csv
import os
from BD import BD
from nodo import *
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
        grid_resumen = GRIDRESUMEN()
        lista = self.resumen.select_all()
        for dato in lista:
            nombre,monto = dato
            cliente = CLIENTE(nombre)
            cliente.add(int(monto))
            grid_resumen.push(cliente)
        grid_resumen.show_resumen()
    
    
    def do_agregar(self, nombreYmontos):
        """
        Recibe un nombre y monto. Los agrega al resumen y su archivo la deuda.
        """
        nombre = nombreYmontos.split()
        montos = []
        while nombre[-1].isdigit():
            montos.append(int(nombre.pop(-1)))
        total_monto= 0

        nombre = " ".join(nombre)
        usuario_base = BD(nombre)
        
        for monto in montos[::-1]:
                total_monto +=monto
                fecha = time.strftime("%d/%m/%y")
                usuario_base.add([monto,fecha,self.vendedor])
        
        if not usuario_base.esta_id(nombre):
            self.resumen.add([nombre,total_monto])
        else:
            self.resumen.update(nombre,[1],[total_monto])
    
    
    def do_quitar(self, parametros):
        """
        Recibe un nombre y elimina du deuda de los archivos.
        """
        parametros = parametros.split(" ")
        if len(parametros) != 2:
            print("Cantidad de valores ingresador invalida.")
            return
        
        nombre, monto = parametros
        
        if not str(monto).isdigit():
            print("El monto ingresado no es valido.".format(self.vendedor))
            return
        
        monto = int(monto)
        
        #Se asegura que el cliente tenga deudas
        if not self.resumen.esta_id(nombre):
            print( nombre + " no tiene deudas.")
            return
        
        cliente = CLIENTE(nombre)
        arch_cliente = BD(nombre)
        nombre, deuda = self.resumen.consulta(nombre)
        saldo = int(deuda) - monto
        fecha = time.strftime("%d/%m/%y")
        
        #En caso que pague toda la deuda
        if int(deuda) == monto:
            self.resumen.remove(nombre)
            arch_cliente.database.delete()
        
        #En caso que pague parte de ella
        else:
            self.resumen.update(nombre, [1], [saldo])
            arch_cliente.add([-monto,fecha,self.vendedor])
        
        #Agrego a ticket
        self.ticket.add(cliente,deuda,monto,self.vendedor)
        
        print("Se han eliminado $" + str(monto) + " de la deuda de " + nombre)
    
    
    def do_mostrar(self,nombre):
        """
        Recibe un nombre y muestra en detalle la deuda del cliente.
        """
        if not self.resumen.esta_id(nombre):
            print("{} no tiene deudas.".format(nombre))
            return
        arch_cliente = BD(nombre)
        grid_cliente = GRIDCLIENTE(nombre)
        lineas = arch_cliente.select_all()
        for datos in lineas:
            cantidad,fecha,vendedor = datos
            dato_fiado = DATO_FIADO(cantidad,fecha,vendedor)
            grid_cliente.agregar(dato_fiado)
        grid_cliente.mostrar()
    
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
