from registro import Registro

class MenuRegistro:
    def __init__(self, conexion, cursor):
        self.registro = Registro(conexion, cursor)
        
        while True:
            print("1) Agregar Registro")
            print("2) Buscar")
            print("0) Salir")
            op = input("Opcion: ")
            
            if op == '1':
                self.agregar()
            elif op == '2':
                self.buscar()
            elif op == '0':
                break
                
    def agregar(self):
        co2 = float(input("CO2: "))
        humedad = float(input("Humedad: "))
        luz = float(input("Luz: "))
        ph = float(input("pH: "))
        id_planta = int(input("Id Planta: "))
        
        self.registro.agregar(co2, humedad, luz, ph, id_planta)
        
    def buscar(self):
        id_planta = int(input("Id de Planta: "))
        resultados = self.registro.buscar(id_planta)
        for r in resultados:
            print(r)