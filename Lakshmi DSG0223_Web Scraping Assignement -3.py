#!/usr/bin/env python
# coding: utf-8

# # Q :1 Write a python program which searches all the product under a particular product from www.amazon.in. The 
# #product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for 
# #guitars. 

# In[13]:


import pandas as pd
import selenium
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import requests
import re
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


# In[14]:


driver=webdriver.Edge()


# In[15]:


driver.get("https://www.amazon.in")


# In[16]:


user_input = input("Enter the product :")


# In[17]:


search = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
search


# In[18]:


search.send_keys(user_input)


# In[19]:


search_btn = driver.find_element(By.XPATH,"//div[@class='nav-search-submit nav-sprite']/span/input")
search_btn.click()


# # Q : 2 In the above question, now scrape the following details of each product listed in first 3 pages of your search 
# results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then 
# scrape all the products available under that product name. Details to be scraped are: "Brand 
# Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and 
# “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“. 

# In[ ]:





# In[22]:


urls = []          # empty list
for i in range(0,3):      # for loop to scrape 3 pages
    page_url = driver.find_elements(By.XPATH,"//a[@class='a-link-normal a-text-normal']")
    for i in page_url:
        urls.append(i.get_attribute("href"))
       # next_btn = driver.find_element(By.XPATH"//li[@class='a-last']/a")
        next_btn = driver.find_element(By.XPATH,"//li[@class='a-last']/a")
        time.sleep(3)


# In[23]:


len(urls)


# In[27]:


#making empty list and fetching required data
brand_name = []
product_name = []
ratings = []
num_ratings = []
prices = []
exchange = []
exp_delivery = []
availability = []
other_details = []

for i in urls:
   driver.get(i)
   time.sleep(3)
   
   
   #fetching brand name 
   try:
       brand = driver.find_element_by_xpath("//a[@id='bylineInfo']")
       brand_name.append(brand.text)
   except NoSuchElementException:
       brand_name.append('-')
   
   
   # fetching Name of the Product
   try:
       product = driver.find_element_by_xpath("//span[@id='productTitle']")
       product_name.append(product.text)
   except NoSuchElementException:
       product_name.append('-')
       
       

    #fetching ratings
   try:
       rating = driver.find_element_by_xpath("//span[@class='a-size-base a-nowrap']/span")
       ratings.append(rating.text)
   except NoSuchElementException:
       ratings.append('-')
       

   #fetching  no of ratings
   try:
       num_rating = driver.find_element_by_xpath("//span[@id='acrCustomerReviewText']")
       num_ratings.append(num_rating.text)
   except NoSuchElementException:
       num_ratings.append('-')
       

   #fetching price of the product
   try:
       price = driver.find_element_by_xpath("//td[@class='a-span12']")
       prices.append(price.text)
   except NoSuchElementException:
       prices.append('-')
       
       
   #fetching return/exchange
   try:
       exch = driver.find_element_by_xpath("//span[@class='a-declarative']/div/a")
       exchange.append(exch.text)
   except NoSuchElementException:
       exchange.append('-')
       

   #fetching expected delivery
   try:
       delivery = driver.find_element_by_xpath("//div[@class='a-section a-spacing-mini']/b")
       exp_delivery.append(delivery.text)
   except NoSuchElementException:
       exp_delivery.append('-')
       

   #fetching availability information
   try:
       avail = driver.find_element_by_xpath("//span[@class='a-size-medium a-color-success']")
       availability.append(avail.text)
   except NoSuchElementException:
       availability.append('-')
       
   #other details
   try:
       oth_det = driver.find_element_by_xpath("//ul[@class='a-unordered-list a-vertical a-spacing-mini']")
       other_details.append(oth_det.text)
   except NoSuchElementException:
       other_details.append('-')
       


# In[28]:


print(len(brand_name),
len(product_name),
len(ratings),
len(num_ratings),
len(prices),
len(exchange),
len(exp_delivery),
len(availability),
len(other_details))


