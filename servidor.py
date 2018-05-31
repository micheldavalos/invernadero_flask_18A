from flask import Flask, request, jsonify, make_response
from usuario import Usuario
from invernaderoClass import InvernaderoClass
import mysql.connector

conexion = mysql.connector.connect(user='michel',
                                   password='12345',
                                   database='invernadero')
cursor = conexion.cursor()

app = Flask(__name__)

usuarioBD = Usuario(conexion, cursor)
invernaderoBD = InvernaderoClass(conexion, cursor)

@app.route('/')
def hola():
    return "Hola"

@app.route('/login/', methods=['GET'])
def login():
    if request.method == 'GET':
        u = request.args.get('user')
        p = request.args.get('pwd')
        print(u)
        print(p)
        response = make_response(str(usuarioBD.login(u, p)))
        #origin = request.headers['Origin']
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    return "Login"


@app.route('/invernaderos/', methods=['POST'])
def invernaderos():
    if request.method == 'POST':

        objeto = [{
            'id': 0,
            'ubicacion': 'revolucion',
            'nombre': 'CUCEI',
            'cultivos': 0
        }, {
            'id': 1,
            'ubicacion': 'tlaquepaque',
            'nombre': 'prepa 12',
            'cultivos': 2
        }]

        print('antes del json')
        if request.is_json:
            json = request.get_json()
            print(json)

            u = json['user']
            p = json['pwd']

            print(u, p)
            return jsonify(invernaderoBD.getInvernaderos(u, p))

        return jsonify(objeto)


from planta import Planta
plantaDB = Planta(conexion, cursor)

@app.route('/cultivos/', methods=['GET'])
def plantas():
    if request.method == 'GET':
        print(request.args.get('id'))
        id = request.args.get('id')
        return jsonify(plantaDB.getCultivos(id))
    

app.run(host='0.0.0.0')