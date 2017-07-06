    def _pedir_monto(self,cliente):
        """
        Pide montos al usuario hasta que no joda mas.
        """
        #verficar que sea entero
        monto = input("Monto: ")
        if monto == "":
            return cliente
        monto = self._verificar_valor(monto)
        cliente.add(float(monto))
        return self._pedir_monto(cliente)


    def _verificar_pasado(self,cliente):
        """
        Muestra al usuario el contenido de cliente y 
        permite modificarlo si es incorrecto.
        """
        rtas_validas = [ "si", "no", "*"]
        grid_aux = GRIDRESUMEN()
        grid_aux.push(cliente)
        grid_aux.show_datos_cliente()
        respuesta = input("¿Los datos ingresados son validos? ('*' para cancelar): ")
        
        if respuesta.lower() == "si":
            return
            
        if respuesta.lower() == "*":
            return -1
            
        if respuesta.lower() == "no":
            nueva_posicion = input("Posición a cambiar: ")
            while not nueva_posicion.isdigit():
                nueva_posicion = input("Posicion invalida. Vuelva a intentarlo: ")
            nuevo_monto = input("Nuevo monto: ")
            nuevo_monto = self._verificar_valor(nuevo_monto)
            
            cliente.change(int(nueva_posicion) -1,float(nuevo_monto))
            return self._verificar_pasado(cliente)
        
        else:
            print("Respuesta no valida.")
            return self._verificar_pasado(cliente)


    def _verificar_valor(self,monto):
        """
        Verifica si el parametro pasado es digito ya sea entero o 
        flotante. Devuelve el monto correcto.
        """
        for caracter in monto:
                if not caracter.isdigit() and caracter != ".":
                    nuevo = input("Monto invalido. Vuelva a intentarlo: ")
                    return self._verificar_valor(nuevo)
        return monto
    
    
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
        print("Ingrese los montos (enter para terminar)")
        cliente = self._pedir_monto(cliente)
        rta=self._verificar_pasado(cliente)
        if rta == -1:
            return
        
        arch_cliente = BD(nombre.lower())        
        total_monto = 0
        for monto in cliente.montos:
            total_monto +=monto
            fecha = time.strftime("%d/%m/%y")
            arch_cliente.add([monto,fecha,self.vendedor])
        
        if not self.resumen.esta_id(nombre):
            self.resumen.add([nombre.lower(),total_monto])
        
        else:
            nombre, deuda = self.resumen.consulta(cliente.nombre)
            self.resumen.update(nombre.lower(),[1],[float(deuda) + total_monto])
