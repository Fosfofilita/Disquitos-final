
# Disquitos - Tienda de Discos Online

**Disquitos** es una aplicación web para la compra de discos de música en línea. Sus funciones principales son mostrar un catálogo de álbumes con portadas, gestionar un carrito de compras interactivo para agregar o eliminar productos, calcular el precio total en tiempo real y generar un ticket con el resumen final de la compra.

---

### Arquitectura del Sistema
El sistema utiliza una arquitectura cliente-servidor dividida en tres partes para procesar la información de forma independiente. El frontend maneja la interfaz de usuario en una sola página sin recargar el navegador. El backend funciona como una **API REST** que procesa las solicitudes de la pantalla y envía las respuestas en formato JSON. Los datos se dividen en una base de datos para el catálogo fijo de productos y en la memoria de sesión del servidor para almacenar el carrito de cada usuario de forma aislada.

### Tecnologías del Frontend
La interfaz visual utiliza **HTML5** para definir la estructura de los contenedores de la tienda. El diseño estético y la distribución del espacio se manejan con **CSS3**, aplicando el sistema **Flexbox** para organizar los discos en una grilla de tarjetas verticales. El dinamismo del sitio se programó con **JavaScript **, utilizando la interfaz **Fetch API** junto con **async/await** para comunicarse con el backend en segundo plano y actualizar los elementos de la pantalla en tiempo real.

### Tecnologías del Backend y Base de Datos
La lógica de control del servidor está escrita en **Python**. El servidor web utiliza el microframework **Flask** para estructurar las rutas de la API que comunican los datos con el cliente. Para el almacenamiento permanente se usa **SQLite**, una base de datos relacional embebida que guarda el inventario en un archivo local. En el entorno de producción en la nube se emplea **Gunicorn** como servidor WSGI para gestionar de forma eficiente múltiples solicitudes simultáneas de usuarios.

### Documentación y Calidad (QA)
Las rutas de comunicación están documentadas mediante **Flasgger & Swagger**, lo que permite mapear y probar los endpoints directamente desde el navegador. Las pruebas automáticas de código se estructuran con el framework **Pytest** para ejecutar verificaciones independientes. La simulación de usuario de extremo a extremo se realiza con **Selenium WebDriver**, un robot que abre el navegador y realiza los clics de compra para validar los totales. Estas pruebas emplean **Fixtures de Pytest** junto con la instrucción **yield** para controlar la apertura y el cierre seguro del navegador en cada ejecución.