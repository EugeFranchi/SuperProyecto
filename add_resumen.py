#Code by @masacr3
from * import nodo
from * import DB
from * import TIKET

def add_resumen(cliente):
	db = DB("resumen")
	if db.esta_id(cliente.nombre):
		return
	db.add(cliente.name,cliente.total)

def update_resumen(cliente,totalNuevo):
	db = DB("resumen")
	if not db.esta_id(cliente.nombre):
		return
	db.update(nombre.cliente,[1],[totalNuevo])


def add_tiket(cliente,pago,vendedor):
	tiketDB = TIKET("tiket")
	resumenDB = DB("resumen")

	if not resumenDB.esta_id(cliente.nombre):
		return

	ID,deuda = resumenDB.consulta(cliente.nombre)
	tiketDB.add(ID,deuda,pago,vendedor)

	saldo = deuda - pago
	if (saldo)<=0:
		resumenDB.delete(ID)

	update_resumen(cliente,saldo)



