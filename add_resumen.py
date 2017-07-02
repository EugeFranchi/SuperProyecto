from * import nodo
from * import DB

def add_resumen(cliente):
	db = DB("resumen")
	if db.esta_id(cliente.nombre):
		return
	db.add(cliente.name,cliente.total)

def update_resumen(cliente):
	db = DB("resumen")
	if not db.esta_id(cliente.nombre):
		return
	
