from flask import Flask, request, jsonify, make_response
from usuario import Usuario
from invernaderoClass import InvernaderoClass
from planta_ import Planta
import mysql.connector

from flask_cors import CORS

conexion = mysql.connector.connect(user='michel', password='12345', database='invernadero')
cursor = conexion.cursor()

app = Flask(__name__)
CORS(app)
app.DEBUG = True
userDB = Usuario(conexion, cursor)
invernadero = InvernaderoClass(conexion, cursor)
plantaDB = Planta(conexion, cursor)

@app.route('/login/', methods = ['GET'])
def login():
    if request.method == 'GET':
        user = request.args.get('user')
        pwd = request.args.get('pwd')
        print(user, pwd)
        print(userDB.login(user, pwd))
        #response = make_response(str(userDB.login(user, pwd)))
        #response.headers.add('Access-Control-Allow-Origin', '*')
        #return response
        return "True"

@app.route('/invernaderos/', methods=['POST'])
def invernaderos():
    print('aqui', request.method)
    if request.method == 'POST':
        print(request.headers['Content-Type'])
        #if request.headers['Content-Type'] == 'application/json':
        if request.is_json:
            print(request.get_json())
            datos = request.get_json()
            u = datos['user']
            p = datos['pwd']

            print(u, p)

            # print(invernadero.getInvernaderos(u, p))
            return jsonify(invernadero.getInvernaderos(u, p))

@app.route('/plantas/', methods=['GET'])
def plantas():
    if request.method == 'GET':
        print(request.args.get('id'))
        id = request.args.get('id')
        return jsonify(plantaDB.getCultivos(id))

@app.route('/cultivos/', methods=['GET'])
def cultivos():
    if request.method == 'GET':
        print(request.args.get('id'))
        id = request.args.get('id')
        return jsonify(plantaDB.getCultivos(id))


app.run(host= '0.0.0.0')

