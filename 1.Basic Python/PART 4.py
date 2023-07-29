#!/usr/bin/env python
# coding: utf-8

# # # Map and Filter Function

# In[1]:


def times(var):
    return var*2


# In[2]:


times(5)


# In[3]:


# map()


# In[4]:


seq = [1,2,3,4,5]


# In[5]:


# Now if we want to apply times function to the entire list "seq", then for that we use map() function


# In[7]:


map(times,seq)


# In[8]:


list(map(times,seq))


# # # lambda function

# In[9]:


# changing the times function to lambda function


# In[10]:


# def times(var):return var*2
t = lambda var:var*2


# In[11]:


t(6)


# In[12]:


# The above function is not the way we want to apply
# We want to apply the lambda function inside the map() function


# In[13]:


list(map(lambda num: num*3,seq))


# # # Filter Function

# In[14]:


filter(lambda num: num%2 == 0,seq)


# In[16]:


list(filter(lambda num:num%2 == 0,seq))


# In[17]:


s = 'hello my name is Sam'


# In[18]:


s.lower()


# In[19]:


s.upper()


# In[20]:


s.split()


# In[21]:


tweet = 'Go Sports! #Sports'


# In[23]:


tweet.split()


# In[24]:


tweet.split('#')


# In[25]:


tweet.split('#')[1]


# In[26]:


#DICTIONARY


# In[27]:


d = {'k1': 1,'k2':2}


# In[28]:


d


# In[29]:


d.keys()


# In[30]:


d.items()


# In[31]:


d.values()


# In[32]:


lst = [1,2,3]


# In[33]:


lst.pop()


# In[34]:


lst


# In[35]:


lst = [1,2,3,4,5]


# In[36]:


item = lst.pop()


# In[37]:


lst


# In[38]:


item


# In[39]:


first = lst.pop(0)


# In[40]:


lst


# In[41]:


first


# In[42]:


lst.append('new')


# In[43]:


lst


# # # in operator

# In[44]:


'x' in [1,2,3]


# In[45]:


'x' in ['x','y','z']


# # # Tuple Unpacking

# In[46]:


x = [(1,2),(3,4),(5,6)]


# In[47]:


x[0]


# In[48]:


x[0][0]


# In[49]:


for item in x:
    print(item)


# In[50]:


# Tuple unpacking
for (a,b) in x:
    print(a)


# In[51]:


for (a,b) in x:
    print(b)


# In[ ]:




