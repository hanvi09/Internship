#!/usr/bin/env python
# coding: utf-8

# • Read all the problem statements, notes carefully and scrape the required data using any web scraping tool of 
# your choice. 
# • You have to handle commonly occurring EXCEPTIONS by using exception handling programing. To get 
# information about selenium Exceptions. You may visit following links: 
# 1. https://selenium-python.readthedocs.io/api.html
# 2. https://www.guru99.com/exception-handling-selenium.html
# 3. https://stackoverflow.com/questions/38022658/selenium-python-handling-no-such-elementexception/38023345
# 1. Scrape the details of most viewed videos on YouTube from Wikipedia. Url 
# = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos You need to find following details: A)
# Rank 
# B) Name 
# C) Artist 
# D) Upload date 
# E) Views 

# In[54]:



import re


import selenium
import pandas as pd
from selenium import webdriver


from bs4 import BeautifulSoup
import requests


import time
from selenium.webdriver.common.by import By


from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from selenium.webdriver.support.ui import WebDriverWait


# In[6]:



driver=webdriver.Edge()



driver.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')


# In[7]:




Rank = []
Name = []
Artist = []
Date = []
Views = []


# In[12]:



try:
    for i in driver.find_elements(By.XPATH,"//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[1]"):
        Rank.append(i.text)
except NoSuchElementException:
    Rank.append("-")
        

try:
    for i in driver.find_elements(By.XPATH,"//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[2]"):
        Name.append(i.text)
except NoSuchElementException:
    Name.append("-")
        

try:
    for i in driver.find_elements(By.XPATH,"//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[3]"):
        Artist.append(i.text)
except NoSuchElementException:
    Artist.append("-")
        

try:
    for i in driver.find_elements(By.XPATH,"//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[5]"):
        Date.append(i.text)
except NoSuchElementException:
    Date.append("-")
        

try:
    for i in driver.find_elements(By.XPATH,"//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[4]"):
        Views.append(i.text)
except NoSuchElementException:
    Views.append("-")
        


# In[13]:



Wiki = pd.DataFrame({})
Wiki['Rank'] = Rank
Wiki['Name'] = Name
Wiki['Artist'] = Artist
Wiki['Upload Date'] = Date
Wiki['Views (in Billions)'] = Views


Wiki.Name = Wiki.Name.apply(lambda x:x[:-4].strip('"'))
Wiki


# In[14]:


print(len(Rank),
len(Name),
len(Artist),
len(Date),
len(Views))


# In[15]:


driver.close()


# 2. Scrape the details team India’s international fixtures from bcci.tv. 
# Url = https://www.bcci.tv/. 
# You need to find following details: 
# A) Series 
# B) Place 
# C) Date 
# D) Time 
# Note: - From bcci.tv home page you have reach to the international fixture page through code. 

# In[8]:


driver=webdriver.Edge()


# In[9]:


url=('https://www.bcci.tv/')
driver.get(url)


# In[6]:


btn=driver.find_element(By.XPATH,"//div[@class='navigation__drop-down drop-down drop-down--reveal-on-hover']/div/ul/li/a")
driver.get(btn.get_attribute("href"))
time.sleep(3)


# In[20]:




# creating empty lists for scraping the data
Match_Title = []
Series = []
Place = []
Date = []
Time = []


# In[22]:


for i in driver.find_elements(By.XPATH,"//div[@class='fixture__format-strip']/span[@class='u-unskewed-text fixture__format']"):
    Match_Title.append(i.text)
    
for i in driver.find_elements(By.XPATH,"//div[@class='fixture__format-strip']/span[@class='u-unskewed-text fixture__tournament-label u-truncated']"):
    Series.append(i.text)
    
for i in driver.find_elements(By.XPATH,"//div[@class='fixture__description u-unskewed-text']/p/span"):
    Place.append(i.text)
        
for i in driver.find_elements(By.XPATH,"//span[@class='fixture__datetime tablet-only']/strong[1]"):
    Date.append(i.text.replace('\n',' '))

date=[i.split(' ',3)[:3] for i in Date]
date=[' '.join(i) for i in date]
Time=[i.split(' ',3)[-1] for i in Date]

# creating data frame
fixture=pd.DataFrame({'Match Title': Match_Title,
                          "Series": Series,
                          "Place": Place,
                          "Date": date,
                          "Time": Time})
fixture


# In[23]:



len(url)


