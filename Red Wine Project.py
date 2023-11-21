#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt  
import pandas as pd
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# In[3]:


df = pd.read_csv("winequality-red.csv")


# In[4]:


df.head()


# In[5]:


print(df.shape)


# In[6]:


df.tail()


# In[7]:


df.dtypes


# In[8]:


df.isnull().sum()


# In[9]:


sns.heatmap(df.isnull())


# In[10]:


df.describe()


# In[11]:


df.corr()


# In[12]:


df.groupby('quality').mean()


# DATA VISUALIZATION

# In[13]:


sns.countplot(df['quality'])
plt.show()


# In[14]:


sns.countplot(df['volatile acidity'])
plt.show()


# In[16]:


sns.countplot(df['fixed acidity'])
plt.show()


# In[17]:


sns.countplot(df['citric acid'])
plt.show()


# In[18]:


sns.countplot(df['residual sugar'])
plt.show()


# In[19]:


sns.countplot(df['chlorides'])
plt.show()


# In[20]:


sns.countplot(df['density'])
plt.show()


# In[21]:


sns.countplot(df['pH'])
plt.show()


# In[21]:


sns.countplot(df['sulphates'])
plt.show()


# In[22]:


sns.countplot(df['alcohol'])
plt.show()


# In[23]:


sns.distplot(df['alcohol'])
plt.show()


# In[24]:


sns.distplot(df['quality'])
plt.show()


# In[25]:


sns.distplot(df['fixed acidity'])
plt.show()


# In[26]:


sns.distplot(df['volatile acidity'])
plt.show()


# In[27]:


sns.distplot(df['citric acid'])
plt.show()


# In[28]:


sns.distplot(df['residual sugar'])
plt.show()


# In[29]:


sns.distplot(df['chlorides'])
plt.show()


# In[30]:


sns.distplot(df['density'])
plt.show()


# CHECKING FOR OUTLIERS BY PLOTTING BOXPLOT

# In[31]:


df.plot(kind ='box',subplots = True,layout =(4,4))
plt.tight_layout()


# In[32]:


df.hist(figsize=(10,10))
plt.tight_layout()


# In[33]:


sns.pairplot(df)


# In[35]:


df['goodquality'] = [1 if x >= 7 else 0 for x in df['quality']]
X = df.drop(['quality','goodquality'], axis = 1)
Y = df['goodquality']


# In[36]:


df['goodquality'].value_counts()


# In[37]:


X


# In[38]:


Y


# Feature Importance

# In[39]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

from sklearn.ensemble import ExtraTreesClassifier
classifiern = ExtraTreesClassifier()
classifiern.fit(X,Y)
score = classifiern.feature_importances_
print(score)


# Splitting Dataset

# In[40]:


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=7)


# LogisticRegression

# In[41]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score,confusion_matrix
print("Accuracy Score:",accuracy_score(Y_test,Y_pred))


# In[42]:


confusion_mat = confusion_matrix(Y_test,Y_pred)
print(confusion_mat)


# Decision Tree

# In[43]:


from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='entropy',random_state=7)
model.fit(X_train,Y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
print("Accuracy Score:",accuracy_score(Y_test,y_pred))


# Random Forest

# In[45]:


from sklearn.ensemble import RandomForestClassifier
model2 = RandomForestClassifier(random_state=1)
model2.fit(X_train, Y_train)
y_pred2 = model2.predict(X_test)

from sklearn.metrics import accuracy_score
print("Accuracy Score:",accuracy_score(Y_test,y_pred2))


# In[48]:


results = pd.DataFrame({
    'Model': ['Logistic Regression','Decision Tree' ,'Random Forest'],
    'Score': [0.868,0.864,0.893]})


# In[49]:


results


# In[ ]:





# In[ ]:




