#!/usr/bin/env python
# coding: utf-8

# In[1]:


#swap
x=int(input('Enter number1:'))
y=int(input('Enter number2:'))
print('Before swapping values:',x,y)
x=x+y
y=x-y
x=x-y
print('After swapping values:',x,y)


# In[2]:


#area of rectangle
x=int(input('Enter the length of reactangle:'))
y=int(input('Enter the breth of reactangle:'))
area=0
area=x*y
print('Area of rectangle:',area)


# In[4]:


#convert temparature
celcius=float(input('Enter the celcius temparature:'))
fahrenhite=0
fahrenhite=float((c*9/5)+32)
print('Fahrenheit temparature:',fahrenhite)


# In[6]:


#string length
string=input('Enter the string:')
print('The string length is:',len(string))


# In[9]:


#vowel count
string=input('Enter the string:')
vowel="aeiouAEIOU"
count=0
for i in string:
    if(i in vowel):
        count=count+1
print('The number of vowels are:',count)


# In[10]:


#string reverse using slicing
string=input('Enter the string:')
reverse=string[::-1]
print('The reverse string is:',reverse)


# In[14]:


#palindrome
string=input('Enter the string:')
reverse=string[::-1]
if (string==reverse):
    print(reverse,'is the palindrome of',string)
else:
     print(reverse,'is not the palindrome of',string)


# In[17]:


#replace space
string=input('Enter the string:')
print('The string witout space is:',string.replace(" ",""))

