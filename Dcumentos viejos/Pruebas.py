#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import pandas as pd
import requests


# In[2]:


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

cookies = {
    'cookie_name': 'cookie_value'
}


# # Semana 1

# In[3]:


# Especifica la ubicación del controlador de Chrome (chromedriver.exe)
chromedriver_path = 'chromedriver.exe'

# Configura el servicio de Chrome con el argumento executable_path
chrome_service = ChromeService(executable_path=chromedriver_path)

# Crea una instancia del navegador Chrome con el servicio configurado
driver = webdriver.Chrome(service=chrome_service)

# Abre la página web
url = 'https://web.archive.org/web/20230912201251/https://www.espn.com/nfl/stats/team'
driver.get(url)

# Espera a que la tabla esté presente en la página
wait = WebDriverWait(driver, 10)
tabla_presente = EC.presence_of_element_located((By.CSS_SELECTOR, '.Table.Table--align-right.Table--fixed.Table--fixed-left'))
tabla = wait.until(tabla_presente)

# Obtén el contenido HTML de la ta bla
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
    if celdas:  # Verifica si hay al menos una celda de datos en la fila
        fila_datos = [celda.text.strip() for celda in celdas]
        datos.append(fila_datos)

# Crea un DataFrame de Pandas con los datos filtrados
columnas = ['Equipo']  # Reemplaza con el nombre de tu columna
dfoffsem1 = pd.DataFrame(datos, columns=columnas)


# Cierra el navegador
driver.quit()


# In[4]:


dfoffsem1


# In[105]:


urloffsem1 = "https://web.archive.org/web/20230912201251/https://www.espn.com/nfl/stats/team"


# In[106]:


roffsem1 = requests.get(urloffsem1, cookies=cookies, headers=headers)
html_contentsoffsem1 = roffsem1.text


# In[107]:


html_soupoffsem1 = BeautifulSoup(html_contentsoffsem1, 'html.parser')


# In[108]:


tabla_puntajeoffsem1 = html_soupoffsem1.find_all('table', class_='Table Table--align-right') 


# In[109]:


columnasoffsem1 =  ['GP','YDS','YDS/G','YDS','YDS/G',
             'YDS','YDS/G','PTS','PTS/G',]


# In[111]:


infoffsem1 = pd.DataFrame(columns = columnasoffsem1)


# In[112]:


for table in tabla_puntajeoffsem1:
    for row in table.find_all('tr')[2:]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(columnasoffsem1):
            infoffsem1.loc[len(infoffsem1)] = values


# In[113]:


infoffsem1


# In[114]:


columnsUnid = pd.concat([dfoffsem1,infoffsem1], axis=1)


# In[115]:


columnsUnid


# In[116]:


columnsUnid.to_excel('Export\\Ofensemana1ESPN.xlsx')

