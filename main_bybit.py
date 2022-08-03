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
    driver.get("https://www.bybit.com/fiat/trade/otc/?actionType=0&token=USDT&fiat=ARS&paymentMethod=")
    driver.maximize_window() 

    #Get data from table
    page = 1
    records = []

    while page<5:

        prices = driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[1]/div[3]/div[2]/div/div/div/table/tbody')

        children = prices.find_elements(By.TAG_NAME,'tr')
        for price in children:
            mercadoPago = False
            bbva = False
            efectivo = False
            transferencia = False
            uala = False
            precio = price.find_element(By.CLASS_NAME,'price-amount').text
            print(precio)
            html = price.get_attribute('innerHTML')
            if 'Mercadopago' in html:
                print('Acepta Mercado Pago')
                mercadoPago = True
            if 'fectivo' in html:
                print('Acepta Efectivo')
                efectivo = True
            if 'BBVA' in html:
                print('Acepta BBVA')
                bbva = True
            if 'Bank Transfer' in html:
                print('Acepta Transferencia')
                transferencia = True
            if 'Uala' in html:
                print('Acepta Uala')
                uala = True

            print('Precio en ARS $', precio)
            records.append({'price': precio, 'mercadoPago': mercadoPago, 'efectivo': efectivo, 'transferencia': transferencia,'bbva': bbva, 'uala': uala, 'datetime': datetime.datetime.now(), 'operation': 'Compra'})


        print('Cambiando pagina...', page)

        btnNextXpath = '//*[@id="root"]/div[3]/div[1]/div[3]/div[2]/div/div/div/div/ul/li[@class="pagination-item pagination-item-'+str(page+1)+'"]/a'
        btnNextPage = driver.find_element(By.XPATH,btnNextXpath)
        btnNextPage.click()
        page+=1
        time.sleep(5)


    df = pd.DataFrame(records)

    print(df)
    df.to_csv('compra_bybit_' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.csv')


def get_csv_venta():
    driver.get("https://www.bybit.com/fiat/trade/otc/?actionType=1&token=USDT&fiat=ARS&paymentMethod=")
    driver.maximize_window() 

    #Get data from table
    page = 1
    records = []

    while page<2:

        prices = driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[1]/div[3]/div[2]/div/div/div/table/tbody')

        children = prices.find_elements(By.TAG_NAME,'tr')
        for price in children:
            mercadoPago = False
            bbva = False
            efectivo = False
            transferencia = False
            uala = False
            precio = price.find_element(By.CLASS_NAME,'price-amount').text
            print(precio)
            html = price.get_attribute('innerHTML')
            if 'Mercadopago' in html:
                print('Acepta Mercado Pago')
                mercadoPago = True
            if 'fectivo' in html:
                print('Acepta Efectivo')
                efectivo = True
            if 'BBVA' in html:
                print('Acepta BBVA')
                bbva = True
            if 'Bank Transfer' in html:
                print('Acepta Transferencia')
                transferencia = True
            if 'Uala' in html:
                print('Acepta Uala')
                uala = True

            print('Precio en ARS $', precio)
            records.append({'price': precio, 'mercadoPago': mercadoPago, 'efectivo': efectivo, 'transferencia': transferencia,'bbva': bbva, 'uala': uala, 'datetime': datetime.datetime.now(), 'operation': 'Compra'})


        print('Cambiando pagina...', page)

        btnNextXpath = '//*[@id="root"]/div[3]/div[1]/div[3]/div[2]/div/div/div/div/ul/li[@class="pagination-item pagination-item-'+str(page+1)+'"]/a'
        btnNextPage = driver.find_element(By.XPATH,btnNextXpath)
        btnNextPage.click()
        page+=1
        time.sleep(5)


    df = pd.DataFrame(records)

    print(df)
    df.to_csv('venta_bybit_' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.csv')

get_csv_venta()