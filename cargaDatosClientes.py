class CLIENTE:
	def __init__(self,cliente):
		self.nombre = cliente
		self.submonto = {}
		self.montototal= 0
		self.index = 0

	def add(self,monto):
		"""agrega submonto al cliente"""
		self.submonto[self.index] = monto
		self.montototal += monto
		self.index += 1

	def remove(self,index):
		"""
		elimina un item del submonto
		"""
		if self._esta(index):
			dato = self.submonto.pop(index)
			self.montototal -= dato
		else:
			print("El elemento {} no exite".format(index))

	def change(self,index,monto):
		"""
		modifica un atributo del subtotal
		"""
		if self._esta(index):
			self.montototal -= self.submonto[index]
			self.submonto[index] = monto
			self.montototal += monto
		else:
			print("el elemento {} no existe".format(index))

	def _esta(self,index):
		""" 
		verifica si esta el key en el diccionario
		"""
		return index in self.submonto