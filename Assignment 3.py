#!/usr/bin/env python
# coding: utf-8

# # Assignment 3

# Assignment during session :
# 
# Your task:
# 
# Take input for the gift_presented_to[] list and print its respective gift_received_from[] list.

# In[38]:


#Taking input, single digit with single space
x=list(map(int, input('gift_presented_to:').strip().split()))

if x[0]!=1:  
    print('Person P1 has received gift from person P',x[0])
    print('Person P',x[0], 'has received gift from person P', x[1])
    print('Person P',x[1], ' has received gift from person P',x[2])
    print('Person P',x[2], ' has received gift from person P',x[3])
    print('Person P',x[3], ' has received gift from person P',x[3])
else:
    print('First person can not be 1')


# In[ ]:




