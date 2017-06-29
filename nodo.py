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
				self.montos.pop(i)
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

class GRID:
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

	def show(self):
		while not (self.first == None):
			print ("{} {} ".format(self.first.nombre,self.first.total))
			self.first = self.first.next


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
	grid.show()
