import cmd

class Shell(cmd.Cmd):
    intro = 'Bienvenido a mi programa.\nIngrese help o ? para listar los comandos.\n'
    prompt = '--> '
    
    
    def do_COMANDO(self,parametros):
        """Este metodo ejecuta un comando"""
        print("COMANDO - Parametros: ",parametros)
        Shell().cmdloop()
    
    
    def do_resumen(self, parametros):
        """
        Imprime por pantalla el resumen.
        """
        with open("resumen.txt") as f:
            arch_csv = csv.reader(f)
            for cliente,monto in arch_csv:
                print("{}: {}".format(cliente, monto))
    
    
    def do_salir(self,parametros):
        """
        Sale del programa.
        """
        system('cls')
        return True
    
    
    
    
Shell().cmdloop()
