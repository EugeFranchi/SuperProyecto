import cmd
import csv
import os
from BD import *
from nodo import *
from ticket import *

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
    
    def _pedir_monto(self,cliente):
        """Pide montos al usuario hasta que no joda mas."""
        #verficar que sea entero
        monto = input("ingrese un monto o precione enter para dejar de agregar: ")
        if monto == "":
            return cliente
        if not self._verificar_valor(monto):
            print("Monto no valido...")
            return self._pedir_monto(cliente)
        cliente.add(float(monto))
        return self._pedir_monto(cliente)

    def _verificar_pasado(self,cliente):
        """Muestra al usuario el contenido de cliente y permite modificarlo si es incorrecto."""
        grid_aux = GRIDRESUMEN()
        grid_aux.push(cliente)
        grid_aux.show_datos_cliente()
        respuesta = input("¿Los datos ingresados son validos?: ")
        if respuesta != "si":
            if respuesta != "no":
                print("respuesta no valida...")
                return self._verificar_pasado(cliente)
            nueva_posicion = input("¿que valor desea cambiar,indique su posicion?: ")
            nuevo_monto = input("Ingrese el nuevo valor que debe contener: ")
            if not self._verificar_valor(nuevo_monto):
                print("Monto no valido...")
                return self._verificar_pasado(cliente)
            cliente.change(int(nueva_posicion) -1,float(nuevo_monto))
            return self._verificar_pasado(cliente)
        return cliente

    def _verificar_valor(self,monto):
        """Verifica si el parametro pasado es digito ya sea entero o flotante,devuelve un boleano."""
        for caracter in monto:
                if not caracter.isdigit() and caracter != ".":
                    return False
        return True
    
    
    def do_resumen(self, parametros):
        """
        Imprime el resumen.
        """
        grid_resumen = GRIDRESUMEN()
        lista = self.resumen.select_all()
        for dato in lista:
            nombre,monto = dato
            cliente = CLIENTE(nombre)
            cliente.add(float(monto))
            grid_resumen.push(cliente)
        grid_resumen.show_resumen()
    
    
    def do_agregar(self, nombre):
        """
        Recibe un nombre y monto. Los agrega al resumen y su archivo la deuda.
        """
        cliente = CLIENTE(nombre)
        cliente = self._pedir_monto(cliente)
        self._verificar_pasado(cliente)
        
        arch_cliente = BD(nombre)        
        total_monto = 0
        for monto in cliente.montos:
            total_monto +=monto
            fecha = time.strftime("%d/%m/%y")
            arch_cliente.add([monto,fecha,self.vendedor])
        
        if not arch_cliente.esta_id(nombre):
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
    
    def do_imprimir1(self, parametros):
        """
        Imprime toda aparicion de un cliente en ticket.
        """
        nombre = parametros.lower()
        grid_ticket = GRIDTICKET()
        lista = self.ticket.get_all()
        for dato in lista:
            cliente, deuda, pagado, fecha, vendedor = dato
            if cliente == nombre:
                datos = DATOTICKET( nombre, deuda, pagado, fecha, vendedor)
                grid_ticket.agregar(datos)
        grid_ticket.mostrar()
    
    def do_imprimir2(self, parametros):
        """
        Imprime la ultima aparicion del cliente en ticket.
        """
        nombre = parametros.lower()
        grid_ticket = GRIDTICKET()
        lista = self.ticket.get_all()
        for dato in lista:
            cliente, deuda, pagado, fecha, vendedor = dato
            if cliente == nombre:
                ultimo = DATOTICKET( nombre, deuda, pagado, fecha, vendedor)
        grid_ticket.agregar(ultimo)
        grid_ticket.mostrar()
    
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
