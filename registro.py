class Registro:
    def __init__(self, conexion, cursor):
        self.c = conexion
        self.cur = cursor
        
    def agregar(self, co2, humedad, luz, ph, id_planta):
        insertar = ("INSERT INTO registro(co2, humedad, luz, ph, id_planta, fecha)  VALUES(%s, %s, %s, %s, %s, NOW())")
        
        self.cur.execute(insertar, (co2, humedad, luz, ph, id_planta))
        self.c.commit()
        
    def buscar(self, id_planta):
        buscar_ = ("SELECT * FROM registro WHERE id_planta = %s ORDER BY fecha DESC")
        self.cur.execute(buscar_, (id_planta,))
        return self.cur.fetchall()