#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[3]:


driver = webdriver.Edge()


# In[4]:


driver.get('https://www.flipkart.com/')
time.sleep(3)


# In[5]:


pop_up_page =driver.find_element(By.XPATH,'/html/body/div[3]/div/span')
pop_up_page.click()
time.sleep(3)


# In[6]:


search_product = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/div/input')
search_product.send_keys('sneakers')


# In[7]:


search_button =driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/button')
search_button.click()
time.sleep(5)


# In[19]:


Brand_name = []
Product_Description = []
Price= []
for i in range(3):
    #brand=driver.find_elements(search_item = driver.find_element_by_xpath("//input[@class='nav-input nav-progressive-attribute']")
    brand=driver.find_elements(By.XPATH,"//div[@class='_2WkVRV']")                          
#search_item.send_keys("laptop"))
    for i in brand :
        b=i.text
        Brand_name.append(b)
    Brand_name

    product=driver.find_elements(By.XPATH,"//a[@class='IRpwTa']")
    for i in product:
        p=i.text
        Product_Description.append(p)
    Product_Description

    price_1=driver.find_elements(By.XPATH,"//div[@class='_30jeq3']")
    for i in price_1:
        pri=i.text
        Price.append(pri)
    Price
  
nxt_button=driver.find_element(By.XPATH,"//a[@class='_1LKTO3']")#scraping the list of buttons from the page
nxt_button.click()


# In[20]:


print(len(Brand_name),len(Product_Description),len(Price))


# In[1]:


df = pd.DataFrame({'Brand': Brand_name,'Product_Description':Product_Description,'Price':Price})

df


# # Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then
# # set CPU Type filter to “Intel Core i7” as shown in the below image:
# After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price
# 

# In[2]:


get_ipython().system('pip install selenium')


# In[21]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[22]:


driver = webdriver.Edge()


# In[23]:


driver.get("https://www.amazon.in/")


# In[24]:


search_item = driver.find_element(By.XPATH,"//input[@class='nav-input nav-progressive-attribute']")
search_item.send_keys("laptop")


# In[25]:


click_search_button = driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']")
click_search_button.click()


# In[27]:


intel_core7 = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[6]/span[13]")
intel_core7.click()

time.sleep(5)


# In[28]:


Title = []
Ratings = []
Price = []

title = driver.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
rating = driver.find_elements(By.XPATH,"//span[@data-hook='acr-average-stars-rating-text']")
price = driver.find_elements(By.XPATH,"//span[@class='a-price-whole']")

for i in title:Title.append(i.text)
for i in rating:Ratings.append(i.text)    
for i in price:Price.append(i.text)
    


# In[29]:


Laptop = pd.DataFrame({'Title':Title,'Price':Price})
Laptop[0:10]


# # Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# #The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on TopQuotes
# 

# In[39]:


get_ipython().system('pip install selenium')


# In[47]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[48]:


driver = webdriver.Edge()


# In[49]:


driver.get("https://www.azquotes.com/")


# In[50]:


search_item = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a")
search_item.click()


# In[57]:


quotes = []
author = []
typename= []
for i in range(10):
    #brand=driver.find_elements(search_item = driver.find_element_by_xpath("//input[@class='nav-input nav-progressive-attribute']")
    q=driver.find_elements(By.XPATH,"//a[@class='title']")                          
#search_item.send_keys("laptop"))
    for i in q :
        b=i.text
        quotes.append(b)
    quotes

    aut=driver.find_elements(By.XPATH,"//div[@class='author']")
    for i in aut:
        p=i.text
        author.append(p)
    author

    ty=driver.find_elements(By.XPATH,"//div[@class='tags']")
    for i in ty:
        pri=i.text
        typename.append(pri)
    typename
  
nxt_button=driver.find_element(By.XPATH,"//li[@class='next']")#scraping the list of buttons from the page
nxt_button.click()


# In[58]:


print(len(quotes),len(author),len(typename))


# In[59]:


df = pd.DataFrame({'Quotes': quotes,'Author':author,'Type':typename})

df


# In[ ]:





# # Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead,
# Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpagehttps://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make theDataFrame

# In[60]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[61]:


driver = webdriver.Edge()


# In[62]:


driver.get("https://www.jagranjosh.com/")


# In[63]:


search_item = driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/div/div[3]/ul/li[3]/a")
search_item.click()


# In[64]:


search_item = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a")
search_item.click()


# In[ ]:


table = []
q=driver.find_elements(By.XPATH,"//div[@class='table-box']//table//")                          
#search_item.send_keys("laptop"))
for i in q:
    b=i.text
    table.append(b)
table


# In[85]:


table = []
q=driver.find_elements(By.XPATH,"//div[@class='table-box']")                          
#search_item.send_keys("laptop"))
for i in q:
    b=i.text
    table.append(b)
    #with open("D:\\log2.txt","a") as f:
        #f.write(f'{table}')
table
                


# In[84]:


df = pd.read_csv("D:\log2.txt")

print(df.to_string())

df = pd.read_csv("log2.txt", sep="\n ")
  
# display DataFrame
print(df)


# # Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e.
# Car name and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpage https://www.motor1.com/
# 2. Then You have to type in the search bar ’50 most expensive cars’
# 3. Then click on 50 most expensive carsin the world..
# 4. Then scrap the mentioned data and make the dataframe

# In[102]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[103]:


driver = webdriver.Edge()


# In[104]:


driver.get("https://www.motor1.com/")


# In[105]:


search_item = driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/input")
search_item.send_keys("50 most expensive cars")


# In[106]:


click_search_button = driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/button[1]")
click_search_button.click()


# In[107]:


click_link = driver.find_element(By.XPATH,"/html/body/div[10]/div[9]/div/div[1]/div/div/div[2]/div/div[1]/h3/a")
click_link.click()


# In[108]:


header=[]
head=driver.find_elements(By.XPATH,"//h3[@class='subheader']")                          
#search_item.send_keys("laptop"))

for i in head[0:50]:
    b=i.text
    header.append(b)
header




# In[109]:


pic_list=[]
pic=driver.find_elements(By.XPATH,"//section//picture[@class='lazyload']")                          
#search_item.send_keys("laptop"))

for i in pic:
    b=i.text
    pic_list.append(b)
pic_list


# In[110]:


price_list=[]
price=driver.find_elements(By.XPATH,"//div[@class='postBody description e-content']//p//strong")                          
#search_item.send_keys("laptop"))

for i in price:
    b=i.text
    price_list.append(b)
price_list


# In[111]:


print(len(header),len(price_list),len(pic_list))


# In[112]:


df = pd.DataFrame({'Header': header,'Price':price_list,'Picture':pic_list})

df


# In[ ]:




