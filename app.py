from flask import Flask, jsonify, request, session
from flasgger import Swagger
import sqlite3

app = Flask(__name__, static_folder='static', static_url_path='')

app.secret_key = "123"

app.config['SWAGGER'] = {
    'openapi': '3.0.3'
}
swagger = Swagger (app, template_file='disquitos.yaml')

@app.route('/')
def inicio():
    return app.send_static_file('index.html')

def conectar_db():
    conexion = sqlite3.connect('disquitos.db')
    conexion.row_factory = sqlite3.Row #trasnformo las categorias en columnas para poder acceder a por nombre
    return conexion

@app.route('/productos')
def get_productos():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute('SELECT nombre, precio, imagen FROM productos') 
    filas = cursor.fetchall() #trae todas las filas/datos 
    conexion.close()
    
    lista_productos = [{"nombre": f["nombre"], "precio": f["precio"], "imagen": f["imagen"]} for f in filas]
    return jsonify({"Discos Disponibles": lista_productos})

@app.route('/productos/<string:nombre>')
def get_producto(nombre):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute('SELECT nombre, precio, imagen FROM productos WHERE LOWER(nombre) = LOWER(?)', (nombre,))
    fila = cursor.fetchone() #trae la consulta 
    conexion.close()
    
    if fila:
        return jsonify({"disco": {"nombre": fila["nombre"], "precio": fila["precio"], "imagen": fila["imagen"]}})
    else:
        return jsonify("Producto no encontrado"), 404


@app.route('/carrito', methods=['GET'])
def ver_carrito():
    if 'carrito' not in session:
        session['carrito'] = []
    return jsonify(session['carrito'])

@app.route('/carrito/agregar', methods=['POST'])
def agregar_carrito():
    if 'carrito' not in session:
        session['carrito'] = []
        
    data = request.get_json(force=True)
    nombre = data.get('nombre')
    cantidad = data.get('cantidad', 1)
    
    if not nombre:
        return jsonify("Falta el nombre del producto"), 400
        
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute('SELECT nombre, precio, imagen FROM productos WHERE LOWER(nombre) = LOWER(?)', (nombre,))
    fila = cursor.fetchone()
    conexion.close()
    
    if not fila:
        return jsonify("Producto no encontrado"), 404
        
    carrito = session['carrito']
    produ_encontrado = next((p for p in carrito if p['nombre'].lower() == nombre.lower()), None)
    
    if produ_encontrado:
        produ_encontrado['cantidad'] += cantidad
    else:
        carrito.append({
            "nombre": fila['nombre'],
            "precio": fila['precio'],
            "imagen": fila['imagen'], 
            "cantidad": cantidad
        })
        
    session['carrito'] = carrito
    session.modified = True
    return jsonify(f"Producto {nombre} agregado correctamente al carrito"), 200
    
@app.route('/carrito/<string:nombre>', methods=['DELETE'])
def eliminar_carrito(nombre):

    if 'carrito' not in session or len(session['carrito']) == 0:
        return jsonify("Carrito vacio"), 404

    carrito= session ['carrito'] 
    producto_encontrado = next((p for p in carrito if p['nombre'] == nombre), None)
    
    if not producto_encontrado:
        return jsonify("Producto no encontrado en el carrito"), 404
    
    carrito.remove(producto_encontrado)
    session.modified = True
    return jsonify({ "Producto eliminado": producto_encontrado, "carrito": carrito}),200

@app.route('/carrito/total', methods=['GET'])
def total_carrito():

    carrito = session.get('carrito', [])
    total = sum(p['precio'] * p['cantidad'] for p in carrito)

    return jsonify({"Total de Compra": total})

@app.route('/limpiar', methods=['POST'])
def limpiar_sesion():
    session.clear()  
    return jsonify("Reinicio de sesion"), 200


if __name__ == '__main__':
    app.run(debug=True)



