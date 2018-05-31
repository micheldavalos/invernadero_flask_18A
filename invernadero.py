from menuUsuario import MenuUsuario
from menuInvernadeo import MenuInvernadero
from menuPlanta import MenuPlanta
from menuRegistro import MenuRegistro
import mysql.connector

conexion = mysql.connector.connect(user='michel', password='12345', database='invernadero')
cursor = conexion.cursor()

while True:
    print("1) Menu Usuario")
    print("2) Menu Invernadero")
    print("3) Menu Planta")
    print("4) Menu Registro")
    print("5) Salir")
    op = input(">")

    if op == "1":
        menu = MenuUsuario(conexion, cursor)
    elif op == "2":
        menuI = MenuInvernadero(conexion, cursor)
    elif op == "3":
        menuP = MenuPlanta(conexion, cursor)
    elif op == "4":
        menuR = MenuRegistro(conexion, cursor)
    elif op == "5":
        break