# In[29]:


guitar = pd.DataFrame({})
guitar['Brand Name'] = brand_name
guitar['Name of the Product'] = product_name
guitar['Rating'] = ratings
guitar['No. of Ratings'] = num_ratings
guitar['Price'] = prices
guitar['Return/Exchange'] = exchange
guitar['Expected Delivery'] = exp_delivery
guitar['Availability'] = availability
guitar['Other Details'] = other_details
guitar['Product URL'] = urls
guitar


# In[ ]:





# # Q 3 : Write a python program to access the search bar and search button on images.google.com and scrape 10 
# images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’. 

# In[ ]:


Write a python program to access the search bar and search button on images.google.com and scrape 10 
images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’. 


# In[51]:


driver=webdriver.Edge()


# In[52]:


url = "http://images.google.com/"


urls = []
data = []

search_item = ["Fruits","Cars","Machine Learning","Guitar", "Cakes"]
for item in search_item:
    driver.get(url)
    time.sleep(5)
    
   
    search = driver.find_element(By.XPATH,"//textarea[@class='gLFyf']")
    search.send_keys(item)
    
    
    search_button = driver.find_element(By.XPATH,"//button[@class='Tg7LZd']").click()
    
    
    for _ in range(100):
        driver.execute_script("window.scrollBy(0,50)")
        
        imgs = driver.find_elements(By.XPATH,"//img[@class='rg_i Q4LuWd']")
    img_url = []
    for image in imgs:
        source = image.get_attribute('src')
        if source is not None:
            if(source[0:4] == 'http'):
                img_url.append(source)
    for i in img_url[:10]:
        urls.append(i)
        
for i in range(len(urls)):
    if i >= 50:
        break
    print("Google Images downloading {0} of {1}" .format(i,50))
    response = requests.get(urls[i])
    
    file = open(r"D:\google\images"+str(i)+".jpg","wb")
    
    file.write(response.content)


# In[29]:


driver.close()


# # 4. Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com
# and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand 
# Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”, 
# “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the 
# details is missing then replace it by “- “. Save your results in a dataframe and CSV. 

# In[36]:


import pandas as pd
import selenium
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import requests
import re
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


# In[40]:


driver=webdriver.Edge()


# In[41]:


url = "https://www.flipkart.com/"
driver.get(url)


# In[42]:


user_input = input("Enter the product :")


# In[ ]:





# In[47]:


search = driver.find_element(By.XPATH,"//input[@class='Pke_EE']")
search.send_keys(user_input)


# In[50]:


search_btn = driver.find_element(By.XPATH,"//button[@class='_2iLD__']")

# clicking on search button
search_btn.click()


# In[52]:


page1_url = []
urls = driver.find_elements(By.XPATH,"//a[@class='_1fQZEK']")
for url in urls:
    page1_url.append(url.get_attribute('href'))


# In[53]:


len(page1_url)


# In[56]:


# creating empty list
Smartphones = ({})
Smartphones['Brand'] = []
Smartphones['Phone name'] = []
Smartphones['Colour'] = []
Smartphones['RAM'] = []
Smartphones['Storage(ROM)'] = []
Smartphones['Primary Camera'] = []
Smartphones['Secondary Camera'] = []
Smartphones['Display Size'] = []
Smartphones['Display Resolution'] = []
Smartphones['Processor'] = []
Smartphones['Processor Cores'] = []
Smartphones['Battery Capacity'] = []
Smartphones['Price'] = []
Smartphones['URL'] = []


# In[58]:


