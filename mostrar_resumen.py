def cargar_al_grid(self):
        """Carga los datos del archivo 'resumen.txt' al objeto grid."""
        grid = GRID()
        with open(self.resumen) as resumen:
            archivo = csv.reader(resumen)
            for datos in archivo:
                cliente = CLIENTE(datos[0])
                cliente.add(int(datos[1]))
                grind.push(cliente)
        return grid