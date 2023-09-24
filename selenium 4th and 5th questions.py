#!/usr/bin/env python
# coding: utf-8

# In[19]:


get_ipython().system('pip install selenium')


# In[20]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[21]:


driver = webdriver.Edge()


# In[22]:


driver.get('https://www.flipkart.com/')
time.sleep(3)


# In[23]:


#remove the pop up page
pop_up_page =driver.find_element(By.XPATH,'/html/body/div[3]/div/span')
pop_up_page.click()
time.sleep(3)


# In[24]:


#search_product = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/div/section/div[2]/div/a")
#search_product.send_keys('sunglasses')
#search_button =driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
#search_button.click()
#time.sleep(5)
search_product = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/div/input')
search_product.send_keys('sunglasses')


# In[25]:


search_button =driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/button')
search_button.click()
time.sleep(5)


# In[32]:


Brand_name = []
Product_Description = []
Price= []
for i in range(3):
    brand=driver.find_elements(By.XPATH,"//div[@class='_2WkVRV']")
    for i in brand :
        b=i.text
        Brand_name.append(b)
    Brand_name

    product=driver.find_elements(By.XPATH,"//a[@class='IRpwTa']")
    for i in product[0:120]:
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


# In[33]:


print(len(Brand_name),len(Product_Description),len(Price))


# In[34]:


df = pd.DataFrame({'Brand': Brand_name,'Product_Description':Product_Description,'Price':Price})

df


# In[ ]:





# In[ ]:





# # Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market
# place=FLIPKART

# In[1]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[2]:


driver = webdriver.Edge()


# In[3]:


driver.get('https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market')


# In[4]:


def scrape_rating():
    rating=[]
    driver.refresh()
    rating_el=driver.find_elements_by_xpath("//div[@class='_3LWZlK _1BLPMq']")
    time.sleep(3)
    for i in rating_el:
        try:
            rating.append(i.text)
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight0)")
        except:
            rating.append("--")
    return rating
            


# In[5]:


def scrape_review_summary():
    review_sum=[]
    driver.refresh()
    rev_sum=driver.find_elements_by_xpath("//p[@class='_2-N8zT']")
    time.sleep(3)
    for i in rev_sum:
        try:
            review_sum.append(i.text)
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight0)")
        except:
            review_sum.append("--")
    return review_sum


# In[6]:


def scrape_full_review():
    full_review=[]
    driver.refresh()
    rev_el=driver.find_elements_by_xpath("//div[@class='t-ZTKy']/div")
    time.sleep(3)
    for i in rev_el:
        try:
            full_review.append(i.text.replace("\n","  New Line: "))
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight0)")
        except:
            full_review.append("--")
    return full_review


# In[8]:


rating=[]
review_sum=[]
full_review=[]
length=len(rating)
while(length<=100):
    driver.refresh()
    rating.extend(scrape_rating())
    review_sum.extend(scrape_review_summary())
    full_review.extend(scrape_full_review())
    time.sleep(5)
    length=len(rating)
    next_btn=driver.find_element_by_xpath("//a[@class='_1LKTO3']/span")
    next_btn.click()
    
len(review_sum)


# In[79]:


length_list=[len(full_review),len(rating),len(review_sum)]
length_list


# In[80]:


review_sum


# In[81]:


df6=pd.DataFrame()
df6["INDEX"]=range(1,101)
df6["RATING"]=rating[:100]
df6["REVIEW_SUMMARY"]=review_sum[:100]
df6["FULL_REVIEW"]=full_review[:100]
df6.set_index("INDEX",inplace=True)
df6


# In[ ]:




