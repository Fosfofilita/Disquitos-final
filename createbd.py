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
    
    cursor.execute('SELECT COUNT(*) FROM productos')  #uso count para ver cuantos registros hay en la tabla y verififco si en la poscion 0 cuantos registros hay
    if cursor.fetchone()[0] == 0: 
        discos_iniciales = [
            ("Gulp", 1000, "gulp.jpg"),
            ("Paranoid", 5000, "paranoid.jpg"),
            ("Arise", 2000, "arise.jpg"),
            ("Toxicity", 1000, "toxicity.jpg")
        ]
        cursor.executemany('INSERT INTO productos (nombre, precio, imagen) VALUES (?, ?, ?)', discos_iniciales)  #ejeuta los datos anteriores, en cada ? va la variable o valor
        conexion.commit() 
        print("Base de datos creada y stock con imágenes cargado correctamente")
    else:
        print("La base de datos ya existe.") #si estos datos ya existen en la tabla no hace nada  
        
    conexion.close()

if __name__ == '__main__':
    inicializar_base_de_datos()

#python createbd.py