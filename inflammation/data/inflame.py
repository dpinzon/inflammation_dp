
# coding: utf-8

# In[47]:

import numpy
inarray = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
print inarray.shape


# In[14]:

a = numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print "our whole array is\n", a
print "the shape is ", a.shape


# In[20]:

a[1,1]
a[1,3]
a[0,:]
a[0,:2]


# In[27]:

a[:,2]. sum()


# In[28]:

a[0:2,0:3]


# In[29]:

a[2,:].max()


# In[38]:

maxes = inarray.max(axis=1)
print maxes.mean()


# maxes = array.max(axis=1)

# In[42]:

maxes = inarray.max(axis=1)


# In[46]:

data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
print data


# In[49]:

inarray[-10:].max(axis =1)
#brings the max for the first ten patients


# In[51]:

from matplotlib import pyplot as plt

get_ipython().magic(u'matplotlib inline')

image  = plt.imshow(inarray)
plt.show(image)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