# # question 3 : Scrape the details of State-wise GDP of India from statisticstime.com. 
# Url = http://statisticstimes.com/ 
# You have to find following details: A) Rank 
# B) State 
# C) GSDP(18-19)- at current prices 
# D) GSDP(19-20)- at current prices 
# E) Share(18-19) 
# F) GDP($ billion) 
# Note: - From statisticstimes home page you have to reach to economy page through code

# In[26]:


driver=webdriver.Edge()


# In[27]:


url = ("https://statisticstimes.com/")
driver.get(url)


# In[28]:



driver.find_element(By.XPATH,"//div[@class='navbar']/div[2]/button").click()


driver.find_element(By.XPATH,"//div[@class='dropdown-content']/a[3]").click()
time.sleep(3)


GDP = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/ul/li[1]/a").click()
time.sleep(3)


# In[29]:


Rank = []
State = []
GSDP1 = []
GSDP2 = []
Share = []
GDP_billion = []


# In[30]:


try:
    for i in driver.find_elements(By.XPATH,"//table[@class='display dataTable']/tbody/tr/td[1]"):
        Rank.append(i.text)
except NoSuchElementException:
    Rank.append("_")
    

try:
    for i in driver.find_elements(By.XPATH,"//table[@class='display dataTable']/tbody/tr/td[2]"):
        State.append(i.text)
except NoSuchElementException:
    State.append("_")
    

try:
    for i in driver.find_elements(By.XPATH,"//table[@class='display dataTable']/tbody/tr/td[3]"):
        GSDP1.append(i.text)
except NoSuchElementException:
    GSDP1.append("_")
    

try:
    for i in driver.find_elements(By.XPATH,"//table[@class='display dataTable']/tbody/tr/td[4]"):
        GSDP2.append(i.text)
except NoSuchElementException:
    GSDP2.append("_")
    

try:
    for i in driver.find_elements(By.XPATH,"//table[@class='display dataTable']/tbody/tr/td[5]"):
        Share.append(i.text)
except NoSuchElementException:
    Share.append("_")
    

try:
    for i in driver.find_elements(By.XPATH,"//table[@class='display dataTable']/tbody/tr/td[6]"):
        GDP_billion.append(i.text)
except NoSuchElementException:
    GDP_billion.append("_")
    
    

GDP = pd.DataFrame({})
GDP['Rank'] = Rank
GDP['State'] = State
GDP['GSDP at current price (19-20)'] = GSDP1
GDP['GSDP at current price (18-19)'] = GSDP2
GDP['Share (18-19)'] = Share
GDP['GDP($ billion)'] = GDP_billion
GDP
    


# # Scrape the details of trending repositories on Github.com. 
# Url = https://github.com/ 
# You have to find the following details: 
# A) Repository title 
# B) Repository description 
# C) Contributors count 
# D) Language used 
# Note: - From the home page you have to click on the trending option from Explore menu through code. 

# In[46]:


driver=webdriver.Edge()


# In[47]:


url = ("https://github.com/")
driver.get(url)


# In[50]:


explore = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button").click()


trend_url = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/div[3]/ul/li[2]/a").Click()
urls = trend_url.get_attribute("href")
driver.get(urls)


# In[ ]:


URLs = []
repository_title = []
Description = []
Contributors = []
Language = []
lang = []


repository = driver.find_elements_by_xpath("//h1[@class='h3 lh-condensed']//a")
for i in repository:
    URLs.append(i.get_attribute("href"))
    

title = driver.find_elements_by_xpath("//h1[@class = 'h3 lh-condensed']")
for i in title:
    repository_title.append(i.text)
    

for i in URLs:
    driver.get(i)
    time.sleep(5)
    
    
    try:
        desc = driver.find_element_by_xpath("//p[@class='f4 mt-3']")
        Description.append(desc.text)
    except NoSuchElementException:
        Description.append('-')
        
        
    
    try:
        contributor = driver.find_element_by_xpath("//*[contains(text(),'    Contributors ')]")
        Contributors.append(contributor.text.replace('Contributors',''))
    except NoSuchElementException:
        Contributors.append('-')
    
    
    
    try:
        for i in driver.find_elements_by_xpath("//ul[@class= 'list-style-none']//li//span[1]"):
            lang.append(i.text)
        Language.append(lang)
    except NoSuchElementException:
        Language.append('-')
        
        

Github = pd.DataFrame({})
Github['Repository Title'] = repository_title
Github['Repository Description'] = Description
Github['Contributors Count'] = Contributors
Github['Language Used'] = Language
Github


# In[ ]:


driver.close()


# # 5. Scrape the details of top 100 songs on billiboard.com. Url = https:/www.billboard.com/ You have to find the 
# following details: 
# A) Song name 
# B) Artist name 
# C) Last week rank 
# D) Peak rank 
# E) Weeks on board 
#  Note: - From the home page you have to click on the charts option then hot 100-page link through code.

# In[55]:


driver=webdriver.Edge()


# In[56]:


url = ("https:/www.billboard.com/")
driver.get(url)


# In[57]:


charts=driver.find_element(By.XPATH,"//a[@class='header__main-link header__main-link--charts']").click()


# In[ ]:


Song_Name = []
Artist_Name =[]
Last_week_rank = []
Peak_rank = []
Weeks_on_board = []


urls = driver.find_element(By.XPATH,"//li[@class='header__submenu__list__element']//a")
page_url = urls.get_attribute("href")
driver.get(page_url)
time.sleep(4)


for i in driver.find_elements(By.XPATH,"//span[@class='chart-element__information__song text--truncate color--primary']"):
    Song_Name.append(i.text)
    

for i in driver.find_elements(By.XPATH,"//span[@class='chart-element__information__artist text--truncate color--secondary']"):
    Artist_Name.append(i.text)
    

for i in driver.find_elements(By.XPATH,"//div[@class='chart-element__meta text--center color--secondary text--last']"):
    Last_week_rank.append(i.text)
    


for i in driver.find_elements(By.XPATH,"//div[@class='chart-element__meta text--center color--secondary text--peak']"):
    Peak_rank.append(i.text)       
    
    

for i in driver.find_elements(By.XPATH,"//div[@class='chart-element__meta text--center color--secondary text--week']"):
    Weeks_on_board.append(i.text)
    
    

billiboard = pd.DataFrame({})
billiboard['Name'] = Song_Name
billiboard['Artist'] = Artist_Name
billiboard['Last Week Rank'] = Last_week_rank
billiboard['Peak Rank'] = Peak_rank
billiboard['Weeks on board'] = Weeks_on_board
billiboard


# # 6. Scrape the details of Highest selling novels. 
# A) Book name 
# B) Author name 
# C) Volumes sold 
# D) Publisher 
# E) Genre 
#  Url - https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare

# In[58]:


driver=webdriver.Edge()


# In[59]:


url = ("https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare")
driver.get(url)


# In[60]:


Book_name = []
Author_name = []
Volumes_sold = []
Publisher = []
Genre = []


# In[63]:


for i in driver.find_elements(By.XPATH,"//tbody//tr//td[2]"):
    Book_name.append(i.text)

    

for i in driver.find_elements(By.XPATH,"//tbody//tr//td[3]"):
    try:
        if i.text == '0' : raise NoSuchElementException
        Author_name.append(i.text)
    except NoSuchElementException:
        Author_name.append('-')
time.sleep(3)



for i in driver.find_elements(By.XPATH,"//tbody//tr//td[4]"):
    Volumes_sold.append(i.text)
    

for i in driver.find_elements(By.XPATH,"//tbody//tr//td[5]"):
    Publisher.append(i.text)
    
    

for i in driver.find_elements(By.XPATH,"//tbody//tr//td[6]"):
    Genre.append(i.text)    
    

Novels = pd.DataFrame({})
Novels['Book Name'] = Book_name
Novels['Author'] = Author_name
Novels['Volume sold'] = Volumes_sold
Novels['Publisher'] = Publisher
Novels['Genre'] = Genre
Novels 


# # Scrape the details most watched tv series of all time from imdb.com. 
# Url = https://www.imdb.com/list/ls095964455/ You have 
# to find the following details: 
# A) Name 
# B) Year span 
# C) Genre 
# D) Run time 
# E) Ratings 
# F) Votes

# In[64]:


driver=webdriver.Edge()


# In[65]:


url = ("https://www.imdb.com/list/ls095964455/")
driver.get(url)


# In[66]:


Name = []
Year_span = []
Genre = []
Run_time = []
Ratings = []
Votes = []


for i in driver.find_elements(By.XPATH,"//h3[@class='lister-item-header']/a"):
    Name.append(i.text)
    
    

for i in driver.find_elements(By.XPATH,"//span[@class='lister-item-year text-muted unbold']"):
    Year_span.append(i.text)
    
    

for i in driver.find_elements(By.XPATH,"//span[@class='genre']"):
    Genre.append(i.text)
    
    

for i in driver.find_elements(By.XPATH,"//span[@class='runtime']"):
    Run_time.append(i.text)
    
    

for i in driver.find_elements(By.XPATH,"//div[@class='ipl-rating-star small']//span[2]"):
    Ratings.append(i.text)
    
    

for i in driver.find_elements(By.XPATH,"//div[@class='lister-item-content']//p[4]/span[2]"):
    Votes.append(i.text) 
    
    

TV_Series = pd.DataFrame({})
TV_Series['Name'] = Name
TV_Series['Year Span'] = Year_span
TV_Series['Genre'] = Genre
TV_Series['Run Time'] = Run_time
TV_Series['Ratings'] = Ratings
TV_Series['Votes'] = Votes
TV_Series


# In[ ]:





# # 8. Details of Datasets from UCI machine learning repositories. 
# Url = https://archive.ics.uci.edu/ You 
# have to find the following details: 
# A) Dataset name 
# B) Data type 
# C) Task 
# D) Attribute type 
# E) No of instances 
# F) No of attribute G) Year 
#  Note: - from the home page you have to go to the Show All Dataset page through code.

# In[ ]:


driver=webdriver.Edge()


# In[ ]:


url = ("https://archive.ics.uci.edu")
driver.get(url)


# In[68]:


Dataset_name = []
Data_type = []
Task = []
Attribute_type = []
No_of_instances = []
No_of_attributes = []
Year = []


# In[69]:


viewall_dataset = driver.find_element(By.XPATH,"//tbody[1]//tr/td[2]/span[2]/a")
page_url = viewall_dataset.get_attribute("href")
driver.get(page_url)
time.sleep(3)

view_list = driver.find_element(By.XPATH,"/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/p/a")
list_url = view_list.get_attribute("href")
driver.get(list_url)
time.sleep(3)

dataset_url = driver.find_elements(By.XPATH,"//p[@class='normal']//b/a")

urls = []
for i in dataset_url:
    urls.append(i.get_attribute("href"))

Dataset_name = []
Data_type = []
Task = []
Attribute_type = []
No_of_instances = []
No_of_attributes = []
Year = []

for i in urls:
    driver.get(i)
    time.sleep(3)
    
    
    
    try:
        dataset_name = driver.find_element(By.XPATH,"//span[@class='heading']")
        Dataset_name.append(dataset_name.text)
    except NoSuchElementException:
        Dataset_name.append('-')
    time.sleep(3)
    
    
    
    
    try:
        data_type = driver.find_element(By.XPATH,"//table[@border='1']//tbody/tr/td[2]")
        if data_type.text == "N/A": raise NoSuchElementException
        Data_type.append(data_type.text)
    except NoSuchElementException:
        Data_type.append('-')
    time.sleep(3)
    
    
    
    try:
        task = driver.find_element(By.XPATH,"//table[@border='1']//tbody/tr[3]/td[2]")
        if task.text == "N/A": raise NoSuchElementException
        Task.append(task.text)
    except NoSuchElementException:
        Task.append('-')
    time.sleep(3)
    
    
    
    
    try:
        attribute_type = driver.find_element(By.XPATH,"//table[@border='1']//tbody/tr[2]/td[2]")
        if attribute_type.text == "N/A": raise NoSuchElementException
        Attribute_type.append(attribute_type.text)
    except NoSuchElementException:
        Attribute_type.append('-')
    time.sleep(3)
    
    
    
    
    try:
        instances = driver.find_element(By.XPATH,"//table[@border='1']//tbody/tr/td[4]")
        if instances.text == "N/A": raise NoSuchElementException
        No_of_instances.append(instances.text)
    except NoSuchElementException:
        No_of_instances.append('-')
    time.sleep(3)
    
    
    
    
    try:
        attribute = driver.find_element(By.XPATH,"//table[@border='1']//tbody/tr[2]/td[4]")
        if attribute.text == "N/A": raise NoSuchElementException
        No_of_attributes.append(attribute.text)
    except NoSuchElementException:
        No_of_attributes.append('-')
    time.sleep(3)
    
    
    
    try:
        year = driver.find_element(By.XPATH,"//table[@border='1']//tbody/tr[2]/td[6]")
        if year.text == "N/A": raise NoSuchElementException
        Year.append(year.text[:4])
    except NoSuchElementException:
        Year.append('-')
    time.sleep(3)


# In[70]:


ML = pd.DataFrame({})
ML['Data Name'] = Data_name 
ML['Data Type '] = Data_type
ML['Task '] = Task 
ML['Attribute Type '] = Attribute_type 
ML['No of Instance '] = No_of_instances
ML['No of Attributes '] = No_of_attributes 
ML['Year '] = Year 
ML


# In[ ]:




