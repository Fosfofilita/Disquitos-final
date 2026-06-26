import time # paraagregar los sleep
import pytest  #uso fixture 
from selenium import webdriver 
from selenium.webdriver.common.by import By # busca por xpath, id, class

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
# creo la funcion dirver para que se ejecute en cada test , primero prepara el navegador con el timepo de carga
# hace la prueba y lo cierra, asi apra qcaa test.


def test_flujo_compra_completo(driver):
    driver.get("http://127.0.0.1:5000/")
    time.sleep(1)
    
    boton_vaciar = driver.find_element(By.XPATH, "//button[contains(text(), 'Vaciar Carrito')]")
    boton_vaciar.click()
    time.sleep(1)
    
    primer_producto = driver.find_element(By.CLASS_NAME, "producto") # agrega gulp porque es el primer producto en la lista
    boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
    
    print("Prueba 1: comprar 1 disco")
    boton_agregar.click()
    time.sleep(2)
    
    elemento_total = driver.find_element(By.ID, "total-compra")
    texto_total = elemento_total.text
    
    print(f"Total detectado: ${texto_total}")
    assert texto_total == "1000", f"Error: se esperaba 1000 pero se obtuvo {texto_total}"
    print("Prueba 1 exitosa") 

def test_compra_masiva_diez_discos(driver):
    driver.get("http://127.0.0.1:5000/")
    time.sleep(1)
    
    boton_vaciar = driver.find_element(By.XPATH, "//button[contains(text(), 'Vaciar Carrito')]")
    boton_vaciar.click()
    time.sleep(1)
    
    print("Prueba 2: comprando 10 unidades de Arise (Búsqueda Dinámica)")
    
    # busca en el contendedor que tenga un producto con el texto arise 
    tarjeta_arise = driver.find_element(By.XPATH, "//div[contains(@class, 'producto') and .//*[contains(text(), 'Arise')]]")
    boton_agregar_arise = tarjeta_arise.find_element(By.TAG_NAME, "button")

    for i in range(10):
        boton_agregar_arise.click()
        time.sleep(0.3)  
        
    time.sleep(2)
    
    elemento_total = driver.find_element(By.ID, "total-compra")
    texto_total = elemento_total.text
    
    print(f"Total detectado tras 10 clics en Arise: ${texto_total}")
    assert texto_total == "20000", f"Error: Se esperaba 20000 pero se obtuvo {texto_total}"
    print("Prueba 2 exitosa")

def test_finalizar_compra_y_emision_ticket(driver):
    driver.get("http://127.0.0.1:5000/")
    time.sleep(1)
    
    #vacio carrito
    boton_vaciar = driver.find_element(By.XPATH, "//button[contains(text(), 'Vaciar Carrito')]")
    boton_vaciar.click()
    time.sleep(1)
    
    print("Prueba 3: flujo de compra y reseteo de Tienda")
    
    # agrego disco paranoid
    tarjeta_para = driver.find_element(By.XPATH, "//div[contains(@class, 'producto') and .//*[contains(text(), 'Paranoid')]]")
    tarjeta_para.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    
    # busca y finaliza compra 
    boton_finalizar = driver.find_element(By.ID, "btn-finalizar")
    boton_finalizar.click()
    time.sleep(2) 
    
    # buscamos el contenedor ticket
    contenedor_ticket = driver.find_element(By.ID, "detalle-ticket")
    texto_ticket = contenedor_ticket.text
    
    print(f"Texto detectado en el ticket final:\n{texto_ticket}")
    
    # valido que  el ticket muestre el total y mencione al producto
    assert "Tu compra: $5000" in texto_ticket, "Error: El ticket no muestra el precio correcto"
    assert "Paranoid" in texto_ticket, "Error: El ticket no menciona el producto comprado"
    print("Visualizacion de ticket: OK")
    
    # verifico que la tienda vuelva a $0
    boton_volver = driver.find_element(By.XPATH, "//button[contains(text(), 'Volver a comprar')]")
    boton_volver.click()
    time.sleep(1)
    
    # valido el 0
    total_recargado = driver.find_element(By.ID, "total-compra").text
    assert total_recargado == "0", f"Error: Al volver a la tienda el total debió ser 0 pero ecnontro {total_recargado}"
    print("Reseteo de tienda a 0 : OK")
    
    print("Prueba 3 exitosa")


#pytest teste2e.py 