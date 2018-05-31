from usuario import Usuario
import getpass

class MenuUsuario:
    def __init__(self, conexion, cursor):
        self.usuario = Usuario(conexion, cursor)
        
        while True:
            print("1) Crear Usuario")
            print("2) Buscar Usuario")
            print("3) Modificar Usuario")
            print("4) Login")
            print("0) Salir")
            op = input("Selecciona una opcion: ")
            
            if op == '1':
                self.crearUsuario()
            elif op == '2':
                self.buscarUsuario()
            elif op == '3':
                pass
            elif op == '4':
                self.login()
            elif op == '0':
                break
                
    def crearUsuario(self):
        nombre = input("Nombre de usuario: ")
        password = getpass.getpass("Password: ")
        tipo = input("Tipo de Usuario")
        
        self.usuario.crear(nombre, password, tipo)
        
    def buscarUsuario(self):
        nombre = input("Username a buscar: ")
        
        resultados = self.usuario.buscar(nombre)
        
        for r in resultados:
            print("{0:15} {1:15} {2:2}".format(r[0], r[1], r[2]))
            
    def login(self):
        nombre = input("Nombre de usuario: ")
        password = getpass.getpass("Password: ")
        
        l = self.usuario.login(nombre, password)
        
        if l == True:
            print('Usuario Logeado')
        else:
            print('El usuario no existe o contraseña incorrecta')        
