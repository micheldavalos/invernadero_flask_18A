import hashlib
class InvernaderoClass:
    def __init__(self, conexion, cursor):
        self.c = conexion
        self.cur = cursor
        
    def agregarDueno(self, nombre, apellido):
        insertar = ('INSERT INTO dueno(nombre, apellido) VALUES(%s, %s)')
        self.cur.execute(insertar, (nombre, apellido))
        self.c.commit()
        
    def agregarInvernadero(self, ubicacion, nombre, id_dueno):
        insertar = ('INSERT INTO invernadero(ubicacion, nombre, id_dueno) VALUES(%s, %s, %s)')
        self.cur.execute(insertar, (ubicacion, nombre, id_dueno))
        self.c.commit()
        
    def buscar(self, nombre):
        _buscar = ("SELECT * FROM invernadero WHERE nombre LIKE %s")
        self.cur.execute(_buscar, ('%' + nombre + '%',))
        resultados = self.cur.fetchall()
        
        return resultados
    
    def agregarInvernaderoUsuario(self, id_usuario, id_invernadero):
        insertar = ("INSERT INTO usuario_invernadero(id_usuario, id_invernadero) VALUES(%s, %s)")
        self.cur.execute(insertar, (id_usuario, id_invernadero))
        self.c.commit()

    def getInvernaderos(self, user, password):
        # hash password
        pass_hash = hashlib.new('sha1', bytes(password, 'utf-8'))
        pass_hash = pass_hash.hexdigest()

        # obtener id usuario
        select_usuario = \
            ("SELECT id FROM usuario WHERE username = %s AND password = %s")

        self.cur.execute(select_usuario, (user, pass_hash))
        id = self.cur.fetchall()

        lista = []
        if id:
            id = id[0][0]
            print('id_usuario', id)

            # obtenemos id's de invernadero
            select_usuario_invernadero = \
                ("SELECT id_invernadero FROM usuario_invernadero WHERE id_usuario = %s")
            self.cur.execute(select_usuario_invernadero, (id, ))
            invernaderos_id = self.cur.fetchall()

            print('id_invernaderos', invernaderos_id)

            for i in invernaderos_id:
                inver = i[0]
                # obtener el invernadero
                select_invenadero = \
                    ("SELECT * FROM invernadero WHERE id = %s")
                self.cur.execute(select_invenadero, (inver,))
                res = self.cur.fetchall()
                print(res)

                if res:
                    select_plantas = \
                        ("SELECT COUNT(id) FROM planta WHERE id_invernadero=%s")
                    self.cur.execute(select_plantas, (res[0][0],))
                    plantas = self.cur.fetchall()

                    invernadero = {
                        'id': res[0][0],
                        'ubicacion': res[0][1],
                        'nombre': res[0][2],
                        'cultivos': plantas
                    }

                    lista.append(invernadero)
            return lista







