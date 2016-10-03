
# coding: utf-8

# Q. Check if a number is a prime number.

# In[9]:

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return "The number is not a prime number"
    else:
        return "The number is a prime number"


# In[11]:

is_prime(97)


# This code is just an example of creating a function. The Time complexity of the code can be improved with another approach.

# In[ ]:



