
# coding: utf-8

# In[1]:


#Printing prime number between 1-100 in single line of cod
print([x for x in range(2,100) if (0 not in [x % i for i in range(2,x)])])

