#!/usr/bin/env python
# coding: utf-8

# # # Dictionary

# In[3]:


d= {'key1':'value','key2':123 }


# In[5]:


d['key1']


# In[6]:


d['key2']


# # # List Inside a Dictionary

# In[9]:


d = {'k1':[1,2,3]} 


# In[10]:


d['k1']


# In[11]:


d['k1'][1]


# In[12]:


my_list = d['k1']


# In[13]:


my_list


# # # Nested Dictionary

# In[14]:


d = {'k1':{'innerkey':[1,2,3]}}


# In[15]:


d['k1']


# In[16]:


d['k1']['innerkey']


# In[17]:


d['k1']['innerkey'][1]


# # # Boolean

# In[18]:


True


# In[19]:


False


# # # Tuple

# In[20]:


t = (1,2,4)


# In[21]:


t[0]


# NOTE:~ Tuple cannot be changed, they are immutable

# # # Sets

# A sets is a collection of unique element

# In[22]:


{1,2,3}


# In[23]:


{1,1,1,2,2,2,3,3,3,3,3}


# In[24]:


# Using hte set() function to get the unique element 
set([1,1,1,2,2,2,3,3,3,4,4,4])


# In[25]:


s = {1,2,3}


# In[26]:


s.add(5)


# In[27]:


s


# In[28]:


s.add(5)


# In[29]:


s


# # # Loops

# In[30]:


seq = [1,2,3,4,5]


# In[31]:


for item in seq:
    print(item)


# In[32]:


for num in seq:
    print("Hello")


# In[34]:


i=1;
while i<5:
    print("i is: {}".format(i))
    i = i+1


# # # Useful Function 

# 1.Range function

# In[35]:


for x in range(0,5):
    print(x)


# In[36]:


# Converting range to List\
list(range(0,5))


# In[37]:


list(range(10))


# # # List Comprehension

# In[38]:


x = [1,2,3,4]


# In[39]:


out = []

for num in x:
    out.append(num**2)


# In[40]:


print(out)


# In[41]:


# List Comprehension
[num**2 for num in x]


# In[42]:


out = [num**2 for num in x]


# In[43]:


out


# # # Functions

# In[44]:


# Function Defination
def my_func(param1):
    print(param1)


# In[45]:


# Function Call
my_func('hello')


# In[48]:


def my_func(name):
    print('Hello '+name)


# In[49]:


my_func('Diwas')


# In[50]:


def my_func(name='Default name'):
    print('Hello '+name)


# In[51]:


my_func()


# In[52]:


def square(num):
    return num**2


# In[53]:


output = square(2)


# In[55]:


output


# In[ ]:




