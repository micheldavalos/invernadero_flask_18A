import mysql.connector

conexion = mysql.connector.connect(user='michel', password='12345', database='invernadero')
cursor = conexion.cursor()

while True:
    print("1) Insertar")
    print("2) Mostrar")
    print("3) Eliminar")
    print("4) Modificar")
    print("0) Salir")
    op = input()
    
    if op == '1':
        nombre = input("Nombre del tipo: ")
        insertar = ("INSERT INTO tipo(nombre) VALUES (%s)")
        cursor.execute(insertar, (nombre,))
        conexion.commit()
    elif op == '2':
        select = ("SELECT * FROM tipo")
        cursor.execute(select)
        for c in cursor:
            print('{0:4} {1:15}'.format(c[0], c[1]))
            
    elif op == '3':
        id = input("Id: ")
        borrar = ("DELETE FROM tipo WHERE id = %s")
        cursor.execute(borrar, (id,))
        conexion.commit()
        
    elif op == '4':
        id = input("Id: ")
        nombre = input("Nombre: ")
        modificar = ("UPDATE tipo SET nombre = %s WHERE id = %s")
        cursor.execute(modificar, (nombre, id))
        conexion.commit()
        
    elif op == '0':
        break