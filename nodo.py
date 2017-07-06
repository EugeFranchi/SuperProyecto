#Code by @masacr3
class CLIENTE:
	def __init__(self,nombre):
		self.nombre = nombre
		self.total = 0
		self.montos = []
		self.next = None

	def add(self,monto):
		self.total += monto
		self.montos.append(monto)

	def remove(self,monto):
		i = 0
		for saldo in self.montos:
			if saldo == monto:
				self.total -= self.montos.pop(i)
				break
			i += 1

	def erase(self):
		self.total = 0
		self.monto =[]

	def change(self,index,newMonto):
		if -1 < index < len(self.montos):
			self.total -= self.montos[index] + newMonto
			self.montos[index] = newMonto
		else:
			print("argumento no valido")

class GRIDRESUMEN:
	def __init__(self):
		self.first = None
		self.last = None
		self.len = 0

	def push (self,cliente):
		item = cliente
		self.len += 1

		if not self.first or not self.last:
			self.first = self.last = cliente
			return

		self.last.next = cliente
		self.last = cliente

	def show_resumen(self):
		for cliente in self:
			print("{} {}".format(cliente.nombre,cliente.total))
	
	def show_datos_cliente(self):
		for cliente in self:
		    print("Cliente: {}".format(cliente.nombre))
		    for indice,monto in enumerate(cliente.montos):
			print("{}- monto: {}".format(indice +1,monto))
		    print("Total: {}".format(cliente.total))

	def __iter__(self):
		return ITERGRID(self.first)

#------------------------------------------------------------------------------------------------------------------------
class DATO_FIADO:
    """Crea un objetos con los datos del cliente de la fecha que se realizo el fiado."""

    def __init__(self,cantidad,fecha,vendedor):
        """constructor de la clase."""
        self.fecha = fecha
        self.cantidad = int(cantidad)
        self.vendedor = vendedor
        self.next = None

class GRIDCLIENTE:
    """Guarda los datos del fiado usuario."""
    
    def __init__(self,nombre_cliente):
	"""Constructor de la clase."""
        self.nombre = nombre_cliente
        self.first = None
        self.last = None
        self.len = 0

    def agregar(self,dato_fiado):
	"""Guarda el objeto DATO_FIADO al final de la lista enlazada."""
        if not self.first:
            self.first = dato_fiado
            self.last = dato_fiado
        else:
            self.last.next = dato_fiado:
            self.last = dato_fiado
        self.len +=1

    def mostrar(self):
	"""Imprime por pantalla los datos del objeto DATO_FIADO, que se encuentra en la lista enlazada."""
        print("El cliente {} debe: ".format(self.nombre))
        for dato_fiado in self:
            print("{}, el dia: {}, fue atendido por: {}".format(dato_fiado.cantidad,dato_fiado.fecha,dato_fiado.vendedor))
	
    def __iter__(self):
        return ITERGRID(self.first)

#----------------------------------------------------------------------------------------------------------------------------

class ITERGRID:
	def __init__(self,first):
		self.current = first

	def _next(self):
		
		if not self.current:
			raise StopIteration

		cliente = self.current
		self.current = self.current.next
		return cliente

	def __next__(self):
		return self._next()


def main():
	leo = CLIENTE("LEO")
	leo.add(20)
	leo.add(30)
	leo.add(40)
	print(leo.nombre)
	print(leo.total)
	print(leo.montos)
	lukas = CLIENTE("lukas")
	lukas.add(29)
	print(lukas.nombre)
	print(lukas.total)
	print(lukas.montos)
	print("meto las cosas al grid")
	grid = GRID()
	grid.push(leo)
	grid.push(lukas)
	print("grid")
	grid.show_resumen()
