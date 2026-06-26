
# Disquitos - Tienda de Discos Online

**Disquitos** es una aplicación web para la compra de discos de musica en línea. Sus funciones principales son mostrar un catalogo de albumes con portadas, gestionar un carrito de compras interactivo para agregar o eliminar productos, calcular el precio total en tiempo real y generar un ticket con el resumen final de la compra.

---

### Arquitectura del Sistema
El sistema utiliza una arquitectura cliente-servidor dividida en tres partes para procesar la informacion de forma independiente. El frontend maneja la interfaz de usuario en una sola pagina sin recargar el navegador. El backend funciona como una api rest que procesa las solicitudes de la pantalla y envia las respuestas en formato json. Los datos se dividen en una base de datos para el catalogo fijo de productos y en la memoria de sesion del servidor para almacenar el carrito de cada usuario de forma aislada.

### Frontend
La interfaz visual utiliza html5 para definir la estructura de los contenedores de la tienda. El diseño estetico y la distribucion del espacio se manejan con css , aplicando el sistema flexbox  para organizar los discos en una grilla de tarjetas verticales. El dinamismo del sitio se programo con javascript, utilizando la interfaz fetch api junto con async o await para comunicarse con el backend en segundo plano y actualizar los elementos de la pantalla en tiempo real.

### Backend y Base de Datos
El servidor esta escrito en python . Utiliza el microframework flask para estructurar las rutas de la api que comunican los datos con el cliente. Para el almacenamiento permanente se usa sqlite*, una base de datos relacional que guarda el inventario en un archivo local.

### Complicaciones y Soluciones
**Complicacion 1:** Preparacion del Frontend con tarejtas dinamicas 
Al cambiar el diseño de la interfaz de una lista a tarjetas con su respectiva portada los elemntos se desalineaban de la pantalla y los titulos largos desconfiguraban el tamaño de los bloques , para solucionarlo separe las estructuras y aplique caracteristicas esteticas como flexbox y column los elementos se ordenaron de forma vertical y se distribuyeron uno al lado del otro solucionado el problema de estetica visual.

**Complicacion 2:** Incorporacion de la tarejta al backend
cuando realice la carga de las portadas en el servidor la pantalla mostraba errores de carga o los productos no aparecian porque las rutas de la consulta a la base de datos no incluian el arhivo imagen.Para resolverlo, modifique el codigo de python para que la ruta productos incluya la columna de la imagen en su select y en el frontend se uso fetch api y async wait para recibir las instrucciones json y devolver los archivos de imagen correspondientes.  

**Complicacion 3:** Logica del carrito y vinculacion con base de datos 
al presionar el boton de agregar, el sistema tenia fallas en el sevidor en falta de sincronzar los datos o dupliacion de datos. Para solucionarlo actualice la funcion en app.py que verifica la base de datos antes de guardar un elemneto. De este modo si se pide un producto y este ya existe en el carrito aumenta su cantidad, sino lo añade por primera vez.



