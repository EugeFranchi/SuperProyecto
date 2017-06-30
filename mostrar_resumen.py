def cargar_al_grid(self):
        """Carga los datos del archivo 'resumen.txt' al objeto grid."""
        grid = GRID()
        with open(self.resumen) as resumen:
            archivo = csv.reader(resumen)
            for datos in archivo:
                nombre,monto = datos
                cliente = CLIENTE(nombre)
                cliente.add(int(total))
                grid.push(cliente)
        return grid
