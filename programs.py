
# coding: utf-8

# In[1]:

#print even and odd elements 
print"program started"
list=[1,2,3,45,6]
even=[]
odd=[]
for i in list:
    if i%2==0:
        print "the even number:",i
        even.append(i)
    else:
        print"the odd number:",i
        odd.append(i)
print"the even elements:",even
print"the odd elements:",odd
print"program ended"


# In[2]:

print "program started"
str="python"
str_1="pyt"
print str_1 in str


# In[3]:

#program to check given number is even or odd
print"started the program"
a=raw_input("enter an input:")
if int(a)%2 == 0:
    print "enter number is even",a
else:
    print "enter number is odd",a


# In[4]:

#string contine one upper character or not
s=raw_input("enter a valid input:")
count=0
for i in s:
    if i.isupper():
        count=count+1
if count==1:
    print"string have one capital letter"
elif count ==0:
    print"string not have any capital letters"
else:
    print"string contain more than one capital letter"
    print "the number of capitals in the string:",count
print"program ended"


# In[5]:

#string contine one lower character or nnot
j=raw_input("enter a valid input:")
count=0
for i in j:
    if i.islower():
        count=count+1
if count == 1:
    print"string have one lower letter"
elif count == 0:
    print"string don't have any lower letters"
else:
    print"string have mmore than one lower letters"
    print"number of lower cases in the string:",count


# In[7]:

#the string contine at least one bigit
k=raw_input("enter a valid input:")
count=0
for i in k:
    if i.isdigit():
        count=count+1
if count==1:
    print"string contine one number"
elif count == 0:
    print"string don't have any numbers"
else:
    print"string containe more than one number"
    print"the number of bigits in the string:",count


# In[8]:

#bigest element of the list
list=[20,30,40,59,22,33,5]
big=0
for i in list:
    if i>big:
        big=i
print "the big element of the list:",big


# In[9]:

#findout big of two numbers
a=raw_input("enter a value:")
b=raw_input("enter b value:")
if a>b:
    print a,"is the big of two mumbers"
else:
    print b,"is the big of two numbers"
    


# In[11]:

#first 100 odd elements 
num =range(1,1000)
odd=[]
for i in num:
    if i%2 == 1:
        odd.append(i)
count=len(odd)
for j in odd:
    if count <=100:
        print j


# In[14]:

#check string have only small leters or not
str=raw_input("enter the string:")
count=0
a=len(str)
for i in str:
    if i.islower():
        count=count+1
if count==a:
    print"the string contine only small letters"
else:
    print"string contine other letters"


# In[21]:

#check string contine only digits or not
dig=raw_input("enter the string:")
count=0
b=len(dig)
for i in dig:
    if i.isdigit():
        count=count+1
if count==b:
    print"the string have only digits"
else:
    "print the string have other letters"
    


# In[22]:

#check string containe only capitals or not 
cap=raw_input("enter the string:")
count=0
c=len(cap)
for i in cap:
    if i.isupper():
        count=count+1
if count==c:
    print"the string have all capitals"
else:
    print"the string have other values"


# In[23]:

#the given number is prime or not
num="enter a value:"
if num > 1:
    for i in range(2,num):
        if(num%i==0):
            print"num is a not a prime"
        else:
            print"num is not a prime"
    


# In[ ]:



