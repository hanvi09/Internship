#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('medical_cost_insurance.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.dtypes


# In[7]:


df.isnull().sum()


# In[8]:


sns.heatmap(df.isnull())


# In[9]:


df.describe()


# In[10]:


df.corr()


# In[11]:


df.info()


# In[12]:


categorical_column=[]
for i in df.dtypes.index:
    if df.dtypes[i]=='object':
        categorical_column.append(i)
        print(categorical_column)


# In[13]:


df.describe(include=['O'])


# In[14]:


numerical_column=[]
for i in df.dtypes.index:
    if df.dtypes[i]!='object':
        numerical_column.append(i)
        print(numerical_column)


# In[15]:


sns.countplot(df['sex'])
plt.show()


# In[16]:


import warnings
warnings.filterwarnings('ignore')


# In[18]:


sns.countplot(df['smoker'])
plt.show()


# In[19]:


sns.countplot(df['region'])
plt.show()


# In[20]:


sns.boxplot(df['age'])
plt.show()


# In[21]:


sns.histplot(df['age'])
plt.show()


# In[23]:


sns.distplot(df['age'])
plt.show()


# In[24]:


sns.boxplot(df['bmi'])
plt.show()


# In[25]:


sns.histplot(df['bmi'])
plt.show()


# In[26]:


sns.distplot(df['bmi'])
plt.show()


# In[27]:


sns.distplot(df['children'])
plt.show()


# In[28]:


sns.boxplot(df['children'])
plt.show()


# In[29]:


sns.histplot(df['children'])
plt.show()


# In[30]:


sns.boxplot(df['charges'])
plt.show()


# In[31]:


sns.distplot(df['charges'])
plt.show()


# In[33]:


sns.histplot(df['charges'])
plt.show()


# In[34]:


df.plot(kind ='box',subplots = True,layout =(4,4))
plt.tight_layout()


# In[35]:


sns.pairplot(df)


# In[36]:


df.head()


# In[38]:


# divide data set in to features and label
y = df[charges]
x = df.drop(charges,axis=1)

print(x)


# In[39]:


X = df.iloc[:, :-1]
Y = df.iloc[:, -1]


# In[40]:


X


# In[41]:


Y


# Splitting Dataset

# In[42]:


# Converting data to categorical type data
df[['region','sex','smoker']] = df[['region','sex','smoker']].astype('category')
df.dtypes


# In[44]:


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=7)


# In[48]:


from sklearn.linear_model import LinearRegression
LinearRegression = LinearRegression()
LinearRegression = LinearRegression.fit(X_train, Y_train)

# Prediction:
y_pred = LinearRegression.predict(X_test)

# Scores:
print(r2_score(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))


# In[47]:


# Converting Data to numerical type using LabelEncoder
from sklearn.preprocessing import LabelEncoder

label = LabelEncoder()

label.fit(df.region.drop_duplicates())
df.region = label.transform(df.region)

label.fit(df.sex.drop_duplicates())
df.sex = label.transform(df.sex)

label.fit(df.smoker.drop_duplicates())
df.smoker = label.transform(df.smoker)

df.dtypes


# In[62]:


from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(X_train,Y_train)
y_pred = LR.predict(X_test)
print('R2_score',r2_score(y_test,y_pred))
print('MAE',mean_absolute_error(y_test,y_pred))


# In[53]:


df.isnull().sum()


# In[54]:


df.duplicated().sum()


# In[55]:


df.drop_duplicates(inplace=True)


# In[56]:


df.nunique()


# In[58]:



df.head()


# In[59]:


X = df.drop('charges', axis = 1)
y = df['charges']


# In[61]:


LR = LinearRegression()
LR.fit(X_train,Y_train)
y_pred = LR.predict(X_test)
print('R2_score',r2_score(y_test,y_pred))
print('MAE',mean_absolute_error(y_test,y_pred))


# In[ ]:





# In[ ]:




