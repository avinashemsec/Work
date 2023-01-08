from tbselenium.tbdriver import TorBrowserDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with TorBrowserDriver("/home/achaurasiya/Downloads/tor-browser/") as driver:
    driver.maximize_window()
    driver.get("http://jbeg2dct2zhku6c2vwnpxtm2psnjo2xnqvvpoiiwr5hxnc6wrp3uhnad.onion/")
    wait = WebDriverWait(driver, 500)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.h_font")))

    Titles=[]
    Descs=[]

    titles=driver.find_elements(By.CSS_SELECTOR,'h1.h_font')
    descs=driver.find_elements(By.CSS_SELECTOR,'p.lead-text5')

    for i in range(len(titles)):
         Titles.append(titles[i].text)
         Descs.append(descs[i].text)

    df=pd.DataFrame({'Title':Titles,'Descriptions':Descs})
    df.to_csv('/home/achaurasiya/Work/Dark Web Project/1/allpage.csv',index=False)
    print(df)
    driver.close()