for url in page1_url:
    driver.get(url)
    print("Scraping URL = ",url)
    Smartphones['URL'].append(url)
    time.sleep(2)
    
    
    #clicking on read more button to get more information
    try:
        read_more = driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _1FH0tX']")
        read_more.click()
    except NoSuchElementException:
        print("Exception occured while moving to next page")
    
    #scraping brand name of smartphone
    try:
        brand_tags = driver.find_element(By.XPATH,"//span[@class='B_NuCI']")
        Smartphones['Brand'].append(brand_tags.text.split()[0])
    except NoSuchElementException:
        Smartphones['Brand'].append('-')
    
    
    # scraping name of smartphones
    try:
        name_tags = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][1]/table/tbody/tr[3]/td[2]/ul/li")
        Smartphones['Phone name'].append(name_tags.text)
    except NoSuchElementException:
        Smartphones['Phone name'].append('-')
        
    #scraping colour of smartphone
    try:
        color_tags = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][1]/table/tbody/tr[4]/td[2]/ul/li")
        Smartphones['Colour'].append(color_tags.text)
    except NoSuchElementException:
        Smartphones['Colour'].append('-')
        
    # scraping RAM data of smartphone
    try:
        ram_tags = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][4]/table[1]/tbody/tr[2]/td[2]/ul/li")
        Smartphones['RAM'].append(ram_tags.text)
    except NoSuchElementException:
        Smartphones['RAM'].append('-')
        
    #scraping ROM data of smartphones
    try:
        rom = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][4]/table[1]/tbody/tr[1]/td[2]/ul/li")
        Smartphones['Storage(ROM)'].append(rom.text)
    except NoSuchElementException:
        Smartphones['Storage(ROM)'].append('-')
        
    # scraping  Primary camera data of smartphone
    try:
        pri =driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][5]/table[1]/tbody/tr[2]/td[2]/ul/li")
        Smartphones['Primary Camera'].append(pri.text)
    except NoSuchElementException:
        Smartphones['Primary Camera'].append('-')
        
    # scraping secondary camera data of smartphone
    try:
        sec = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][5]/table[1]/tbody/tr[6]/td[1]")
        if sec != 'Secondary Camera' :
            if driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][5]/table[1]/tbody/tr[5]/td[1]").text == "Secondary Camera":
                sec_cam =driver.find_element_by_xpath("//div[@class='_3k-BhJ'][5]/table[1]/tbody/tr[5]/td[2]/ul/li")
            else :
                raise NoSuchElementException
        else :
            sec_cam = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][5]/table[1]/tbody/tr[6]/td[2]/ul/li")
        Smartphones['Secondary Camera'].append(sec_cam.text)
    except NoSuchElementException:
        Smartphones['Secondary Camera'].append('-')
        
    
    #scraping display size data of smartphone
    try:
        disp = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][2]/div")
        if disp.text != 'Display Features' : raise NoSuchElementException
        disp_size = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][2]/table[1]/tbody/tr[1]/td[2]/ul/li")
        Smartphones['Display Size'].append(disp_size.text)
    except NoSuchElementException:
        Smartphones['Display Size'].append('-')
        
    
    #scraping display resolution of smartphone
    try:
        disp = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][2]/div")
        if disp.text != 'Display Features' : raise NoSuchElementException
        disp_reso = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][2]/table[1]/tbody/tr[2]/td[2]/ul/li")
        Smartphones['Display Resolution'].append(disp_reso.text)
    except NoSuchElementException:
        Smartphones['Display Resolution'].append('-')
        
        
    #scraping processor of smartphone
    try:
        pro = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][3]/table[1]/tbody/tr[2]/td[1]]")
        if pro.text != 'Processor Type' : raise NoSuchElementException
        processor = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][3]/table[1]/tbody/tr[2]/td[2]/ul/li")
        Smartphones['Processor'].append(processor.text)
    except NoSuchElementException:
        Smartphones['Processor'].append('-')
    
        
       
    # scraping processor core of smartphone
    try:
        core = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][3]/table[1]/tbody/tr[3]/td[1]")
        if core.text != 'Processor Core' :
            core = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][3]/table[1]/tbody/tr[2]/td[1]")
            if core.text != 'Processor Core' :
                raise NoSuchElementException
            else :
                cores = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][3]/table[1]/tbody/tr[2]/td[2]/ul/li")
        else :
            cores = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][3]/table[1]/tbody/tr[3]/td[2]/ul/li")
        Smartphones['Processor Cores'].append(disp_reso.text)
    except NoSuchElementException:
        Smartphones['Processor Cores'].append('-')
        
        
        
    # scraping the battery capacity of smartphone
    try:
        if driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][10]/div").text != "Battery & Power Features" :
            if driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][9]/div").text == "Battery & Power Features" :
                bat_tags = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][9]/table/tbody/tr/td[1]")
                if bat_tags.text != "Battery Capacity" : raise NoSuchElementException
                bat_capa = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][9]/table/tbody/tr/td[2]/ul/li")
            elif driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][8]/div").text == "Battery & Power Features" :
                bat_tags = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][8]/table/tbody/tr/td[1]")
                if bat_tags.text != "Battery Capacity" : raise NoSuchElementException
                bat_capa = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][8]/table/tbody/tr/td[2]/ul/li")
            else:
                raise NoSuchElementException
        else :
            bat_tags = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][10]/table/tbody/tr/td[1]")
            if bat_tags.text != "Battery Capacity" : raise NoSuchElementException
            bat_capa = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][10]/table/tbody/tr/td[2]/ul/li")
        Smartphones['Battery Capacity'].append(bat_capa.text)
    except NoSuchElementException:
        Smartphones['Battery Capacity'].append('-')
    
    
    
    
    # scraping price of smartphone
    try:
        price_tags = driver.find_element(By.XPATH,"//div[@class='_30jeq3 _16Jk6d']")
        Smartphones['Price'].append(price_tags.text)
    except NoSuchElementException:
          Smartphones['Price'].append('-')  


# In[59]:


print(len(Smartphones['Brand']),len(Smartphones['Phone name']), len(Smartphones['Colour']),len(Smartphones['RAM']),len(Smartphones['Storage(ROM)']),len(Smartphones['Primary Camera']),len(Smartphones['Secondary Camera']), len(Smartphones['Display Size']), len(Smartphones['Display Resolution']), len(Smartphones['Processor']), len(Smartphones['Processor Cores']), len(Smartphones['Battery Capacity']), len(Smartphones['Price']), len(Smartphones['URL'])) 


# In[60]:



df = pd.DataFrame.from_dict(Smartphones)
df


# In[ ]:





# # 5. Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps.

# In[54]:


driver=webdriver.Edge()


# In[55]:


url = 'https://www.google.co.in/maps'
driver.get(url)
time.sleep(2)


# In[58]:


City = input('Enter City name that has to be searched : ')
search_bar = driver.find_element(By.ID,'searchboxinput')
search_bar.click()
time.sleep(2)

#sending keys to find cities
search_bar.send_keys(City)

#checking for webelement and clicking on search button
search_btn = driver.find_element(By.ID,"searchbox-searchbutton")
search_btn.click()
time.sleep(2)

try:
    url_str = driver.current_url
    print("URL Extracted: ", url_str)
    latitude_longitude = re.findall(r'@(.*)data',url_str)
    if len(latitude_longitude):
        lat_lng_list = latitude_longitude[0].split(",")
        if len(lat_lng_list)>=2:
            latitude = lat_lng_list[0]
            longitude = lat_lng_list[1]
        print("Latitude = {}, Longitude = {}".format(latitude, longitude))
except Exception as e:
        print("Error: ", str(e))


# In[ ]:





# # 7. Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: 
# “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”.

# In[59]:


driver=webdriver.Edge()


# In[60]:


url = "https://www.forbes.com/?sh=41bd46d2254c"
driver.get(url)


# In[63]:


opt_btn = driver.find_element(By.XPATH,"//div[@class='_69hVhdY4']//button")
opt_btn.click()
time.sleep(3)

#select billionaires from options
blns = driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div[3]/ul/li[1]")
blns.click()
time.sleep(3)
#select world billionaire
bln_list = driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div[3]/ul/li[1]/div[2]/ul/li[2]/a")
bln_list.click()
time.sleep(4)


# In[ ]:


Rank = []
Person_Name = []
Net_worth = []
Age = []
Citizenship = []
Source = []
Industry = []


while(True):
    
    # scraping the data of rank of the billionaires
    rank_tag = driver.find_elements_by_xpath("//div[@class='rank']")
    for rank in rank_tag:
        Rank.append(rank.text)
    time.sleep(1)
    
    
 
    # scraping the data  of names of the billionaires
    name_tag = driver.find_elements_by_xpath("//div[@class='personName']/div")
    for name in name_tag:
        Person_Name.append(name.text)
    time.sleep(1)
    
    
    # scraping the data of age of the billionaires
    age_tag = driver.find_elements_by_xpath("//div[@class='age']/div")
    for age in age_tag:
        Age.append(age.text)
    time.sleep(1)
    
    
    # scraping the data of citizenship of the billionaires
    cit_tag = driver.find_elements_by_xpath("//div[@class='countryOfCitizenship']")
    for cit in cit_tag:
        Citizenship.append(cit.text)
    time.sleep(1)
    
    
    # scraping the data of source of income of the billionaires
    sour_tag = driver.find_elements_by_xpath("//div[@class='source']")
    for sour in sour_tag:
        Source.append(sour.text)
    time.sleep(1)
    
    
    # scraping data of industry of the billionaires
    ind_tag = driver.find_elements_by_xpath("//div[@class='category']//div")
    for ind in ind_tag:
        Industry.append(ind.text)
    time.sleep(1)
    
    
    # scraping data of net_worth of billionaires
    net_tag = driver.find_elements_by_xpath("//div[@class='netWorth']/div")
    for net in net_tag:
        Net_worth.append(net.text)
    time.sleep(1)
    
    
    # clicking on next button
    try:
        next_button = driver.find_element_by_xpath("//button[@class='pagination-btn pagination-btn--next ']")
        next_button.click()
    except:
        break


# In[ ]:


print(len(Rank),
len(Person_Name),
len(Net_worth),
len(Age),
len(Citizenship),
len(Source),
len(Industry))


# In[ ]:


Billionaires = pd.DataFrame({})
Billionaires['Rank'] = Rank
Billionaires['Name'] = Person_Name
Billionaires['Net Worth'] = Net_worth
Billionaires['Age'] = Age
Billionaires['Citizenship'] = Citizenship
Billionaires['Source'] = Source
Billionaires['Industry'] = Industry
Billionaires


# # 8. Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted 
# from any YouTube Video. 

# In[63]:


driver=webdriver.Edge()


# In[64]:


url = "https://www.youtube.com/"
driver.get(url)
time.sleep(2)


# In[70]:


search_bar = driver.find_element(By.XPATH,"//input[@class='ytd-searchbox']")
search_bar.send_keys("GOT")      # entering video name
time.sleep(2)


# In[73]:


user_input = input("Enter the product :")



# In[77]:


search = driver.find_element(By.XPATH,"//div[@class='ytd-searchbox-spt']/input")
search.send_keys(user_input)


# In[ ]:


search_btn = driver.find_element(By.XPATH,"//button[@class='style-scope ytd-searchbox']")

# clicking on search button
search_btn.click()


# In[ ]:





# In[ ]:





# # 9. Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in 
# “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall 
# reviews, privates from price, dorms from price, facilities and property description.

# In[64]:


driver=webdriver.Edge()


# In[65]:


# getting the web page of mentioned url
url = "https://www.hostelworld.com/"
driver.get(url)
time.sleep(3)


# In[67]:


# locating the location search bar
search_bar = driver.find_element(By.XPATH,"search-input-field")

# entering London in search bar
search_bar.send_keys("London")


# In[ ]:




