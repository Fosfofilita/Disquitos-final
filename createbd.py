import sqlite3

def inicializar_base_de_datos():
    conexion = sqlite3.connect('disquitos.db')
    cursor = conexion.cursor() # cursor indica posicion y permite ejecutar comandos 
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    
    cursor.execute('SELECT COUNT(*) FROM productos')
    if cursor.fetchone()[0] == 0: 
        discos_iniciales = [
            ("Gulp", 1000),
            ("Paranoid", 5000),
            ("Arise", 2000),
            ("Yes", 1000)
        ]
        cursor.executemany('INSERT INTO productos (nombre, precio) VALUES (?, ?)', discos_iniciales) # remplaza los insert 
        conexion.commit() # guardo de manera permanente 
        print("Base de datos creada y stock inicial cargado correctamente")
    else:
        print("La base de datos ya existe y tiene productos cargados.")
        
    conexion.close()

if __name__ == '__main__':
    inicializar_base_de_datos()