class grid:
	""" simula una grilla tipo tabla"""
	def __init__(self):
		self.clientes = {}

	def _esta(self,cliente):
		""" 
		verifica si esta el cliente
		"""
		return cliente in self.clientes

	def add(self,cliente,monto):
		"""
		agrega un cliente con su monto respetivo al grid
		"""
		if self._esta(cliente):
			return

		self.clientes[cliente] = monto

	def remove(self,cliente):
		"""
		elimina un cliente del grid
		"""
		if self._esta(cliente):
			self.clientes.pop(cliente)
		else:
			print("el cliente {} no exite".format(cliente))


	def mostrar(self):
		"""
		muestra los clientes
		"""
		print("{:15.15} {}".format("cliente","monto"))
		for cliente in self.clientes:
			print("{:15.15} {}".format(cliente,self.clientes[cliente]))
		


