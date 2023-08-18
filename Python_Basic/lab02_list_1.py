#!/usr/bin/env python
# coding: utf-8

# In[2]:


data = [ "서울","부산","대구","인천" ]


# In[3]:


data.append("천안")
print(data)


# In[4]:


data.insert(1, "경기")
data


# In[5]:


del data[0]
data


# In[6]:


data.remove("대구")
data


# In[7]:


data.sort()
data


# In[11]:


data.sort(reverse = True)
data


# In[14]:


i = 0
while i < len(data):
    if data[i] == "경기":
        print(i)
        break
    else:
        i += 1
