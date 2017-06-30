    def __iter__(self):
           return Iterador(self.first)

class Iterador:
    """Crea la clase Iterador."""

    def __init__(self,primero):
        """Constructor de la clase iterador."""
        self.actual = primero

    def __next__(self):
        """Devuelve el dato y pasa al proximo nodo."""        
        if self.actual == None:
            raise StopIteracion("Lista Vacia")
        dato = self.actual
        self.actual = self.actual.next
        return dato