import sqlite3

def inicializar_base_de_datos():
    conexion = sqlite3.connect('disquitos.db')
    cursor = conexion.cursor() 
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            imagen TEXT
        )
    ''')
    
    cursor.execute('SELECT COUNT(*) FROM productos')
    if cursor.fetchone()[0] == 0: 
        discos_iniciales = [
            ("Gulp", 1000, "gulp.jpg"),
            ("Paranoid", 5000, "paranoid.jpg"),
            ("Arise", 2000, "arise.jpg"),
            ("Toxicity", 1000, "toxicity.jpg")
        ]
        cursor.executemany('INSERT INTO productos (nombre, precio, imagen) VALUES (?, ?, ?)', discos_iniciales) 
        conexion.commit() 
        print("Base de datos creada y stock con imágenes cargado correctamente")
    else:
        print("La base de datos ya existe.")
        
    conexion.close()

if __name__ == '__main__':
    inicializar_base_de_datos()