	def filtrar(self,iniciales):
		"""Busca los nombres con las iniciales y las imprime por pantalla."""
		for cliente in self:
			if cliente.nombre[:len(iniciales)].lower() == iniciales.lower():
				print("{},{}".format(cliente.nombre,cliente.total))