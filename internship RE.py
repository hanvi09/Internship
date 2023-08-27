#!/usr/bin/env python
# coding: utf-8

# QUESTION 1
Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
Sample Text- 'Python Exercises, PHP exercises.'
# In[3]:


import regex as re
sample_text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", sample_text))


# # QUESTION 2

# Question 2-  Write a Python program to find all words starting with 'a' or 'e' in a given string.

# In[13]:


import regex as re
sample_text = 'Python Regular Expression'
out = re.findall("[ae]\w+",sample_text)
print(out)


# QUESTION 3
Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.
# In[16]:


import regex as re
sample_text = 'Python Regular Expression'

print(re.findall(r"\b\w{4,}\b",sample_text))


# QUESTION 4
Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.
# In[24]:


import regex as re
sample_text = 'java j2ee php python Data Science World, A sample data'
print(re.findall(r"\b\w{3,5}\b",sample_text))


# QUESTION 5
Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

# In[25]:


import re
sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
for item in sample_text:
    
     print(re.sub("[()]","",item))


# QUESTION 6
Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

# In[26]:


import re
sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
y = []
for item in sample_text:
    x=re.sub(r" ?\([^)]+\)", "", item)
    y.append(x)
print(y)


# QUESTION 7 

# In[ ]:


Question 7- Write a regular expression in Python to split a string into uppercase letters.
Sample text: “ImportanceOfRegularExpressionsInPython”
Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]


# In[7]:


import regex as re
text =  "ImportanceOfRegularExpressionsInPython"
print(re.findall('[A-Z][a-z]*',text))


# QUESTION 8
Create a function in python to insert spaces between words starting with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

# In[32]:


import re
st = "RegularExpression1IsAn2ImportantTopic3InPython"
regx = re.sub(r"(\w)(\d)", r"\1 \2", st)
print(regx)


# QUESTION 9
Create a function in python to insert spaces between words starting with capital letters or with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython

# In[30]:


import re
st = "RegularExpression1IsAn2ImportantTopic3InPython"
regx = re.sub(r"(\d)(\w)", r"\0 \1 \2", st)
print(regx)


# QUESTION 10
Write a python program to extract email address from the text stored in the text file using Regular Expression.
Sample Text- Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com. 
Please contact us at hr@fliprobo.com for further information. 
Expected Output: 
['xyz@domain.com', 'xyz.abc@sdomain.domain.com']
['hr@fliprobo.com']

Note- Store given sample text in the text file and then extract email addresses.

# In[34]:


import re 
  

st1 = "Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com"
st2="Please contact us at hr@fliprobo.com for further information. "
  
lst = re.findall('\S+@\S+', st1) 
lst1 = re.findall('\S+@\S+', st2)
  
print(lst,lst1) 


# QUESTION 11
*Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
# In[39]:


import re
def st1(text):
        p = '^[a-zA-Z0-9_]*$'
        if re.search(p,  text):
                return 'Matched'
        else:
                return('Not matched')

print(st1("The quick brown fox jumps over the lazy dog."))
print(st1("Python_Exercises_1"))


# In[ ]:


QUESTION 12
Write a Python program where a string will start with a specific number. 


# In[41]:


import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(match_num('712-556655'))
print(match_num('56778768978-22-2345861'))


# In[ ]:


QUESTION 13
Write a Python program to remove leading zeros from an IP address


# In[52]:


import re
ip_address = "198.08.09.01"
remove_zero = re.sub('\.[0+]*', '.', ip_address)
print(remove_zero)


# In[ ]:


QUESTION 14
Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
Expected Output- August 15th 1947
Note- Store given sample text in the text file and then extract the date string asked format.


# In[53]:


import re
with open("sample.txt", "r") as t:
    sample_text = t.read()
pattern = r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(st|nd|rd|th)\s+\d{4}\b"
matches = re.findall(pattern, sample_text)
for match in matches:
    print(" ".join(match))


# In[ ]:


QUESTION 15:
    Write a Python program to search some literals strings in a string. 
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'


# In[59]:


import re
words = [ 'fox', 'dog', 'horse' ]
sample_text = 'The quick brown fox jumps over the lazy dog.'
for x in words:
    print('Searching for "%s" in "%s" ->' % (x, sample_text),)
    if re.search(x,  sample_text):
        print('Matched!')
    else:
        print('Not Matched!')

Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'

# In[ ]:




QUESTION 17:Write a Python program to find the substrings within a string.
Sample text : 'Python exercises, PHP exercises, C# exercises'
Pattern : 'exercises'.

    


# In[60]:


import re
sample_text = 'Python exercises, PHP exercises, C# exercises'
word = 'exercises'
for match in re.findall(word, sample_text):
    print('Found "%s"' % match)


# In[ ]:


QUESTION 18 Write a Python program to find the occurrence and position of the substrings within a string.


# In[62]:


import re
sample_text = 'Python exercises, PHP exercises, C# exercises'
word = 'exercises'
for match in re.finditer(word, sample_text):
    start = match.start()
    end = match.end()
    print('Found "%s" at %d:%d' % (sample_text[start:end], start, end))


# In[ ]:


QUESTION 19 Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.


# In[63]:


import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Date YYY-MM-DD Format: ",dt1)
print("New date DD-MM-YYYY Format: ",change_date_format(dt1))


# In[ ]:


QUESTION 21


# In[64]:


import re

text = "The following example 67 creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())
	


# In[ ]:


Question 23- Create a function in python to insert spaces between words starting with capital letters.


# In[65]:


import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("RegularExpressionIsAnImportantTopicInPython"))


# In[ ]:


Question 24- Python regex to find sequences of one upper case letter followed by lower case letters


# In[66]:


import re
def text_match(text):
        regx  = '[A-Z]+[a-z]+$'
        if re.search(regx, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("Regular"))
print(text_match("regular"))
print(text_match("Expression"))
print(text_match("expression"))
print(text_match("regex"))
print(text_match("Aaaaaaaa"))


# In[ ]:


Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.


# In[67]:


import re


def Remove_Duplicates(Test_string):
      regx = r"\b(\w+)(?:\W\1\b)+"
      return re.sub(regx, r"\1", Test_string)
Test_string1 = "Hello hello world world"
print(Remove_Duplicates(Test_string1))


# In[ ]:


Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.


# In[71]:


import re

regex = '[a-zA-z0-9]$'

def check_string(my_string):

   if(re.search(regex, my_string)):
      print("Aplhanuemric exist")

   else:
      print("Not exist")


my_string_1 = "##Python@"
print("The string is :")
print(my_string_1)
check_string(my_string_1)

my_string_2 = "Python1245"
print("\nThe string is :")
print(my_string_2)
check_string(my_string_2)


# In[ ]:


Question 27-Write a python program using RegEx to extract the hashtags.
Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']


# In[73]:



def extract_hashtags(text):


    hashtaglist = []

    for word in text.split():


        if word[0] == '#':


            hashtaglist.append(word[1:])


    print("Hashtags are :")
    for hashtag in hashtaglist:
        newlist = []
        newlist.append(hashtag)
        print(newlist)


if __name__ == "__main__":
    text1 = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
    
    extract_hashtags(text1)
    


# In[ ]:


Question 28- Write a python program using RegEx to remove <U+..> like symbols
Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders


# In[39]:


import re

my_str = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

result = re.sub(r'[U+]', '', my_str)
print(result)  


# In[ ]:




