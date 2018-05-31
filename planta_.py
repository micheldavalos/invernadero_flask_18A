class Planta:
    def __init__(self, conexion, cursor):
        self.c = conexion
        self.cur = cursor
        
    def agregar(self, cultivo, fecha, id_invernadero):
        insertar = ("INSERT INTO planta(cultivo, fecha, id_invernadero) VALUES(%s, NOW(), %s)")
        self.cur.execute(insertar, (cultivo, id_invernadero))
        self.c.commit()

    def getCultivos(self, id):
        cultivos = []

        select_cultivos = ("SELECT * FROM planta WHERE id_invernadero = %s")
        self.cur.execute(select_cultivos, (id,))

        res = self.cur.fetchall()

        for r in res:
            cultivo = {
                'id': r[0],
                'cultivo': r[1],
                'fecha': r[2]
            }

            cultivos.append(cultivo)

        return  cultivos


