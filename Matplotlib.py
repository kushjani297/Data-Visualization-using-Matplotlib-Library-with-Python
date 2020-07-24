#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


import numpy as np
x = np.linspace(0,5,11)
y = x**2


# In[6]:


x


# In[7]:


y


# In[10]:


# Functional
plt.plot(x,y,'g-')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')


# In[18]:


plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')


# In[16]:


# Object Orinted Method
fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')


# In[23]:


fig=plt.figure()

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y,'r')
axes1.set_title('LARGER PLOT')

axes2.plot(y,x)
axes2.set_title('SMALLER PLOT')


# In[26]:


fig,axes = plt.subplots(nrows=1,ncols=2)

for new in axes :
    new.plot(x,y)


# In[31]:


fig,axes = plt.subplots(nrows=3,ncols=3)
plt.tight_layout()


# In[34]:


fig,axes = plt.subplots(nrows=1,ncols=2)

axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('Second Plot')


# ## Figure Size and DPI
# 

# In[38]:


fig = plt.figure(figsize=(8,2))

ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)


# In[40]:


fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))

axes[0].plot(x,y)

axes[1].plot(y,x)

plt.tight_layout()


# In[44]:


fig.savefig('Pic.jpg',dpi=200)


# In[45]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)

ax.set_title('Title')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')


# In[47]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.plot(y,x)


# In[53]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label = 'X Squared')
ax.plot(x,x**3,label = 'X Cubed')

ax.legend()


# ## Plot Appearance 
# 

# In[65]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,y,color = '#FF8C00',linewidth=3,alpha=0.5 ,linestyle='-.') # RGB Hex Code 
# thier is no need to write whole linewidth u can wit'lw' instead alsp 'ls'for line .


# In[74]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,y,color = 'purple',linewidth=3,linestyle='-',marker = 'o',markersize=10) #'*','1','+'


# In[77]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,y,color = 'purple',linewidth=3,linestyle='-',marker = 'o',markersize=10,
       markerfacecolor='yellow',markeredgewidth=3,markeredgecolor='green')


# In[81]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,y,color = 'purple',linewidth=3,ls='--')

ax.set_xlim([0,1])
ax.set_ylim([0,2])


# In[ ]:




