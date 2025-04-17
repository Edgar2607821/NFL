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


# In[2]:


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

cookies = {
    'cookie_name': 'cookie_value'
}


# In[3]:


# Especifica la ubicación del controlador de Chrome (chromedriver.exe)
chromedriver_path = 'chromedriver.exe'

# Configura el servicio de Chrome con el argumento executable_path
chrome_service = ChromeService(executable_path=chromedriver_path)

# Crea una instancia del navegador Chrome con el servicio configurado
driver = webdriver.Chrome(service=chrome_service)

# Abre la página web
url = 'https://www.google.com'
driver.get(url)


# In[ ]:




