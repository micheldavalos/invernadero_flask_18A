from planta import Planta
from datetime import datetime, date, timedelta
class MenuPlanta:
    def __init__(self, conexion, cursor):
        self.planta = Planta(conexion, cursor)
        
        while True:
            print('1) Agregar Planta')
            print('0) Salir')
            op = input('Opcion: ')
            
            if op == '1':
                self.agregar()
            elif op == '0':
                break
                
    def agregar(self):
        cultivo = input('Nombre del cultivo: ')
        fecha = datetime.now().date() + timedelta(days=2)
        year = input('Año: ')
        month = input('Mes: ')
        day = input('Dia: ')
        fecha = date(int(year), int(month), int(day))
        id_invernadero = input('Id Invernadero: ')
        self.planta.agregar(cultivo, fecha, id_invernadero)
