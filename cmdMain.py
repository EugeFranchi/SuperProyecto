import cmd

class Shell(cmd.Cmd):
    intro = 'Bienvenido a mi programa.\nIngrese help o ? para listar los comandos.\n'
    prompt = '--> '
    
    
    def do_COMANDO(self,parametros):
        """Este metodo ejecuta un comando"""
        print("COMANDO - Parametros: ",parametros)
        Shell().cmdloop()

    
    
    
    
Shell().cmdloop()
