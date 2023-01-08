from tbselenium.tbdriver import TorBrowserDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from selenium.webdriver.common.by import By
import time
  with TorBrowserDriver("/home/achaurasiya/Downloads/tor-browser/") as driver:
    driver.get("http://stniiomyjliimcgkvdszvgen3eaaoz55hreqqx6o77yvmpwt7gklffqd.onion")
    time.sleep(5)
    k=0

    for j in range(17):
      titles=driver.find_elements(By.CSS_SELECTOR,'div.title')
      descs=driver.find_elements(By.CSS_SELECTOR,'div.preview_container')
      
      Titles=[]
      Descs=[]
      for i in range(len(titles)):
         Titles.append(titles[i].text)
         Descs.append(descs[i].text)
      # df=pd.DataFrame({'Title':Titles,'Descriptions':Descs})
      # k=k+1
      # df.to_csv('/home/achaurasiya/Work/Dark Web Project/page'+str(k)+'.csv',index=False)
      # print(df)
      driver.find_element(By.CSS_SELECTOR,'div.next-page-btn').click()
      time.sleep(5)

    df=pd.DataFrame({'Title':Titles,'Descriptions':Descs})
    df.to_csv('/home/achaurasiya/Work/Dark Web Project/1/allpage.csv',index=False)
    print(df)
