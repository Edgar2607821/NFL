#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2
#from sqlalchemy import create_engine


# In[2]:


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

cookies = {
    'cookie_name': 'cookie_value'
}


# In[3]:


urlDal = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/dal"


# In[4]:


urlGb = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/gb"


# In[5]:


urlMia = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/mia"


# In[6]:


urlJax = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/jax"


# In[7]:


urlLar = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/lar"


# In[8]:


urlSf = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/sf"


# In[9]:


urlBal = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/bal"


# In[10]:


urlPhi = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/phi"


# In[11]:


urlAtl = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/atl"


# In[12]:


urlCle = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/cle"


# In[13]:


urlNyj = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/nyj"


# In[14]:


urlDet = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/det"


# In[15]:


urlTb = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/tb"


# In[16]:


urlWsh = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/wsh"


# In[17]:


urlLv = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/lv"


# In[18]:


urlNo = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/no"


# In[19]:


urlLac = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/lac"


# In[20]:


urlInd = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/ind"


# In[21]:


urlChi = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/chi"


# In[22]:


urlKc = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/kc"


# In[23]:


urlNe = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/ne"


# In[24]:


urlMin = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/min"


# In[25]:


urlAri = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/ari"


# In[26]:


urlBuf = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/buf"


# In[27]:


urlDen = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/den"


# In[28]:


urlTen = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/ten"


# In[29]:


urlSea = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/sea"


# In[30]:


urlCar = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/car"


# In[31]:


urlHou = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/hou"


# In[32]:


urlPit = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/pit"


# In[33]:


urlCin = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/cin"


# In[34]:


urlNyg = "https://www.espn.com.mx/futbol-americano/nfl/equipo/calendario/_/nombre/nyg"


# In[35]:


TabGen = ['Semana','Fecha', 'Oponente','Resultado','G-P','L.Pases','L. Corr','L. Recib']


# In[36]:


rDal = requests.get(urlDal, cookies=cookies, headers=headers)
html_contentsDal = rDal.text


# In[37]:


html_soupDal = BeautifulSoup(html_contentsDal, 'html.parser')


# In[38]:


calendarioDal = html_soupDal.find_all('table', class_='Table') 


# In[39]:


Dallas = pd.DataFrame(columns = TabGen)


# In[40]:


for table in calendarioDal:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Dallas.loc[len(Dallas)] = values


# In[41]:


Dallas.insert(0, 'Equipo', 'Dallas Cowboys')
Dallas['Resultado_L'] = Dallas['Resultado'].str.extract(r'([A-Za-z]+)')
Dallas['Resultado_Numeros'] = Dallas['Resultado'].str.extract(r'(\d+-\d+)')
Dallas[['R1', 'R2']] = Dallas['Resultado_Numeros'].str.split('-', expand=True)
Dallas['Local_Visitante'] = Dallas['Oponente'].str.split().str[0].str.replace('.', '')
Dallas['Local_Visitante'] = Dallas['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Dallas['Equipo_Oponente'] = Dallas['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Dallas['G'] = (Dallas['Resultado_L'] == 'G').astype(int)
Dallas['P'] = (Dallas['Resultado_L'] == 'P').astype(int)
Dallas['E'] = (Dallas['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Dallas_select = Dallas[columnas_deseadas]
Dallas_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Dallas_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Dallas_select = Dallas_select.copy()
Dallas_select['Diferencia_Pts.'] = Dallas_select['R1'] - Dallas_select['R2']


# In[42]:


Dallas_select


# In[43]:


rGb = requests.get(urlGb, cookies=cookies, headers=headers)
html_contentsGb = rGb.text


# In[44]:


html_soupGb = BeautifulSoup(html_contentsGb, 'html.parser')


# In[45]:


calendarioGb = html_soupGb.find_all('table', class_='Table') 


# In[46]:


Green_Bay = pd.DataFrame(columns = TabGen)


# In[47]:


for table in calendarioGb:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Green_Bay.loc[len(Green_Bay)] = values


# In[48]:


Green_Bay.insert(0, 'Equipo', 'Green Bay Packers')
Green_Bay['Resultado_L'] = Green_Bay['Resultado'].str.extract(r'([A-Za-z]+)')
Green_Bay['Resultado_Numeros'] = Green_Bay['Resultado'].str.extract(r'(\d+-\d+)')
Green_Bay[['R1', 'R2']] = Green_Bay['Resultado_Numeros'].str.split('-', expand=True)
Green_Bay['Local_Visitante'] = Green_Bay['Oponente'].str.split().str[0].str.replace('.', '')
Green_Bay['Local_Visitante'] = Green_Bay['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Green_Bay['Equipo_Oponente'] = Green_Bay['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Green_Bay['G'] = (Green_Bay['Resultado_L'] == 'G').astype(int)
Green_Bay['P'] = (Green_Bay['Resultado_L'] == 'P').astype(int)
Green_Bay['E'] = (Green_Bay['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Green_Bay_select = Green_Bay[columnas_deseadas]
Green_Bay_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Green_Bay_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Green_Bay_select = Green_Bay_select.copy()
Green_Bay_select['Diferencia_Pts.'] = Green_Bay_select['R1'] - Green_Bay_select['R2']


# In[49]:


Green_Bay_select


# In[50]:


rMia = requests.get(urlMia, cookies=cookies, headers=headers)
html_contentsMia = rMia.text


# In[51]:


html_soupMia = BeautifulSoup(html_contentsMia, 'html.parser')


# In[52]:


calendarioMia = html_soupMia.find_all('table', class_='Table') 


# In[53]:


Miami = pd.DataFrame(columns = TabGen)


# In[54]:


for table in calendarioMia:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Miami.loc[len(Miami)] = values


# In[55]:


Miami.insert(0, 'Equipo', 'Miami Dolphins')
Miami['Resultado_L'] = Miami['Resultado'].str.extract(r'([A-Za-z]+)')
Miami['Resultado_Numeros'] = Miami['Resultado'].str.extract(r'(\d+-\d+)')
Miami[['R1', 'R2']] = Miami['Resultado_Numeros'].str.split('-', expand=True)
Miami['Local_Visitante'] = Miami['Oponente'].str.split().str[0].str.replace('.', '')
Miami['Local_Visitante'] = Miami['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Miami['Equipo_Oponente'] = Miami['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Miami['G'] = (Miami['Resultado_L'] == 'G').astype(int)
Miami['P'] = (Miami['Resultado_L'] == 'P').astype(int)
Miami['E'] = (Miami['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Miami_select = Miami[columnas_deseadas]
Miami_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Miami_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Miami_select = Miami_select.copy()
Miami_select['Diferencia_Pts.'] = Miami_select['R1'] - Miami_select['R2']


# In[56]:


Miami_select


# In[57]:


rJax = requests.get(urlJax, cookies=cookies, headers=headers)
html_contentsJax = rJax.text


# In[58]:


html_soupJax = BeautifulSoup(html_contentsJax, 'html.parser')


# In[59]:


calendarioJax = html_soupJax.find_all('table', class_='Table') 


# In[60]:


Jacksonville = pd.DataFrame(columns = TabGen)


# In[61]:


for table in calendarioJax:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Jacksonville.loc[len(Jacksonville)] = values


# In[62]:


Jacksonville.insert(0, 'Equipo', 'Jacksonville Jaguars')
Jacksonville['Resultado_L'] = Jacksonville['Resultado'].str.extract(r'([A-Za-z]+)')
Jacksonville['Resultado_Numeros'] = Jacksonville['Resultado'].str.extract(r'(\d+-\d+)')
Jacksonville[['R1', 'R2']] = Jacksonville['Resultado_Numeros'].str.split('-', expand=True)
Jacksonville['Local_Visitante'] = Jacksonville['Oponente'].str.split().str[0].str.replace('.', '')
Jacksonville['Local_Visitante'] = Jacksonville['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Jacksonville['Equipo_Oponente'] = Jacksonville['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Jacksonville['G'] = (Jacksonville['Resultado_L'] == 'G').astype(int)
Jacksonville['P'] = (Jacksonville['Resultado_L'] == 'P').astype(int)
Jacksonville['E'] = (Jacksonville['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Jacksonville_select = Jacksonville[columnas_deseadas]
Jacksonville_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Jacksonville_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Jacksonville_select = Jacksonville_select.copy()
Jacksonville_select['Diferencia_Pts.'] = Jacksonville_select['R1'] - Jacksonville_select['R2']


# In[63]:


Jacksonville_select


# In[64]:


rLar = requests.get(urlLar, cookies=cookies, headers=headers)
html_contentsLar = rLar.text


# In[65]:


html_soupLar = BeautifulSoup(html_contentsLar, 'html.parser')


# In[66]:


calendarioLar = html_soupLar.find_all('table', class_='Table') 


# In[67]:


Los_Angeles_Rams = pd.DataFrame(columns = TabGen)


# In[68]:


for table in calendarioLar:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Los_Angeles_Rams.loc[len(Los_Angeles_Rams)] = values


# In[69]:


Los_Angeles_Rams.insert(0, 'Equipo', 'Los Angeles Rams')
Los_Angeles_Rams['Resultado_L'] = Los_Angeles_Rams['Resultado'].str.extract(r'([A-Za-z]+)')
Los_Angeles_Rams['Resultado_Numeros'] = Los_Angeles_Rams['Resultado'].str.extract(r'(\d+-\d+)')
Los_Angeles_Rams[['R1', 'R2']] = Los_Angeles_Rams['Resultado_Numeros'].str.split('-', expand=True)
Los_Angeles_Rams['Local_Visitante'] = Los_Angeles_Rams['Oponente'].str.split().str[0].str.replace('.', '')
Los_Angeles_Rams['Local_Visitante'] = Los_Angeles_Rams['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Los_Angeles_Rams['Equipo_Oponente'] = Los_Angeles_Rams['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Los_Angeles_Rams['G'] = (Los_Angeles_Rams['Resultado_L'] == 'G').astype(int)
Los_Angeles_Rams['P'] = (Los_Angeles_Rams['Resultado_L'] == 'P').astype(int)
Los_Angeles_Rams['E'] = (Los_Angeles_Rams['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Los_Angeles_Rams_select = Los_Angeles_Rams[columnas_deseadas]
Los_Angeles_Rams_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Los_Angeles_Rams_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Los_Angeles_Rams_select = Los_Angeles_Rams_select.copy()
Los_Angeles_Rams_select['Diferencia_Pts.'] = Los_Angeles_Rams_select['R1'] - Los_Angeles_Rams_select['R2']


# In[70]:


Los_Angeles_Rams_select


# In[71]:


rSf = requests.get(urlSf, cookies=cookies, headers=headers)
html_contentsSf = rSf.text


# In[72]:


html_soupSf = BeautifulSoup(html_contentsSf, 'html.parser')


# In[73]:


calendarioSf = html_soupSf.find_all('table', class_='Table') 


# In[74]:


San_Francisco = pd.DataFrame(columns = TabGen)


# In[75]:


for table in calendarioSf:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            San_Francisco.loc[len(San_Francisco)] = values


# In[76]:


San_Francisco.insert(0, 'Equipo', 'San Francisco 49ers')
San_Francisco['Resultado_L'] = San_Francisco['Resultado'].str.extract(r'([A-Za-z]+)')
San_Francisco['Resultado_Numeros'] = San_Francisco['Resultado'].str.extract(r'(\d+-\d+)')
San_Francisco[['R1', 'R2']] = San_Francisco['Resultado_Numeros'].str.split('-', expand=True)
San_Francisco['Local_Visitante'] = San_Francisco['Oponente'].str.split().str[0].str.replace('.', '')
San_Francisco['Local_Visitante'] = San_Francisco['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
San_Francisco['Equipo_Oponente'] = San_Francisco['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
San_Francisco['G'] = (San_Francisco['Resultado_L'] == 'G').astype(int)
San_Francisco['P'] = (San_Francisco['Resultado_L'] == 'P').astype(int)
San_Francisco['E'] = (San_Francisco['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
San_Francisco_select = San_Francisco[columnas_deseadas]
San_Francisco_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = San_Francisco_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
San_Francisco_select = San_Francisco_select.copy()
San_Francisco_select['Diferencia_Pts.'] = San_Francisco_select['R1'] - San_Francisco_select['R2']


# In[77]:


San_Francisco_select


# In[78]:


rBal = requests.get(urlBal, cookies=cookies, headers=headers)
html_contentsBal = rBal.text


# In[79]:


html_soupBal = BeautifulSoup(html_contentsBal, 'html.parser')


# In[80]:


calendarioBal = html_soupBal.find_all('table', class_='Table') 


# In[81]:


Baltimore_Ravens = pd.DataFrame(columns = TabGen)


# In[82]:


for table in calendarioBal:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Baltimore_Ravens.loc[len(Baltimore_Ravens)] = values


# In[83]:


Baltimore_Ravens.insert(0, 'Equipo', 'Baltimore Ravens')
Baltimore_Ravens['Resultado_L'] = Baltimore_Ravens['Resultado'].str.extract(r'([A-Za-z]+)')
Baltimore_Ravens['Resultado_Numeros'] = Baltimore_Ravens['Resultado'].str.extract(r'(\d+-\d+)')
Baltimore_Ravens[['R1', 'R2']] = Baltimore_Ravens['Resultado_Numeros'].str.split('-', expand=True)
Baltimore_Ravens['Local_Visitante'] = Baltimore_Ravens['Oponente'].str.split().str[0].str.replace('.', '')
Baltimore_Ravens['Local_Visitante'] = Baltimore_Ravens['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Baltimore_Ravens['Equipo_Oponente'] = Baltimore_Ravens['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Baltimore_Ravens['G'] = (Baltimore_Ravens['Resultado_L'] == 'G').astype(int)
Baltimore_Ravens['P'] = (Baltimore_Ravens['Resultado_L'] == 'P').astype(int)
Baltimore_Ravens['E'] = (Baltimore_Ravens['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Baltimore_Ravens_select = Baltimore_Ravens[columnas_deseadas]
Baltimore_Ravens_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Baltimore_Ravens_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Baltimore_Ravens_select = Baltimore_Ravens_select.copy()
Baltimore_Ravens_select['Diferencia_Pts.'] = Baltimore_Ravens_select['R1'] - Baltimore_Ravens_select['R2']


# In[84]:


Baltimore_Ravens_select


# In[85]:


rPhi = requests.get(urlPhi, cookies=cookies, headers=headers)
html_contentsPhi = rPhi.text


# In[86]:


html_soupPhi = BeautifulSoup(html_contentsPhi, 'html.parser')


# In[87]:


calendarioPhi = html_soupPhi.find_all('table', class_='Table') 


# In[88]:


Philadelphia = pd.DataFrame(columns = TabGen)


# In[89]:


for table in calendarioPhi:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Philadelphia.loc[len(Philadelphia)] = values


# In[90]:


Philadelphia.insert(0, 'Equipo', 'Philadelphia Eagles')
Philadelphia['Resultado_L'] = Philadelphia['Resultado'].str.extract(r'([A-Za-z]+)')
Philadelphia['Resultado_Numeros'] = Philadelphia['Resultado'].str.extract(r'(\d+-\d+)')
Philadelphia[['R1', 'R2']] = Philadelphia['Resultado_Numeros'].str.split('-', expand=True)
Philadelphia['Local_Visitante'] = Philadelphia['Oponente'].str.split().str[0].str.replace('.', '')
Philadelphia['Local_Visitante'] = Philadelphia['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Philadelphia['Equipo_Oponente'] = Philadelphia['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Philadelphia['G'] = (Philadelphia['Resultado_L'] == 'G').astype(int)
Philadelphia['P'] = (Philadelphia['Resultado_L'] == 'P').astype(int)
Philadelphia['E'] = (Philadelphia['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Philadelphia_select = Philadelphia[columnas_deseadas]
Philadelphia_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Philadelphia_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Philadelphia_select = Philadelphia_select.copy()
Philadelphia_select['Diferencia_Pts.'] = Philadelphia_select['R1'] - Philadelphia_select['R2']


# In[91]:


Philadelphia_select


# In[92]:


rAtl = requests.get(urlAtl, cookies=cookies, headers=headers)
html_contentsAtl = rAtl.text


# In[93]:


html_soupAtl = BeautifulSoup(html_contentsAtl, 'html.parser')


# In[94]:


calendarioAtl = html_soupAtl.find_all('table', class_='Table') 


# In[95]:


Atlanta = pd.DataFrame(columns = TabGen)


# In[96]:


for table in calendarioAtl:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Atlanta.loc[len(Atlanta)] = values


# In[97]:


Atlanta.insert(0, 'Equipo', 'Atlanta Falcons')
Atlanta['Resultado_L'] = Atlanta['Resultado'].str.extract(r'([A-Za-z]+)')
Atlanta['Resultado_Numeros'] = Atlanta['Resultado'].str.extract(r'(\d+-\d+)')
Atlanta[['R1', 'R2']] = Atlanta['Resultado_Numeros'].str.split('-', expand=True)
Atlanta['Local_Visitante'] = Atlanta['Oponente'].str.split().str[0].str.replace('.', '')
Atlanta['Local_Visitante'] = Atlanta['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Atlanta['Equipo_Oponente'] = Atlanta['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Atlanta['G'] = (Atlanta['Resultado_L'] == 'G').astype(int)
Atlanta['P'] = (Atlanta['Resultado_L'] == 'P').astype(int)
Atlanta['E'] = (Atlanta['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Atlanta_select = Atlanta[columnas_deseadas]
Atlanta_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Atlanta_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Atlanta_select = Atlanta_select.copy()
Atlanta_select['Diferencia_Pts.'] = Atlanta_select['R1'] - Atlanta_select['R2']


# In[98]:


Atlanta_select


# In[99]:


rCle = requests.get(urlCle, cookies=cookies, headers=headers)
html_contentsCle = rCle.text


# In[100]:


html_soupCle = BeautifulSoup(html_contentsCle, 'html.parser')


# In[101]:


calendarioCle = html_soupCle.find_all('table', class_='Table') 


# In[102]:


Cleveland = pd.DataFrame(columns = TabGen)


# In[103]:


for table in calendarioCle:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Cleveland.loc[len(Cleveland)] = values


# In[104]:


Cleveland.insert(0, 'Equipo', 'Cleveland Browns')
Cleveland['Resultado_L'] = Cleveland['Resultado'].str.extract(r'([A-Za-z]+)')
Cleveland['Resultado_Numeros'] = Cleveland['Resultado'].str.extract(r'(\d+-\d+)')
Cleveland[['R1', 'R2']] = Cleveland['Resultado_Numeros'].str.split('-', expand=True)
Cleveland['Local_Visitante'] = Cleveland['Oponente'].str.split().str[0].str.replace('.', '')
Cleveland['Local_Visitante'] = Cleveland['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Cleveland['Equipo_Oponente'] = Cleveland['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Cleveland['G'] = (Cleveland['Resultado_L'] == 'G').astype(int)
Cleveland['P'] = (Cleveland['Resultado_L'] == 'P').astype(int)
Cleveland['E'] = (Cleveland['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Cleveland_select = Cleveland[columnas_deseadas]
Cleveland_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Cleveland_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Cleveland_select = Cleveland_select.copy()
Cleveland_select['Diferencia_Pts.'] = Cleveland_select['R1'] - Cleveland_select['R2']


# In[105]:


Cleveland_select


# In[106]:


rNyj = requests.get(urlNyj, cookies=cookies, headers=headers)
html_contentsNyj = rNyj.text


# In[107]:


html_soupNyj = BeautifulSoup(html_contentsNyj, 'html.parser')


# In[108]:


calendarioNyj = html_soupNyj.find_all('table', class_='Table') 


# In[109]:


New_York_Jets = pd.DataFrame(columns = TabGen)


# In[110]:


for table in calendarioNyj:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            New_York_Jets.loc[len(New_York_Jets)] = values


# In[111]:


New_York_Jets.insert(0, 'Equipo', 'New York Jets')
New_York_Jets['Resultado_L'] = New_York_Jets['Resultado'].str.extract(r'([A-Za-z]+)')
New_York_Jets['Resultado_Numeros'] = New_York_Jets['Resultado'].str.extract(r'(\d+-\d+)')
New_York_Jets[['R1', 'R2']] = New_York_Jets['Resultado_Numeros'].str.split('-', expand=True)
New_York_Jets['Local_Visitante'] = New_York_Jets['Oponente'].str.split().str[0].str.replace('.', '')
New_York_Jets['Local_Visitante'] = New_York_Jets['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
New_York_Jets['Equipo_Oponente'] = New_York_Jets['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
New_York_Jets['G'] = (New_York_Jets['Resultado_L'] == 'G').astype(int)
New_York_Jets['P'] = (New_York_Jets['Resultado_L'] == 'P').astype(int)
New_York_Jets['E'] = (New_York_Jets['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
New_York_Jets_select = New_York_Jets[columnas_deseadas]
New_York_Jets_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = New_York_Jets_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
New_York_Jets_select = New_York_Jets_select.copy()
New_York_Jets_select['Diferencia_Pts.'] = New_York_Jets_select['R1'] - New_York_Jets_select['R2']


# In[112]:


New_York_Jets_select


# In[113]:


rDet = requests.get(urlDet, cookies=cookies, headers=headers)
html_contentsDet = rDet.text


# In[114]:


html_soupDet = BeautifulSoup(html_contentsDet, 'html.parser')


# In[115]:


calendarioDet = html_soupDet.find_all('table', class_='Table') 


# In[116]:


Detroit = pd.DataFrame(columns = TabGen)


# In[117]:


for table in calendarioDet:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Detroit.loc[len(Detroit)] = values


# In[118]:


Detroit.insert(0, 'Equipo', 'Detroit Lions')
Detroit['Resultado_L'] = Detroit['Resultado'].str.extract(r'([A-Za-z]+)')
Detroit['Resultado_Numeros'] = Detroit['Resultado'].str.extract(r'(\d+-\d+)')
Detroit[['R1', 'R2']] = Detroit['Resultado_Numeros'].str.split('-', expand=True)
Detroit['Local_Visitante'] = Detroit['Oponente'].str.split().str[0].str.replace('.', '')
Detroit['Local_Visitante'] = Detroit['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Detroit['Equipo_Oponente'] = Detroit['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Detroit['G'] = (Detroit['Resultado_L'] == 'G').astype(int)
Detroit['P'] = (Detroit['Resultado_L'] == 'P').astype(int)
Detroit['E'] = (Detroit['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Detroit_select = Detroit[columnas_deseadas]
Detroit_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Detroit_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Detroit_select = Detroit_select.copy()
Detroit_select['Diferencia_Pts.'] = Detroit_select['R1'] - Detroit_select['R2']


# In[119]:


Detroit_select


# In[120]:


rTb = requests.get(urlTb, cookies=cookies, headers=headers)
html_contentsTb = rTb.text


# In[121]:


html_soupTb = BeautifulSoup(html_contentsTb, 'html.parser')


# In[122]:


calendarioTb = html_soupTb.find_all('table', class_='Table') 


# In[123]:


Tampa_Bay = pd.DataFrame(columns = TabGen)


# In[124]:


for table in calendarioTb:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Tampa_Bay.loc[len(Tampa_Bay)] = values


# In[125]:


Tampa_Bay.insert(0, 'Equipo', 'Tampa Bay Buccaneers')
Tampa_Bay['Resultado_L'] = Tampa_Bay['Resultado'].str.extract(r'([A-Za-z]+)')
Tampa_Bay['Resultado_Numeros'] = Tampa_Bay['Resultado'].str.extract(r'(\d+-\d+)')
Tampa_Bay[['R1', 'R2']] = Tampa_Bay['Resultado_Numeros'].str.split('-', expand=True)
Tampa_Bay['Local_Visitante'] = Tampa_Bay['Oponente'].str.split().str[0].str.replace('.', '')
Tampa_Bay['Local_Visitante'] = Tampa_Bay['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Tampa_Bay['Equipo_Oponente'] = Tampa_Bay['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Tampa_Bay['G'] = (Tampa_Bay['Resultado_L'] == 'G').astype(int)
Tampa_Bay['P'] = (Tampa_Bay['Resultado_L'] == 'P').astype(int)
Tampa_Bay['E'] = (Tampa_Bay['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Tampa_Bay_select = Tampa_Bay[columnas_deseadas]
Tampa_Bay_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Tampa_Bay_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Tampa_Bay_select = Tampa_Bay_select.copy()
Tampa_Bay_select['Diferencia_Pts.'] = Tampa_Bay_select['R1'] - Tampa_Bay_select['R2']


# In[126]:


Tampa_Bay_select


# In[127]:


rWsh = requests.get(urlWsh, cookies=cookies, headers=headers)
html_contentsWsh = rWsh.text


# In[128]:


html_soupWsh = BeautifulSoup(html_contentsWsh, 'html.parser')


# In[129]:


calendarioWsh = html_soupWsh.find_all('table', class_='Table') 


# In[130]:


Washington = pd.DataFrame(columns = TabGen)


# In[131]:


for table in calendarioWsh:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Washington.loc[len(Washington)] = values


# In[132]:


Washington.insert(0, 'Equipo', 'Washington Commanders')
Washington['Resultado_L'] = Washington['Resultado'].str.extract(r'([A-Za-z]+)')
Washington['Resultado_Numeros'] = Washington['Resultado'].str.extract(r'(\d+-\d+)')
Washington[['R1', 'R2']] = Washington['Resultado_Numeros'].str.split('-', expand=True)
Washington['Local_Visitante'] = Washington['Oponente'].str.split().str[0].str.replace('.', '')
Washington['Local_Visitante'] = Washington['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Washington['Equipo_Oponente'] = Washington['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Washington['G'] = (Washington['Resultado_L'] == 'G').astype(int)
Washington['P'] = (Washington['Resultado_L'] == 'P').astype(int)
Washington['E'] = (Washington['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Washington_select = Washington[columnas_deseadas]
Washington_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Washington_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Washington_select = Washington_select.copy()
Washington_select['Diferencia_Pts.'] = Washington_select['R1'] - Washington_select['R2']


# In[133]:


Washington_select


# In[134]:


rLv = requests.get(urlLv, cookies=cookies, headers=headers)
html_contentsLv = rLv.text


# In[135]:


html_soupLv = BeautifulSoup(html_contentsLv, 'html.parser')


# In[136]:


calendarioLv = html_soupLv.find_all('table', class_='Table') 


# In[137]:


Las_Vegas = pd.DataFrame(columns = TabGen)


# In[138]:


for table in calendarioLv:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Las_Vegas.loc[len(Las_Vegas)] = values


# In[139]:


Las_Vegas.insert(0, 'Equipo', 'Las Vegas Raiders')
Las_Vegas['Resultado_L'] = Las_Vegas['Resultado'].str.extract(r'([A-Za-z]+)')
Las_Vegas['Resultado_Numeros'] = Las_Vegas['Resultado'].str.extract(r'(\d+-\d+)')
Las_Vegas[['R1', 'R2']] = Las_Vegas['Resultado_Numeros'].str.split('-', expand=True)
Las_Vegas['Local_Visitante'] = Las_Vegas['Oponente'].str.split().str[0].str.replace('.', '')
Las_Vegas['Local_Visitante'] = Las_Vegas['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Las_Vegas['Equipo_Oponente'] = Las_Vegas['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Las_Vegas['G'] = (Las_Vegas['Resultado_L'] == 'G').astype(int)
Las_Vegas['P'] = (Las_Vegas['Resultado_L'] == 'P').astype(int)
Las_Vegas['E'] = (Las_Vegas['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Las_Vegas_select = Las_Vegas[columnas_deseadas]
Las_Vegas_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Las_Vegas_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Las_Vegas_select = Las_Vegas_select.copy()
Las_Vegas_select['Diferencia_Pts.'] = Las_Vegas_select['R1'] - Las_Vegas_select['R2']


# In[140]:


Las_Vegas_select


# In[141]:


rNo = requests.get(urlNo, cookies=cookies, headers=headers)
html_contentsNo = rNo.text


# In[142]:


html_soupNo = BeautifulSoup(html_contentsNo, 'html.parser')


# In[143]:


calendarioNo = html_soupNo.find_all('table', class_='Table') 


# In[144]:


New_Orleans = pd.DataFrame(columns = TabGen)


# In[145]:


for table in calendarioNo:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            New_Orleans.loc[len(New_Orleans)] = values


# In[146]:


New_Orleans.insert(0, 'Equipo', 'New Orleans Saints')
New_Orleans['Resultado_L'] = New_Orleans['Resultado'].str.extract(r'([A-Za-z]+)')
New_Orleans['Resultado_Numeros'] = New_Orleans['Resultado'].str.extract(r'(\d+-\d+)')
New_Orleans[['R1', 'R2']] = New_Orleans['Resultado_Numeros'].str.split('-', expand=True)
New_Orleans['Local_Visitante'] = New_Orleans['Oponente'].str.split().str[0].str.replace('.', '')
New_Orleans['Local_Visitante'] = New_Orleans['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
New_Orleans['Equipo_Oponente'] = New_Orleans['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
New_Orleans['G'] = (New_Orleans['Resultado_L'] == 'G').astype(int)
New_Orleans['P'] = (New_Orleans['Resultado_L'] == 'P').astype(int)
New_Orleans['E'] = (New_Orleans['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
New_Orleans_select = New_Orleans[columnas_deseadas]
New_Orleans_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = New_Orleans_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
New_Orleans_select = New_Orleans_select.copy()
New_Orleans_select['Diferencia_Pts.'] = New_Orleans_select['R1'] - New_Orleans_select['R2']


# In[147]:


New_Orleans_select


# In[148]:


rLac= requests.get(urlLac, cookies=cookies, headers=headers)
html_contentsLac = rLac.text


# In[149]:


html_soupLac = BeautifulSoup(html_contentsLac, 'html.parser')


# In[150]:


calendarioLac = html_soupLac.find_all('table', class_='Table') 


# In[151]:


Los_Angeles_Chargers = pd.DataFrame(columns = TabGen)


# In[152]:


for table in calendarioLac:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Los_Angeles_Chargers.loc[len(Los_Angeles_Chargers)] = values


# In[153]:


Los_Angeles_Chargers.insert(0, 'Equipo', 'Los Angeles Chargers')
Los_Angeles_Chargers['Resultado_L'] = Los_Angeles_Chargers['Resultado'].str.extract(r'([A-Za-z]+)')
Los_Angeles_Chargers['Resultado_Numeros'] = Los_Angeles_Chargers['Resultado'].str.extract(r'(\d+-\d+)')
Los_Angeles_Chargers[['R1', 'R2']] = Los_Angeles_Chargers['Resultado_Numeros'].str.split('-', expand=True)
Los_Angeles_Chargers['Local_Visitante'] = Los_Angeles_Chargers['Oponente'].str.split().str[0].str.replace('.', '')
Los_Angeles_Chargers['Local_Visitante'] = Los_Angeles_Chargers['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Los_Angeles_Chargers['Equipo_Oponente'] = Los_Angeles_Chargers['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Los_Angeles_Chargers['G'] = (Los_Angeles_Chargers['Resultado_L'] == 'G').astype(int)
Los_Angeles_Chargers['P'] = (Los_Angeles_Chargers['Resultado_L'] == 'P').astype(int)
Los_Angeles_Chargers['E'] = (Los_Angeles_Chargers['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Los_Angeles_Chargers_select = Los_Angeles_Chargers[columnas_deseadas]
Los_Angeles_Chargers_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Los_Angeles_Chargers_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Los_Angeles_Chargers_select = Los_Angeles_Chargers_select.copy()
Los_Angeles_Chargers_select['Diferencia_Pts.'] = Los_Angeles_Chargers_select['R1'] - Los_Angeles_Chargers_select['R2']


# In[154]:


Los_Angeles_Chargers_select


# In[155]:


rInd = requests.get(urlInd, cookies=cookies, headers=headers)
html_contentsInd = rInd.text


# In[156]:


html_soupInd = BeautifulSoup(html_contentsInd, 'html.parser')


# In[157]:


calendarioInd = html_soupInd.find_all('table', class_='Table') 


# In[158]:


Indianapolis = pd.DataFrame(columns = TabGen)


# In[159]:


for table in calendarioInd:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Indianapolis.loc[len(Indianapolis)] = values


# In[160]:


Indianapolis.insert(0, 'Equipo', 'Indianapolis Colts')
Indianapolis['Resultado_L'] = Indianapolis['Resultado'].str.extract(r'([A-Za-z]+)')
Indianapolis['Resultado_Numeros'] = Indianapolis['Resultado'].str.extract(r'(\d+-\d+)')
Indianapolis[['R1', 'R2']] = Indianapolis['Resultado_Numeros'].str.split('-', expand=True)
Indianapolis['Local_Visitante'] = Indianapolis['Oponente'].str.split().str[0].str.replace('.', '')
Indianapolis['Local_Visitante'] = Indianapolis['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Indianapolis['Equipo_Oponente'] = Indianapolis['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Indianapolis['G'] = (Indianapolis['Resultado_L'] == 'G').astype(int)
Indianapolis['P'] = (Indianapolis['Resultado_L'] == 'P').astype(int)
Indianapolis['E'] = (Indianapolis['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Indianapolis_select = Indianapolis[columnas_deseadas]
Indianapolis_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Indianapolis_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Indianapolis_select = Indianapolis_select.copy()
Indianapolis_select['Diferencia_Pts.'] = Indianapolis_select['R1'] - Indianapolis_select['R2']


# In[161]:


Indianapolis_select


# In[162]:


rChi = requests.get(urlChi, cookies=cookies, headers=headers)
html_contentsChi = rChi.text


# In[163]:


html_soupChi = BeautifulSoup(html_contentsChi, 'html.parser')


# In[164]:


calendarioChi = html_soupChi.find_all('table', class_='Table') 


# In[165]:


Chicago = pd.DataFrame(columns = TabGen)


# In[166]:


for table in calendarioChi:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Chicago.loc[len(Chicago)] = values


# In[167]:


Chicago.insert(0, 'Equipo', 'Chicago Bears')
Chicago['Resultado_L'] = Chicago['Resultado'].str.extract(r'([A-Za-z]+)')
Chicago['Resultado_Numeros'] = Chicago['Resultado'].str.extract(r'(\d+-\d+)')
Chicago[['R1', 'R2']] = Chicago['Resultado_Numeros'].str.split('-', expand=True)
Chicago['Local_Visitante'] = Chicago['Oponente'].str.split().str[0].str.replace('.', '')
Chicago['Local_Visitante'] = Chicago['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Chicago['Equipo_Oponente'] = Chicago['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Chicago['G'] = (Chicago['Resultado_L'] == 'G').astype(int)
Chicago['P'] = (Chicago['Resultado_L'] == 'P').astype(int)
Chicago['E'] = (Chicago['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Chicago_select = Chicago[columnas_deseadas]
Chicago_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Chicago_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Chicago_select = Chicago_select.copy()
Chicago_select['Diferencia_Pts.'] = Chicago_select['R1'] - Chicago_select['R2']


# In[168]:


Chicago_select


# In[169]:


rKc = requests.get(urlKc, cookies=cookies, headers=headers)
html_contentsKc = rKc.text


# In[170]:


html_soupKc = BeautifulSoup(html_contentsKc, 'html.parser')


# In[171]:


calendarioKc = html_soupKc.find_all('table', class_='Table') 


# In[172]:


Kansas_City = pd.DataFrame(columns = TabGen)


# In[173]:


for table in calendarioKc:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Kansas_City.loc[len(Kansas_City)] = values


# In[174]:


Kansas_City.insert(0, 'Equipo', 'Kansas City Chiefs')
Kansas_City['Resultado_L'] = Kansas_City['Resultado'].str.extract(r'([A-Za-z]+)')
Kansas_City['Resultado_Numeros'] = Kansas_City['Resultado'].str.extract(r'(\d+-\d+)')
Kansas_City[['R1', 'R2']] = Kansas_City['Resultado_Numeros'].str.split('-', expand=True)
Kansas_City['Local_Visitante'] = Kansas_City['Oponente'].str.split().str[0].str.replace('.', '')
Kansas_City['Local_Visitante'] = Kansas_City['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Kansas_City['Equipo_Oponente'] = Kansas_City['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Kansas_City['G'] = (Kansas_City['Resultado_L'] == 'G').astype(int)
Kansas_City['P'] = (Kansas_City['Resultado_L'] == 'P').astype(int)
Kansas_City['E'] = (Kansas_City['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Kansas_City_select = Kansas_City[columnas_deseadas]
Kansas_City_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Kansas_City_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Kansas_City_select = Kansas_City_select.copy()
Kansas_City_select['Diferencia_Pts.'] = Kansas_City_select['R1'] - Kansas_City_select['R2']


# In[175]:


Kansas_City_select


# In[176]:


rNe = requests.get(urlNe, cookies=cookies, headers=headers)
html_contentsNe = rNe.text


# In[177]:


html_soupNe = BeautifulSoup(html_contentsNe, 'html.parser')


# In[178]:


calendarioNe = html_soupNe.find_all('table', class_='Table') 


# In[179]:


New_England  = pd.DataFrame(columns = TabGen)


# In[180]:


for table in calendarioNe:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            New_England.loc[len(New_England)] = values


# In[181]:


New_England.insert(0, 'Equipo', 'New England Patriots')
New_England['Resultado_L'] = New_England['Resultado'].str.extract(r'([A-Za-z]+)')
New_England['Resultado_Numeros'] = New_England['Resultado'].str.extract(r'(\d+-\d+)')
New_England[['R1', 'R2']] = New_England['Resultado_Numeros'].str.split('-', expand=True)
New_England['Local_Visitante'] = New_England['Oponente'].str.split().str[0].str.replace('.', '')
New_England['Local_Visitante'] = New_England['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
New_England['Equipo_Oponente'] = New_England['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
New_England['G'] = (New_England['Resultado_L'] == 'G').astype(int)
New_England['P'] = (New_England['Resultado_L'] == 'P').astype(int)
New_England['E'] = (New_England['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
New_England_select = New_England[columnas_deseadas]
New_England_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = New_England_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
New_England_select = New_England_select.copy()
New_England_select['Diferencia_Pts.'] = New_England_select['R1'] - New_England_select['R2']


# In[182]:


New_England_select


# In[183]:


rMin = requests.get(urlMin, cookies=cookies, headers=headers)
html_contentsMin = rMin.text


# In[184]:


html_soupMin = BeautifulSoup(html_contentsMin, 'html.parser')


# In[185]:


calendarioMin = html_soupMin.find_all('table', class_='Table') 


# In[186]:


Minnesota  = pd.DataFrame(columns = TabGen)


# In[187]:


for table in calendarioMin:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Minnesota.loc[len(Minnesota)] = values


# In[188]:


Minnesota.insert(0, 'Equipo', 'Minnesota Vikings')
Minnesota['Resultado_L'] = Minnesota['Resultado'].str.extract(r'([A-Za-z]+)')
Minnesota['Resultado_Numeros'] = Minnesota['Resultado'].str.extract(r'(\d+-\d+)')
Minnesota[['R1', 'R2']] = Minnesota['Resultado_Numeros'].str.split('-', expand=True)
Minnesota['Local_Visitante'] = Minnesota['Oponente'].str.split().str[0].str.replace('.', '')
Minnesota['Local_Visitante'] = Minnesota['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Minnesota['Equipo_Oponente'] = Minnesota['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Minnesota['G'] = (Minnesota['Resultado_L'] == 'G').astype(int)
Minnesota['P'] = (Minnesota['Resultado_L'] == 'P').astype(int)
Minnesota['E'] = (Minnesota['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Minnesota_select = Minnesota[columnas_deseadas]
Minnesota_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Minnesota_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Minnesota_select = Minnesota_select.copy()
Minnesota_select['Diferencia_Pts.'] = Minnesota_select['R1'] - Minnesota_select['R2']


# In[189]:


Minnesota_select


# In[190]:


rAri = requests.get(urlAri, cookies=cookies, headers=headers)
html_contentsAri = rAri.text


# In[191]:


html_soupAri = BeautifulSoup(html_contentsAri, 'html.parser')


# In[192]:


calendarioAri = html_soupAri.find_all('table', class_='Table') 


# In[193]:


Arizona  = pd.DataFrame(columns = TabGen)


# In[194]:


for table in calendarioAri:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Arizona.loc[len(Arizona)] = values


# In[195]:


Arizona.insert(0, 'Equipo', 'Arizona Cardinals')
Arizona['Resultado_L'] = Arizona['Resultado'].str.extract(r'([A-Za-z]+)')
Arizona['Resultado_Numeros'] = Arizona['Resultado'].str.extract(r'(\d+-\d+)')
Arizona[['R1', 'R2']] = Arizona['Resultado_Numeros'].str.split('-', expand=True)
Arizona['Local_Visitante'] = Arizona['Oponente'].str.split().str[0].str.replace('.', '')
Arizona['Local_Visitante'] = Arizona['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Arizona['Equipo_Oponente'] = Arizona['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Arizona['G'] = (Arizona['Resultado_L'] == 'G').astype(int)
Arizona['P'] = (Arizona['Resultado_L'] == 'P').astype(int)
Arizona['E'] = (Arizona['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Arizona_select = Arizona[columnas_deseadas]
Arizona_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Arizona_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Arizona_select = Arizona_select.copy()
Arizona_select['Diferencia_Pts.'] = Arizona_select['R1'] - Arizona_select['R2']


# In[196]:


Arizona_select


# In[197]:


rBuf = requests.get(urlBuf, cookies=cookies, headers=headers)
html_contentsBuf = rBuf.text


# In[198]:


html_soupBuf = BeautifulSoup(html_contentsBuf, 'html.parser')


# In[199]:


calendarioBuf = html_soupBuf.find_all('table', class_='Table') 


# In[200]:


Buffalo  = pd.DataFrame(columns = TabGen)


# In[201]:


for table in calendarioBuf:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Buffalo.loc[len(Buffalo)] = values


# In[202]:


Buffalo.insert(0, 'Equipo', 'Buffalo Bills')
Buffalo['Resultado_L'] = Buffalo['Resultado'].str.extract(r'([A-Za-z]+)')
Buffalo['Resultado_Numeros'] = Buffalo['Resultado'].str.extract(r'(\d+-\d+)')
Buffalo[['R1', 'R2']] = Buffalo['Resultado_Numeros'].str.split('-', expand=True)
Buffalo['Local_Visitante'] = Buffalo['Oponente'].str.split().str[0].str.replace('.', '')
Buffalo['Local_Visitante'] = Buffalo['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Buffalo['Equipo_Oponente'] = Buffalo['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Buffalo['G'] = (Buffalo['Resultado_L'] == 'G').astype(int)
Buffalo['P'] = (Buffalo['Resultado_L'] == 'P').astype(int)
Buffalo['E'] = (Buffalo['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Buffalo_select = Buffalo[columnas_deseadas]
Buffalo_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Buffalo_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Buffalo_select = Buffalo_select.copy()
Buffalo_select['Diferencia_Pts.'] = Buffalo_select['R1'] - Buffalo_select['R2']


# In[203]:


Buffalo_select


# In[204]:


rDen = requests.get(urlDen, cookies=cookies, headers=headers)
html_contentsDen = rDen.text


# In[205]:


html_soupDen = BeautifulSoup(html_contentsDen, 'html.parser')


# In[206]:


calendarioDen = html_soupDen.find_all('table', class_='Table') 


# In[207]:


Denver  = pd.DataFrame(columns = TabGen)


# In[208]:


for table in calendarioDen:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Denver.loc[len(Denver)] = values


# In[209]:


Denver.insert(0, 'Equipo', 'Denver Broncos')
Denver['Resultado_L'] = Denver['Resultado'].str.extract(r'([A-Za-z]+)')
Denver['Resultado_Numeros'] = Denver['Resultado'].str.extract(r'(\d+-\d+)')
Denver[['R1', 'R2']] = Denver['Resultado_Numeros'].str.split('-', expand=True)
Denver['Local_Visitante'] = Denver['Oponente'].str.split().str[0].str.replace('.', '')
Denver['Local_Visitante'] = Denver['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Denver['Equipo_Oponente'] = Denver['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Denver['G'] = (Denver['Resultado_L'] == 'G').astype(int)
Denver['P'] = (Denver['Resultado_L'] == 'P').astype(int)
Denver['E'] = (Denver['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Denver_select = Denver[columnas_deseadas]
Denver_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Denver_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Denver_select = Denver_select.copy()
Denver_select['Diferencia_Pts.'] = Denver_select['R1'] - Denver_select['R2']


# In[210]:


Denver_select


# In[211]:


rTen = requests.get(urlTen, cookies=cookies, headers=headers)
html_contentsTen = rTen.text


# In[212]:


html_soupTen = BeautifulSoup(html_contentsTen, 'html.parser')


# In[213]:


calendarioTen = html_soupTen.find_all('table', class_='Table') 


# In[214]:


Tennessee  = pd.DataFrame(columns = TabGen)


# In[215]:


for table in calendarioTen:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Tennessee.loc[len(Tennessee)] = values


# In[216]:


Tennessee.insert(0, 'Equipo', 'Tennessee Titans')
Tennessee['Resultado_L'] = Tennessee['Resultado'].str.extract(r'([A-Za-z]+)')
Tennessee['Resultado_Numeros'] = Tennessee['Resultado'].str.extract(r'(\d+-\d+)')
Tennessee[['R1', 'R2']] = Tennessee['Resultado_Numeros'].str.split('-', expand=True)
Tennessee['Local_Visitante'] = Tennessee['Oponente'].str.split().str[0].str.replace('.', '')
Tennessee['Local_Visitante'] = Tennessee['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Tennessee['Equipo_Oponente'] = Tennessee['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Tennessee['G'] = (Tennessee['Resultado_L'] == 'G').astype(int)
Tennessee['P'] = (Tennessee['Resultado_L'] == 'P').astype(int)
Tennessee['E'] = (Tennessee['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Tennessee_select = Tennessee[columnas_deseadas]
Tennessee_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Tennessee_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Tennessee_select = Tennessee_select.copy()
Tennessee_select['Diferencia_Pts.'] = Tennessee_select['R1'] - Tennessee_select['R2']


# In[217]:


Tennessee_select


# In[218]:


rSea = requests.get(urlSea, cookies=cookies, headers=headers)
html_contentsSea = rSea.text


# In[219]:


html_soupSea = BeautifulSoup(html_contentsSea, 'html.parser')


# In[220]:


calendarioSea = html_soupSea.find_all('table', class_='Table') 


# In[221]:


Seattle  = pd.DataFrame(columns = TabGen)


# In[222]:


for table in calendarioSea:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Seattle.loc[len(Seattle)] = values


# In[223]:


Seattle.insert(0, 'Equipo', 'Seattle Seahawks')
Seattle['Resultado_L'] = Seattle['Resultado'].str.extract(r'([A-Za-z]+)')
Seattle['Resultado_Numeros'] = Seattle['Resultado'].str.extract(r'(\d+-\d+)')
Seattle[['R1', 'R2']] = Seattle['Resultado_Numeros'].str.split('-', expand=True)
Seattle['Local_Visitante'] = Seattle['Oponente'].str.split().str[0].str.replace('.', '')
Seattle['Local_Visitante'] = Seattle['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Seattle['Equipo_Oponente'] = Seattle['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Seattle['G'] = (Seattle['Resultado_L'] == 'G').astype(int)
Seattle['P'] = (Seattle['Resultado_L'] == 'P').astype(int)
Seattle['E'] = (Seattle['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Seattle_select = Seattle[columnas_deseadas]
Seattle_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Seattle_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Seattle_select = Seattle_select.copy()
Seattle_select['Diferencia_Pts.'] = Seattle_select['R1'] - Seattle_select['R2']


# In[224]:


Seattle_select


# In[225]:


rCar = requests.get(urlCar, cookies=cookies, headers=headers)
html_contentsCar = rCar.text


# In[226]:


html_soupCar = BeautifulSoup(html_contentsCar, 'html.parser')


# In[227]:


calendarioCar = html_soupCar.find_all('table', class_='Table') 


# In[228]:


Carolina   = pd.DataFrame(columns = TabGen)


# In[229]:


for table in calendarioCar:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Carolina.loc[len(Carolina)] = values


# In[230]:


Carolina.insert(0, 'Equipo', 'Carolina Panthers')
Carolina['Resultado_L'] = Carolina['Resultado'].str.extract(r'([A-Za-z]+)')
Carolina['Resultado_Numeros'] = Carolina['Resultado'].str.extract(r'(\d+-\d+)')
Carolina[['R1', 'R2']] = Carolina['Resultado_Numeros'].str.split('-', expand=True)
Carolina['Local_Visitante'] = Carolina['Oponente'].str.split().str[0].str.replace('.', '')
Carolina['Local_Visitante'] = Carolina['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Carolina['Equipo_Oponente'] = Carolina['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Carolina['G'] = (Carolina['Resultado_L'] == 'G').astype(int)
Carolina['P'] = (Carolina['Resultado_L'] == 'P').astype(int)
Carolina['E'] = (Carolina['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Carolina_select = Carolina[columnas_deseadas]
Carolina_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Carolina_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Carolina_select = Carolina_select.copy()
Carolina_select['Diferencia_Pts.'] = Carolina_select['R1'] - Carolina_select['R2']


# In[231]:


Carolina_select


# In[232]:


rHou = requests.get(urlHou, cookies=cookies, headers=headers)
html_contentsHou = rHou.text


# In[233]:


html_soupHou = BeautifulSoup(html_contentsHou, 'html.parser')


# In[234]:


calendarioHou = html_soupHou.find_all('table', class_='Table') 


# In[235]:


Houston = pd.DataFrame(columns = TabGen)


# In[236]:


for table in calendarioHou:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Houston.loc[len(Houston)] = values


# In[237]:


Houston.insert(0, 'Equipo', 'Houston Texans')
Houston['Resultado_L'] = Houston['Resultado'].str.extract(r'([A-Za-z]+)')
Houston['Resultado_Numeros'] = Houston['Resultado'].str.extract(r'(\d+-\d+)')
Houston[['R1', 'R2']] = Houston['Resultado_Numeros'].str.split('-', expand=True)
Houston['Local_Visitante'] = Houston['Oponente'].str.split().str[0].str.replace('.', '')
Houston['Local_Visitante'] = Houston['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Houston['Equipo_Oponente'] = Houston['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Houston['G'] = (Houston['Resultado_L'] == 'G').astype(int)
Houston['P'] = (Houston['Resultado_L'] == 'P').astype(int)
Houston['E'] = (Houston['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Houston_select = Houston[columnas_deseadas]
Houston_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Houston_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Houston_select = Houston_select.copy()
Houston_select['Diferencia_Pts.'] = Houston_select['R1'] - Houston_select['R2']


# In[238]:


Houston_select


# In[239]:


rPit = requests.get(urlPit, cookies=cookies, headers=headers)
html_contentsPit = rPit.text


# In[240]:


html_soupPit = BeautifulSoup(html_contentsPit, 'html.parser')


# In[241]:


calendarioPit = html_soupPit.find_all('table', class_='Table') 


# In[242]:


Pittsburgh  = pd.DataFrame(columns = TabGen)


# In[243]:


for table in calendarioPit:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Pittsburgh.loc[len(Pittsburgh)] = values


# In[244]:


Pittsburgh.insert(0, 'Equipo', 'Pittsburgh Steelers')
Pittsburgh['Resultado_L'] = Pittsburgh['Resultado'].str.extract(r'([A-Za-z]+)')
Pittsburgh['Resultado_Numeros'] = Pittsburgh['Resultado'].str.extract(r'(\d+-\d+)')
Pittsburgh[['R1', 'R2']] = Pittsburgh['Resultado_Numeros'].str.split('-', expand=True)
Pittsburgh['Local_Visitante'] = Pittsburgh['Oponente'].str.split().str[0].str.replace('.', '')
Pittsburgh['Local_Visitante'] = Pittsburgh['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Pittsburgh['Equipo_Oponente'] = Pittsburgh['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Pittsburgh['G'] = (Pittsburgh['Resultado_L'] == 'G').astype(int)
Pittsburgh['P'] = (Pittsburgh['Resultado_L'] == 'P').astype(int)
Pittsburgh['E'] = (Pittsburgh['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Pittsburgh_select = Pittsburgh[columnas_deseadas]
Pittsburgh_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Pittsburgh_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Pittsburgh_select = Pittsburgh_select.copy()
Pittsburgh_select['Diferencia_Pts.'] = Pittsburgh_select['R1'] - Pittsburgh_select['R2']


# In[245]:


Pittsburgh_select


# In[246]:


rCin = requests.get(urlCin, cookies=cookies, headers=headers)
html_contentsCin = rCin.text


# In[247]:


html_soupCin = BeautifulSoup(html_contentsCin, 'html.parser')


# In[248]:


calendarioCin = html_soupCin.find_all('table', class_='Table') 


# In[249]:


Cincinnati = pd.DataFrame(columns = TabGen)


# In[250]:


for table in calendarioCin:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            Cincinnati.loc[len(Cincinnati)] = values


# In[251]:


Cincinnati.insert(0, 'Equipo', 'Cincinnati Bengals')
Cincinnati['Resultado_L'] = Cincinnati['Resultado'].str.extract(r'([A-Za-z]+)')
Cincinnati['Resultado_Numeros'] = Cincinnati['Resultado'].str.extract(r'(\d+-\d+)')
Cincinnati[['R1', 'R2']] = Cincinnati['Resultado_Numeros'].str.split('-', expand=True)
Cincinnati['Local_Visitante'] = Cincinnati['Oponente'].str.split().str[0].str.replace('.', '')
Cincinnati['Local_Visitante'] = Cincinnati['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
Cincinnati['Equipo_Oponente'] = Cincinnati['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
Cincinnati['G'] = (Cincinnati['Resultado_L'] == 'G').astype(int)
Cincinnati['P'] = (Cincinnati['Resultado_L'] == 'P').astype(int)
Cincinnati['E'] = (Cincinnati['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
Cincinnati_select = Cincinnati[columnas_deseadas]
Cincinnati_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = Cincinnati_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
Cincinnati_select = Cincinnati_select.copy()
Cincinnati_select['Diferencia_Pts.'] = Cincinnati_select['R1'] - Cincinnati_select['R2']


# In[252]:


Cincinnati_select


# In[253]:


rNyg = requests.get(urlNyg, cookies=cookies, headers=headers)
html_contentsNyg = rNyg.text


# In[254]:


html_soupNyg = BeautifulSoup(html_contentsNyg, 'html.parser')


# In[255]:


calendarioNyg = html_soupNyg.find_all('table', class_='Table') 


# In[256]:


New_York_Giants = pd.DataFrame(columns = TabGen)


# In[257]:


for table in calendarioNyg:
    for row in table.find_all('tr')[2:21]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(TabGen):
            New_York_Giants.loc[len(New_York_Giants)] = values


# In[258]:


New_York_Giants


# In[259]:


New_York_Giants.insert(0, 'Equipo', 'New York Giants')
New_York_Giants['Resultado_L'] = New_York_Giants['Resultado'].str.extract(r'([A-Za-z]+)')
New_York_Giants['Resultado_Numeros'] = New_York_Giants['Resultado'].str.extract(r'(\d+-\d+)')
New_York_Giants[['R1', 'R2']] = New_York_Giants['Resultado_Numeros'].str.split('-', expand=True)
New_York_Giants['Local_Visitante'] = New_York_Giants['Oponente'].str.split().str[0].str.replace('.', '')
New_York_Giants['Local_Visitante'] = New_York_Giants['Local_Visitante'].str.replace('vs', 'local').str.replace('en', 'visitante')
New_York_Giants['Equipo_Oponente'] = New_York_Giants['Oponente'].str.extract(r'(vs\.|en\s)([^,]+)')[1]
# Agregar las columnas "G," "P," y "E" basadas en la columna "Resultado_L"
New_York_Giants['G'] = (New_York_Giants['Resultado_L'] == 'G').astype(int)
New_York_Giants['P'] = (New_York_Giants['Resultado_L'] == 'P').astype(int)
New_York_Giants['E'] = (New_York_Giants['Resultado_L'] == 'E').astype(int)
columnas_deseadas = ['Equipo', 'Semana', 'Fecha', 'Resultado_L', 'R1', 'R2', 'Local_Visitante', 'Equipo_Oponente', 'G', 'P', 'E']
New_York_Giants_select = New_York_Giants[columnas_deseadas]
New_York_Giants_select.loc[:, ['Semana', 'R1', 'R2', 'G', 'P', 'E']] = New_York_Giants_select[['Semana', 'R1', 'R2', 'G', 'P', 'E']].astype(int)
New_York_Giants_select = New_York_Giants_select.copy()
New_York_Giants_select['Diferencia_Pts.'] = New_York_Giants_select['R1'] - New_York_Giants_select['R2']



# In[260]:


New_York_Giants_select


# In[ ]:





# # Pocisiones

# In[261]:


urlp = "https://www.espn.com.mx/futbol-americano/nfl/posiciones/_/grupo/liga"


# In[262]:


rp = requests.get(urlp, cookies=cookies, headers=headers)
html_contentsp = rp.text


# In[263]:


html_soupp = BeautifulSoup(html_contentsp, 'html.parser')


# In[264]:


tabla_puntajep = html_soupp.find_all('table', class_='Table Table--align-right') 


# In[265]:


# Encuentra todos los elementos span con la clase hide-mobile
elementos_equipo = html_soupp.find_all('span', class_='hide-mobile')
# Inicializa una lista para almacenar los nombres de los equipos
nombres_equipos = []
# Itera sobre los elementos y obtén el texto de cada uno
for elemento_equipo in elementos_equipo:
    nombre_equipo = elemento_equipo.text
    nombres_equipos.append(nombre_equipo)
# Ahora, nombres_equipos contendrá los nombres de todos los equipos
# Crea un DataFrame con una columna llamada 'Nombre_Equipo'
nom = pd.DataFrame({'Equipo': nombres_equipos})

# Si deseas agregar un índice numérico, puedes hacerlo así:
nom.index = range(1, len(nom) + 1)  # Índice de 1 a n (número de equipos)


# In[266]:


columnaspos =  ['G','P','E','PCT','LOCAL',
             'VIS','DIV','CONF','PA','PC',
             'DIFP','R']


# In[267]:


pos = pd.DataFrame(columns = columnaspos)


# In[268]:


for table in tabla_puntajep:
    for row in table.find_all('tr')[1:]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(columnaspos):
            pos.loc[len(pos)] = values


# In[269]:


pos.index = range(1, len(pos) + 1)  # Índice de 1 a n (número de equipos)


# In[270]:


resultadopos = pd.concat([nom, pos ], axis=1)


# In[271]:


resultadopos


# # Base de Datos

# In[68]:


conexion1 = psycopg2.connect(database="Nfl", user="postgres", password="Edgar821")
cursor1 = conexion1.cursor()


# # Consular Semana 
# 

# In[69]:


cursor1.execute("SELECT max(semana) from calendario")


# In[70]:


resultados = cursor1.fetchall()


# In[71]:


semana_siguiente = resultados[0][0]+1


# In[72]:


semana_siguiente


# In[277]:


week_siguiente_DAL = Dallas_select[Dallas_select['Semana'] == semana_siguiente]
week_siguiente_MIA = Miami_select[Miami_select['Semana'] == semana_siguiente]
week_siguiente_SF = San_Francisco_select[San_Francisco_select['Semana'] == semana_siguiente]
week_siguiente_BAL = Baltimore_Ravens_select[Baltimore_Ravens_select['Semana'] == semana_siguiente]
week_siguiente_ATL = Atlanta_select[Atlanta_select['Semana'] == semana_siguiente]
week_siguiente_NO = New_Orleans_select[New_Orleans_select['Semana'] == semana_siguiente]
week_siguiente_TB = Tampa_Bay_select[Tampa_Bay_select['Semana'] == semana_siguiente]
week_siguiente_PHI = Philadelphia_select[Philadelphia_select['Semana'] == semana_siguiente]
week_siguiente_WSH = Washington_select[Washington_select['Semana'] == semana_siguiente]
week_siguiente_JAX = Jacksonville_select[Jacksonville_select['Semana'] == semana_siguiente]
week_siguiente_GB = Green_Bay_select[Green_Bay_select['Semana'] == semana_siguiente]
week_siguiente_LV = Las_Vegas_select[Las_Vegas_select['Semana'] == semana_siguiente]
week_siguiente_PIT = Pittsburgh_select[Pittsburgh_select['Semana'] == semana_siguiente]
week_siguiente_NYJ = New_York_Jets_select[New_York_Jets_select['Semana'] == semana_siguiente]
week_siguiente_KC = Kansas_City_select[Kansas_City_select['Semana'] == semana_siguiente]
week_siguiente_BUF = Buffalo_select[Buffalo_select['Semana'] == semana_siguiente]
week_siguiente_IND = Indianapolis_select[Indianapolis_select['Semana'] == semana_siguiente]
week_siguiente_LAR = Los_Angeles_Rams_select[Los_Angeles_Rams_select['Semana'] == semana_siguiente]
week_siguiente_TEN = Tennessee_select[Tennessee_select['Semana'] == semana_siguiente]
week_siguiente_SEA = Seattle_select[Seattle_select['Semana'] == semana_siguiente]
week_siguiente_CLE = Cleveland_select[Cleveland_select['Semana'] == semana_siguiente]
week_siguiente_NYG = New_York_Giants_select[New_York_Giants_select['Semana'] == semana_siguiente]
week_siguiente_DET = Detroit_select[Detroit_select['Semana'] == semana_siguiente]
week_siguiente_NE = New_England_select[New_England_select['Semana'] == semana_siguiente]
week_siguiente_MIN = Minnesota_select[Minnesota_select['Semana'] == semana_siguiente]
week_siguiente_LAC = Los_Angeles_Chargers_select[Los_Angeles_Chargers_select['Semana'] == semana_siguiente]
week_siguiente_CAR = Carolina_select[Carolina_select['Semana'] == semana_siguiente]
week_siguiente_HOU = Houston_select[Houston_select['Semana'] == semana_siguiente]
week_siguiente_CIN = Cincinnati_select[Cincinnati_select['Semana'] == semana_siguiente]
week_siguiente_ARI = Arizona_select[Arizona_select['Semana'] == semana_siguiente]
week_siguiente_CHI = Chicago_select[Chicago_select['Semana'] == semana_siguiente]
week_siguiente_DEN = Denver_select[Denver_select['Semana'] == semana_siguiente]



# Crear un nuevo DataFrame que contenga solo la semana 1 de ambas tablas
week_siguiente_df = pd.concat([week_siguiente_DAL, week_siguiente_MIA, week_siguiente_SF, week_siguiente_BAL, week_siguiente_ATL, week_siguiente_NO,
                               week_siguiente_TB, week_siguiente_PHI, week_siguiente_WSH, week_siguiente_JAX,week_siguiente_GB, week_siguiente_LV, 
                               week_siguiente_PIT, week_siguiente_NYJ, week_siguiente_KC, week_siguiente_BUF, week_siguiente_IND, week_siguiente_LAR, 
                               week_siguiente_TEN, week_siguiente_SEA, week_siguiente_CLE, week_siguiente_NYG, week_siguiente_DET, week_siguiente_NE, 
                               week_siguiente_MIN, week_siguiente_LAC, week_siguiente_CAR, week_siguiente_HOU, week_siguiente_CIN, week_siguiente_ARI, 
                               week_siguiente_CHI, week_siguiente_DEN], ignore_index=True)


# In[278]:


week_siguiente_df


# In[279]:


Div = pd.read_excel("Export/NombresNFL.xlsx")
columnas_deseadas = ['Equipo', 'PCT', 'PA', 'PC', 'DIFP', 'R']
resultadopos_select = resultadopos[columnas_deseadas]
df_possem = pd.merge(week_siguiente_df, resultadopos_select, on='Equipo', how='inner')
df_mergedsem = pd.merge(df_possem, Div, on='Equipo', how='inner')
df_mergedsem


# In[280]:


try:
    for index, row in df_mergedsem.iterrows():
        cursor1.execute(
            "INSERT INTO calendario (Equipo, Semana, Fecha, Resultado_L, R1, R2, Local_Visitante, Equipo_Oponente, G, P, E, Diferencia_Pts, PCT, PA, PC, DIFP, R, Nombre_Abreviado, Divisiones) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row['Equipo'], int(row['Semana']), row['Fecha'], row['Resultado_L'], int(row['R1']), int(row['R2']),
             row['Local_Visitante'], row['Equipo_Oponente'], int(row['G']), int(row['P']), int(row['E']), int(row['Diferencia_Pts.']),float(row['PCT']), 
             int(row['PA']), int(row['PC']), int(row['DIFP']), row['R'], row['Nombre_Abreviado'], row['Divisiones'])
        )



    
    # Confirmar la transacción
    conexion1.commit()
    
except Exception as e:
    print(f"Error: {e}")
    # Realizar un rollback en caso de error
    conexion1.rollback()

finally:
    cursor1.close()
    conexion1.close()


# # Ofensiva 

# In[297]:


# Especifica la ubicación del controlador de Chrome (chromedriver.exe)
chromedriver_pathoff = 'chromedriver.exe'

# Configura el servicio de Chrome con el argumento executable_path
chrome_serviceoff = ChromeService(executable_path=chromedriver_pathoff)

# Crea una instancia del navegador Chrome con el servicio configurado
driveroff = webdriver.Chrome(service=chrome_serviceoff)

# Abre la página web
urloff = 'https://www.espn.com.mx/futbol-americano/nfl/estadisticas/equipo'
driveroff.get(urloff)

# Espera a que la tabla esté presente en la página
wait = WebDriverWait(driveroff, 10)
tabla_presenteoff = EC.presence_of_element_located((By.CSS_SELECTOR, '.Table.Table--align-right.Table--fixed.Table--fixed-left'))
tablaoff = wait.until(tabla_presenteoff)

# Obtén el contenido HTML de la tabla
tabla_htmloff = tablaoff.get_attribute('outerHTML')

# Utiliza BeautifulSoup para analizar el contenido HTML
soupoff = BeautifulSoup(tabla_htmloff, 'html.parser')

# Encuentra todas las filas de la tabla
filasoff = soupoff.find_all('tr')

# Inicializa una lista para almacenar los datos
datosoff = []

# Recorre las filas y obtén los datos de cada celda
for fila in filasoff:
    celdas = fila.find_all('td')
    if celdas:  # Verifica si hay al menos una celda de datos en la fila
        fila_datos = [celda.text.strip() for celda in celdas]
        datosoff.append(fila_datos)

# Crea un DataFrame de Pandas con los datos filtrados
columnasoff = ['Equipo']  # Reemplaza con el nombre de tu columna
dfoff = pd.DataFrame(datosoff, columns=columnasoff)


# Cierra el navegador
driveroff.quit()


# In[298]:


roff = requests.get(urloff, cookies=cookies, headers=headers)
html_contentsoff = roff.text


# In[299]:


html_soupoff = BeautifulSoup(html_contentsoff, 'html.parser')


# In[300]:


tabla_puntajeoff = html_soupoff.find_all('table', class_='Table Table--align-right') 


# In[301]:


columnasoff =  ['GP','YDS','YDS/G','YDS1','YDS/G',
             'YDS2','YDS/G','PTS','PTS/G',]


# In[302]:


infoff = pd.DataFrame(columns = columnasoff)


# In[303]:


for table in tabla_puntajeoff:
    for row in table.find_all('tr')[2:]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(columnasoff):
            infoff.loc[len(infoff)] = values


# In[304]:


dfoff.insert(0, 'Semana', semana_siguiente)
dfoff.insert(1, 'RK', range(1, 33, 1))
columnsUnidoff = pd.concat([dfoff,infoff], axis=1)


# In[305]:


columnas_deseadasoff = ['Semana','RK','Equipo','GP','YDS']
Off_select = columnsUnidoff[columnas_deseadasoff]
Off_select


# In[311]:


try:
    for index, row in Off_select.iterrows():
        cursor1.execute(
            "INSERT INTO offencive (Semana, RK, Equipo, GP, YDS) "
            "VALUES (%s, %s, %s, %s, %s)",
            (int(row['Semana']), int(row['RK']), row['Equipo'], int(row['GP'].replace(',', '')), int(row['YDS'].replace(',', '')))
        )
        conexion1.commit()

except Exception as e:
    print(f"Error: {e}")
    # Rollback en caso de error
    conexion1.rollback()

finally:
    # Cierre del cursor fuera del bucle
    cursor1.close()

# Cierre de la conexión fuera del bucle de iteración
conexion1.close()


# In[367]:


Off_select.to_excel('Export\\OFENRensemana11ESPN.xlsx') 


# # Defensiva

# In[313]:


# Especifica la ubicación del controlador de Chrome (chromedriver.exe)
chromedriver_path = 'chromedriver.exe'

# Configura el servicio de Chrome con el argumento executable_path
chrome_service = ChromeService(executable_path=chromedriver_path)

# Crea una instancia del navegador Chrome con el servicio configurado
driver = webdriver.Chrome(service=chrome_service)

# Abre la página web
urldeff = 'https://www.espn.com.mx/futbol-americano/nfl/estadisticas/equipo/_/vista/defensiva'
driver.get(urldeff)

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
    if celdas:  # Verifica si hay al menos una celda de datos en la fila
        fila_datos = [celda.text.strip() for celda in celdas]
        datos.append(fila_datos)

# Crea un DataFrame de Pandas con los datos filtrados
columnas = ['Equipo']  # Reemplaza con el nombre de tu columna
dfdeff = pd.DataFrame(datos, columns=columnas)


# Cierra el navegador
driver.quit()


# In[314]:


rdeff = requests.get(urldeff, cookies=cookies, headers=headers)
html_contentsdeff = rdeff.text


# In[315]:


html_soupdeff = BeautifulSoup(html_contentsdeff, 'html.parser')


# In[316]:


tabla_puntajedeff = html_soupdeff.find_all('table', class_='Table Table--align-right') 


# In[317]:


columnasdeff =  ['GP','YDS','YDS/G','YDS1','YDS/G',
             'YDS2','YDS/G','PTS','PTS/G',]


# In[318]:


infdeff = pd.DataFrame(columns = columnasdeff)


# In[319]:


for table in tabla_puntajedeff:
    for row in table.find_all('tr')[2:]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(columnasdeff):
            infdeff.loc[len(infdeff)] = values


# In[320]:


dfdeff.insert(0, 'Semana', semana_siguiente)
dfdeff.insert(1, 'RK', range(1, 33, 1))
columnsUniddeff = pd.concat([dfdeff,infdeff], axis=1)


# In[321]:


columnas_deseadasdeff = ['Semana','RK','Equipo','GP','YDS']
Deff_select = columnsUniddeff[columnas_deseadasdeff]
Deff_select


# In[324]:


try:
    for index, row in Deff_select.iterrows():
        cursor1.execute(
            "INSERT INTO defencive (Semana, RK, Equipo, GP, YDS) "
            "VALUES (%s, %s, %s, %s, %s)",
            (int(row['Semana']), int(row['RK']), row['Equipo'], int(row['GP'].replace(',', '')), int(row['YDS'].replace(',', '')))
        )
        conexion1.commit()

except Exception as e:
    print(f"Error: {e}")
    # Rollback en caso de error
    conexion1.rollback()

finally:
    # Cierre del cursor fuera del bucle
    cursor1.close()

# Cierre de la conexión fuera del bucle de iteración
conexion1.close()


# In[368]:


Deff_select.to_excel('Export\\DEFRensemana11ESPN.xlsx') 


# # Power Index

# In[56]:


# Especifica la ubicación del controlador de Chrome (chromedriver.exe)
chromedriver_path = 'chromedriver.exe'

# Configura el servicio de Chrome con el argumento executable_path
chrome_service = ChromeService(executable_path=chromedriver_path)

# Crea una instancia del navegador Chrome con el servicio configurado
driver = webdriver.Chrome(service=chrome_service)

# Abre la página web
urlpi = 'https://www.espn.com.mx/futbol-americano/nfl/fpi'
driver.get(urlpi)

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
    if celdas:  # Verifica si hay al menos una celda de datos en la fila
        fila_datos = [celda.text.strip() for celda in celdas]
        datos.append(fila_datos)

# Crea un DataFrame de Pandas con los datos filtrados
columnas = ['Equipo']  # Reemplaza con el nombre de tu columna
dfpi = pd.DataFrame(datos, columns=columnas)


# Cierra el navegador
driver.quit()


# In[57]:


rpi = requests.get(urlpi, cookies=cookies, headers=headers)
html_contentspi = rpi.text


# In[58]:


html_souppi = BeautifulSoup(html_contentspi, 'html.parser')


# In[59]:


tabla_indexpi = html_souppi.find_all('table', class_='Table Table--align-right') 


# In[60]:


columnaspi =  ['W-L-T','FPI','RK1','TREND','OFF',
             'DEF','ST','SOS','REM SOS','AVGWP',]


# In[61]:


infpi = pd.DataFrame(columns = columnaspi)


# In[62]:


for table in tabla_indexpi:
    for row in table.find_all('tr')[2:]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(columnaspi):
            infpi.loc[len(infpi)] = values


# In[63]:


dfpi.insert(0, 'Semana', semana_siguiente)
dfpi.insert(1, 'RK', range(1, 33, 1))
columnsUnidpi = pd.concat([dfpi,infpi], axis=1)


# In[64]:


columnas_deseadaspi = ['Semana', 'RK', 'Equipo', 'FPI']
Pi_select = columnsUnidpi[columnas_deseadaspi]
Pi_select


# In[65]:


print("Semana:", row['Semana'])
print("RK:", row['RK'])


# In[73]:


try:
    for index, row in Pi_select.iterrows():
        cursor1.execute(
            "INSERT INTO powerindex (Semana, RK, Equipo, FPI)"
            "VALUES (%s, %s, %s, %s)",
            (int(row['Semana']), int(row['RK']),row['Equipo'],float(row['FPI']))
        )
    
    # Confirmar la transacción
    conexion1.commit()
    
except Exception as e:
    print(f"Error: {e}")
    # Realizar un rollback en caso de error
    conexion1.rollback()

finally:
    cursor1.close()
    conexion1.close()


# In[369]:


Pi_select.to_excel('Export\\powerindexESPNsem11.xlsx') 


# #  QBR
# 

# 

# In[348]:


urlqbr="https://www.espn.com.mx/futbol-americano/nfl/qbr"


# In[349]:


rqbr = requests.get(urlqbr, cookies=cookies, headers=headers)
html_contentsqbr = rqbr.text


# In[350]:


html_soupqbr = BeautifulSoup(html_contentsqbr, 'html.parser')


# In[351]:


tabla_QBR = html_soupqbr.find_all('table', class_='Table Table--align-right') 


# In[352]:


columnasqbr =  ['QBR','PAA','PLAYS','EPA','PASS',
             'RUN','SACK','PEN','RAW']


# In[353]:


QBR = pd.DataFrame(columns = columnasqbr)


# In[354]:


for table in tabla_QBR:
    for row in table.find_all('tr')[1:]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(columnasqbr):
            QBR.loc[len(QBR)] = values


# In[ ]:





# In[355]:


tabla_nomqbr = html_soupqbr.find_all('table', class_='Table Table--align-right Table--fixed Table--fixed-left') 
Nombresqbr =  ['RK','Nombre']
rk = pd.DataFrame(columns = Nombresqbr)


# In[356]:


for table in tabla_nomqbr:
    for row in table.find_all('tr')[1:]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if len(values) == len(Nombresqbr):
            rk.loc[len(rk)] = values


# In[357]:


tabla_eqbr = html_soupqbr.find_all('span', class_='pl2 ns10 athleteCell__teamAbbrev') 
Eqqbr =  ['Equipo']
nomqbr = pd.DataFrame(columns = Eqqbr)


# In[358]:


team_abbreviations = [element.text for element in tabla_eqbr]

# Crear un DataFrame con las abreviaciones
nomqbr = pd.DataFrame({Eqqbr[0]: team_abbreviations})


# In[ ]:





# In[363]:


resultado= pd.concat([rk, nomqbr, QBR], axis=1)


# In[364]:


resultado.insert(0, 'Semana', semana_siguiente)
resultado = resultado.drop(columns=['Nombre'])
resultado



# In[365]:


columnas_deseadasqbr = ['Semana', 'RK', 'Equipo', 'QBR']
QBR_select = resultado[columnas_deseadasqbr]
QBR_select


# In[ ]:


try:
    for index, row in df_mergedsem.iterrows():
        cursor1.execute(
            "INSERT INTO calendario (Semana, RK, Equipo, QBR) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (int(row['Equipo'], int(row['RK']), row['Equipo'], row['QBR']))
        )
    # Confirmar la transacción
    conexion1.commit()
    
except Exception as e:
    print(f"Error: {e}")
    # Realizar un rollback en caso de error
    conexion1.rollback()

finally:
    cursor1.close()
    conexion1.close()


# In[370]:


QBR_select.to_excel('Export\\QBR11.xlsx')  


# In[ ]:




