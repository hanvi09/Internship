#!/usr/bin/env python
# coding: utf-8

# In[65]:


get_ipython().system('pip install selenium')


# In[2]:


#Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
#have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
#jobs data.


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


driver.get("https://www.shine.com/")


# In[7]:


designation=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/input")
designation.send_keys('Data Analyst')


# In[8]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bangalore')                    


# In[11]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search.click()


# In[12]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]

    


# In[13]:


title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title_tags [0:10]:
    title=i.text
    job_title.append(title)
job_title


# In[84]:


location=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for j in location [0:10]:
    loc=j.text
    job_location.append(loc)
job_location


# In[85]:


company=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for k in company[0:10]:
    c=k.text
    company_name.append(c)
company_name


# In[86]:


experience=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for x in experience [0:10]:
    e=x.text
    experience_required.append(e)
experience_required


# In[87]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[88]:



df=pd.DataFrame({'title':job_title,'location':job_location,'Company':company_name,'Experience':experience_required})
df


# # Q2:Write a python program to scrape data for “Data Scientist” Job position in“Bangalore” location. You
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Scientist” in “Job title, Skills” field and enter “Bangalore” in “enter thelocation” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manuall

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


driver.get("https://www.shine.com/")


# In[5]:


designation=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/input")
designation.send_keys('Data Scientist')


# In[6]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bangalore')     


# In[7]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search.click()


# In[8]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[9]:


title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title_tags [0:10]:
    title=i.text
    job_title.append(title)
job_title


# In[10]:


location=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for j in location [0:10]:
    loc=j.text
    job_location.append(loc)
job_location


# In[11]:


company=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for k in company[0:10]:
    c=k.text
    company_name.append(c)
company_name


# In[12]:


experience=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for x in experience [0:10]:
    e=x.text
    experience_required.append(e)
experience_required


# In[13]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[14]:


df=pd.DataFrame({'title':job_title,'location':job_location,'Company':company_name,'Experience':experience_required})
df


# In[ ]:





# # In this question you have to scrape data using the filters available on the webpage 
#  You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get the web page https://www.shine.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the search button.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results you get.
# 6. Finally create a dataframe of the scrapeddata.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[15]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[16]:


driver = webdriver.Edge()


# In[17]:


driver.get("https://www.shine.com/")


# In[18]:


designation=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/input")
designation.send_keys('Data Scientist')


# In[19]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Delhi/NCR')  


# In[20]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search.click()


# In[21]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[22]:


title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title_tags [0:10]:
    title=i.text
    job_title.append(title)
job_title


# In[23]:


location=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for j in location [0:10]:
    loc=j.text
    job_location.append(loc)
job_location


# In[24]:


company=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for k in company[0:10]:
    c=k.text
    company_name.append(c)
company_name


# In[25]:


experience=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for x in experience [0:10]:
    e=x.text
    experience_required.append(e)
experience_required


# In[26]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[27]:


df=pd.DataFrame({'title':job_title,'location':job_location,'Company':company_name,'Experience':experience_required})
df


# # Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 6. Brand
# 7. ProductDescription
# 8. Price
# The attributes which you have to scrape is ticked marked in the below image.

# In[ ]:




