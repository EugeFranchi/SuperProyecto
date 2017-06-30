def cargar_datos_cliente(self,nombre):
        """Carga los datos del cliente al objeto grid. """
        if self.existe(nombre):
            grid = GRID()
            nombres = nombre.lower().split(" ")
            nombre_archivo = "".join(nombres)
            with open("{}.txt".format(nombre_archivo)) as archivo:
                archivo_csv = csv.reader(archivo)
                cliente = CLIENTE(nombre)
                for datos in archivo_csv:
                    cliente.add(int(datos[0]))
                grid.push(cliente)
            return grid
        else:
            raise ValueError("El nombre no exsiste")