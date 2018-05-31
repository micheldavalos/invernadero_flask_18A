from invernaderoClass import InvernaderoClass
class MenuInvernadero:
    def __init__(self, conexion, cursor):
        self.invernadero = InvernaderoClass(conexion, cursor)
        while True:
            print('1) Agregar Dueño')
            print('2) Agregar Invernadero')
            print('3) Buscar')
            print('4) Agregar Usuario-Invernadero')
            print('0) Salir')
            op = input('>')
            
            if op == '1':
                self.agregarDueno()
            elif op == '2':
                self.agregarInvernadero()
            elif op == '3':
                self.buscar()
            elif op == '4':
                self.agregarUsuarioInvernadero()
            elif op == '0':
                break        
    
    def agregarDueno(self):
        nombre = input('Nombre del Dueño: ')
        apellidos = input('Apellidos del Dueño: ')
        self.invernadero.agregarDueno(nombre, apellidos)
    
    def agregarInvernadero(self):
        ubicacion = input('Ubicacion del invernadero: ')
        nombre = input('Nombre del invernadero: ')
        id_dueno = input('Id del dueño: ')
        self.invernadero.agregarInvernadero(ubicacion, nombre, id_dueno)
    
    def buscar(self):
        nombre = input('Nombre del invernadero: ')
        
        resultados = self.invernadero.buscar(nombre)
        
        for r in resultados:
            print("{0:3} {1:25} {2:15} {3:3}".format(r[0], r[1], r[2], r[3]))
    def agregarUsuarioInvernadero(self):
        id_usuario = int(input('Id de Usuario: '))
        id_invernadero = int(input('id de Invernadero'))
        self.invernadero.agregarInvernaderoUsuario(id_usuario, id_invernadero)