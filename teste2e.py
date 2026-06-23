import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def probar_flujo_compra_completo():
    # 1. Iniciar el navegador Chrome
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    try:
        # 2. Entrar a la aplicación
        driver.get("http://127.0.0.1:5000/")
        time.sleep(1)
        
        # 3. Limpiar la sesión haciendo clic en el botón "Vaciar Carrito" de la interfaz
        # Buscamos el botón gris de vaciar por su texto
        boton_vaciar = driver.find_element(By.XPATH, "//button[contains(text(), 'Vaciar Carrito')]")
        boton_vaciar.click()
        time.sleep(1) # Esperamos que se limpie la pantalla
        
        # 4. Buscar el primer producto (Gulp) y hacer clic en su botón "Agregar"
        primer_producto = driver.find_element(By.CLASS_NAME, "producto")
        boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
        
        print("clic del usuario en 'Agregar' para el disco Gulp")
        boton_agregar.click()
        
        # Esperamos 2 segundos para darle tiempo al fetch de actualizar la pantalla
        time.sleep(2)
        
        # 5. Validar que el total de la compra se haya actualizado correctamente a 1000
        elemento_total = driver.find_element(By.ID, "total-compra")
        texto_total = elemento_total.text
        
        print(f"Total detectado en pantalla: ${texto_total}")
        
        assert texto_total == "1000", f"Error: El total esperado era 1000 pero se obtuvo {texto_total}"
        print(" Prueba exitosa")
        
    except Exception as e:
        print(f"La prueba falló debido a: {e}")
        
    finally:
        # Cerrar el navegador controlado automáticamente
        time.sleep(3)
        driver.quit()

if __name__ == '__main__':
    probar_flujo_compra_completo()