from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Inicializa el controlador de Chrome
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# Abre la página web
url = 'https://www.espn.com.co/futbol-americano/nfl/estadisticas/equipo'
driver.get(url)

# Espera a que la tabla esté presente en la página
wait = WebDriverWait(driver, 10)
tabla_presente = EC.presence_of_element_located((By.CSS_SELECTOR, '.Table.Table--align-right.Table--fixed.Table--fixed-left'))
tabla = wait.until(tabla_presente)

# Obtén el contenido HTML de la tabla
tabla_html = tabla.get_attribute('outerHTML')

# Utiliza BeautifulSoup para analizar el contenido HTML
soup = BeautifulSoup(tabla_html, 'html.parser')

# Encuentra todas las filas de la tabla
filas = soup.find_all('tr')

# Inicializa una lista para almacenar los datos
datos = []

# Recorre las filas y obtén los datos de cada celda
for fila in filas:
    celdas = fila.find_all('td')
    fila_datos = [celda.text.strip() for celda in celdas]
    datos.append(fila_datos)

# Crea un DataFrame de Pandas con los datos
columnas = ['Columna1', 'Columna2', 'Columna3']  # Reemplaza con los nombres de tus columnas
df = pd.DataFrame(datos, columns=columnas)

# Cierra el navegador
driver.quit()

# Imprime el DataFrame
print(df)
