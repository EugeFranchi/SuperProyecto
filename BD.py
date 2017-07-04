#Code by @EugeFranchi and @masacr3 
from archivo import ARCHIVO
import csv

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
    
    
    def esta_id(self, ID):
        """
        Devuelve un valor booleano segun este
         o no el id pasado por parametro.
        """
        
        return self.consulta(ID) != []
    
    
    def add(self, *datos):
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
    
    
    def remove(self, ID):
        """
        Remueve la linea con el id indicado.
        """
        
        if not self.esta_id(ID):
            return
        
        archivo = []
        
        #guardo las lineas, quitando la que posee el id
        with open(self.nombre) as file:
            arch_csv = csv.reader(file)
            for linea in arch_csv:
                if linea[0] == ID:
                    continue
                archivo.append(linea)
        
        #reescribo la base de datos
        with open(self.nombre, "w") as file:
            for datos in archivo:
                file.write(",".join(datos) + "\n")
    
    
    
    def update(self, ID, col,values):
        """
        Actualiza la base de datos.
        """
        
        if not self.esta_id(ID):
            return
        
        archivo = []
        do = True
        
        #guardo las lineas, quitando la que posee el id
        with open(self.nombre) as file:
            arch_csv = csv.reader(file)
            for linea in arch_csv:
                if linea[0] == ID and do == True:
                    for i in range(len(col)):
                        linea[col[i]] = values[i]
                    do = False
                    break
                archivo.append(linea)
        
        #reescribo la base de datos
        with open(self.nombre, "w") as file:
            for datos in archivo:
                file.write(",".join(datos) + "\n")

    def select_all(self):
        table = []
        with open(self.nombre) as file:
            arch_csv = csv.reader(file)
            for linea in arch_csv:
                table.append(linea)
        return table
