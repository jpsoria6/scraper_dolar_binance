from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd 
import time
import datetime


#Set web driver and navigate
driver = webdriver.Chrome('./drivers/chromedriver.exe')



def get_csv_compra():
    driver.get("https://p2p.binance.com/es/trade/all-payments/USDT?fiat=ARS")
    time.sleep(20)
    #Get data from table
    page = 0
    records = []

    while page<10:

        prices = driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/main/div[1]/div[4]/div/div[2]')

        children = prices.find_elements(By.CLASS_NAME,'css-ovjtyv')

        for price in children:
            mercadoPago = False
            precio = price.find_element(By.CLASS_NAME,'css-1m1f8hn').text
            html = price.get_attribute('innerHTML')
            if 'Mercadopago' in html:
                print('Acepta Mercado Pago')
                mercadoPago = True
            else:
                print('No acepta Mercado Pago')
            print('Precio en ARS $',precio)

            records.append({'price':precio,'mercadoPago':mercadoPago,'datetime':datetime.datetime.now(),'operation':'Compra'})

        print('Cambiando pagina...', page)

        btnNextXpath = '//*[@id="__APP"]/div[2]/main/div[1]/div[4]/div/div[3]/div/button[@aria-label="Page number '+str(page+1)+'"]'
        btnNextPage = driver.find_element(By.XPATH,btnNextXpath)
        btnNextPage.click()
        page+=1
        time.sleep(5)


    df = pd.DataFrame(records)

    print(df)
    df.to_csv('compra.csv')


def get_csv_venta():
    driver.get("https://p2p.binance.com/es/trade/sell/USDT?fiat=ARS&payment=ALL")
    time.sleep(20)
    #Get data from table
    page = 0
    records = []

    while page<10:

        prices = driver.find_element(By.XPATH, '//*[@id="__APP"]/div[2]/main/div[1]/div[4]/div/div[2]')

        children = prices.find_elements(By.CLASS_NAME,'css-ovjtyv')

        for price in children:
            mercadoPago = False
            precio = price.find_element(By.CLASS_NAME,'css-1m1f8hn').text
            html = price.get_attribute('innerHTML')
            if 'Mercadopago' in html:
                print('Acepta Mercado Pago')
                mercadoPago = True
            else:
                print('No acepta Mercado Pago')
            print('Precio en ARS $',precio)

            records.append({'price':precio,'mercadoPago':mercadoPago,'datetime':datetime.datetime.now(),'operation':'Venta'})

        print('Cambiando pagina...', page)

        btnNextXpath = '//*[@id="__APP"]/div[2]/main/div[1]/div[4]/div/div[3]/div/button[@aria-label="Page number '+str(page+1)+'"]'
        btnNextPage = driver.find_element(By.XPATH,btnNextXpath)
        btnNextPage.click()
        page+=1
        time.sleep(5)


    df = pd.DataFrame(records)

    print(df)
    df.to_csv('venta.csv')

get_csv_venta()