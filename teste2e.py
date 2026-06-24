import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def probar_flujo_compra_completo():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    try:
        driver.get("http://127.0.0.1:5000/")
        time.sleep(1)
        #busco el botón gris usando xpath por texto exacto que muestra
        boton_vaciar = driver.find_element(By.XPATH, "//button[contains(text(), 'Vaciar Carrito')]")
        boton_vaciar.click()
        time.sleep(1)
        
        #selecciono primer producto de la lista  
        primer_producto = driver.find_element(By.CLASS_NAME, "producto")
        boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
        
        print("Prueba 1: comprar 1 disco")
        boton_agregar.click()
        time.sleep(2)
        
        elemento_total = driver.find_element(By.ID, "total-compra")
        texto_total = elemento_total.text
        
        print(f"Total detectado: ${texto_total}")
        assert texto_total == "1000", f"Error: se esperaba 1000 pero se obtuvo {texto_total}"
        print("Prueba 1 exitosa") #valido que aparezca 1000 en la pantalla 
        
    except Exception as e:
        print(f"La prueba 1 falló debido a: {e}")
        
    finally:
        driver.quit()

def probar_compra_masiva_diez_discos():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    try:
        driver.get("http://127.0.0.1:5000/")
        time.sleep(1)
        
        boton_vaciar = driver.find_element(By.XPATH, "//button[contains(text(), 'Vaciar Carrito')]")
        boton_vaciar.click()
        time.sleep(1)
        
        print("Prueba 2: comprando 10 unidades de arise")
        # //div[contains(@class, "producto")] busca cualquier tarjeta de producto en la pantalla
        # .//*[contains(text(), "Arise")]]'  se queda con la tarjeta que adentro tenga el texto arise 
        # el * indica que no importa si el título es un h3 h4
        # guarda esa tarjeta específica en la variable tarjeta arise.
        tarjeta_arise = driver.find_element(By.XPATH, "//div[contains(@class, 'producto') and .//*[contains(text(), 'Arise')]]")
     
        # Buscá la etiqueta button de tarjeta_arise
        boton_agregar_arise = tarjeta_arise.find_element(By.TAG_NAME, "button")
       

        for i in range(10):
            boton_agregar_arise.click()
            time.sleep(0.3)  # agrego hasta llegar a 10 con un delay entre click
            
        time.sleep(2)
        
        elemento_total = driver.find_element(By.ID, "total-compra")
        texto_total = elemento_total.text
        
        print(f"Total detectado tras 10 clics en Arise: ${texto_total}")
        assert texto_total == "20000", f"Error: Se esperaba 20000 pero se obtuvo {texto_total}"
        print("Prueba 2 exitosa")
        
    except Exception as e:
        print(f"La prueba 2 falló debido a: {e}")
        
    finally:
        time.sleep(3)
        driver.quit()

if __name__ == '__main__':
    probar_flujo_compra_completo()
    probar_compra_masiva_diez_discos()

    #python teste2e.py