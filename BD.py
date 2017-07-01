from archivo import ARCHIVO

class BD:
    
    def __init__(self, nombre):
        """
        Inicializa la Base de Datos.
        """
        
        self.database = ARCHIVO(nombre)
        self.database.create()
        self.nombre = self.database.nombre
    
    
    def consulta(self,nombre):
        """
        Devuelve la información de nombre en una lista.
        """
        
        with open(self.nombre) as file:
            arch_csv = csv.reader(file)
            for linea in arch_csv:
                if linea[0] == nombre:
                    return linea
        return []
    
    
    def esta_id(self, id):
        """
        Devuelve un valor booleano segun este
         o no el id pasado por parametro.
        """
        
        return self.consulta(id) != []
    
    
    def add(self, datos):
        """
        Recibe una lista de datos y la agrega a la
        base de datos.
        """
        datos_nuevos = []
        with open(self.nombre, "r+") as file:
            linea = file.readline()
            while linea:
                linea = file.readline()
            
            for elem in datos:
                datos_nuevos.append(str(elem))
            nueva = ",".join(datos_nuevos)
            file.write(nueva + "\n")
    
    
    def remove(self, id):
        """
        Remueve la linea con el id indicado.
        """
        
        if not self.esta_id(id):
            return
        
        archivo = []
        
        #guardo las lineas, quitando la que posee el id
        with open(self.nombre) as file:
            arch_csv = csv.reader(file)
            for linea in arch_csv:
                if linea[0] == id:
                    continue
                archivo.append(linea)
        
        #reescribo la base de datos
        with open(self.nombre, "w") as file:
            for datos in archivo:
                file.write(",".join(datos) + "\n")
    
    
    
    def update(self, id, monto):
        """
        Actualiza la base de datos.
        """
        
        if not self.esta_id(id):
            return
        
        archivo = []
        
        #guardo las lineas, quitando la que posee el id
        with open(self.nombre) as file:
            arch_csv = csv.reader(file)
            for linea in arch_csv:
                if linea[0] == id:
                    linea[1] = int(linea[1]) + int(monto)
                    linea[1] = str(linea[1])
                archivo.append(linea)
        
        #reescribo la base de datos
        with open(self.nombre, "w") as file:
            for datos in archivo:
                file.write(",".join(datos) + "\n")
