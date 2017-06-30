def pagar_deuda_parcial(self,nombre,cantidad):
    """Resibe el nombre del cliente y la cantidad pagada por el cliente. modifica el archivo 'resumen.txt' con la nueva cantidad que debe"""
    if not existe(nombre):
        raise ValueError("el nombre no existe")
    nuevos_montos = self.resumen_a_lista(nombre,-cantidad)
    self.lista_a_resumen(nuevos_montos)
    nombre_archivo = self.nombre_archivo_cliente(nombre)
    self.deuda_a_cliente(nombre_archivo,-cantidad)