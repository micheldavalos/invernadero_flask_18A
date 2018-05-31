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

    def getInvernaderos(self, usuario, password):
        pass_hash = hashlib.new('sha1', bytes(password, 'utf-8'))
        pass_hash = pass_hash.hexdigest()
        lista = []
        select_usuario = ("SELECT id FROM usuario WHERE username = %s AND password = %s")
        self.cur.execute(select_usuario, (usuario, pass_hash))
        id = self.cur.fetchall()
        print("id", id[0][0])
        if id:
            id = id[0][0]

            select_usuario_invernadero = ("SELECT id_invernadero FROM usuario_invernadero WHERE id_usuario = %s")
            self.cur.execute(select_usuario_invernadero, (id,))
            invernaderos_id = self.cur.fetchall()

            print("id_inv", invernaderos_id)

            select_invernadero = ("SELECT * FROM invernadero WHERE id = %s")
            for i in invernaderos_id:
                self.cur.execute(select_invernadero, (i[0],))
                inv = self.cur.fetchall()
                print("inv", inv)
                if inv:
                    inve = inv[0]
                    count = ("SELECT COUNT(id) FROM planta WHERE id_invernadero = %s")
                    self.cur.execute(count, (id_invernadero,))
                    res = self.cur.fetchall()
                    print(res)
                    invernadero = {
                        'id': inve[0],
                        'ubicacion': inve[1],
                        'nombre': inve[2],
                        'cultivos': 0
                    }
                    lista.append(invernadero)

        return lista
