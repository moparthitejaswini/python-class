
# coding: utf-8

# In[2]:

b=20


# In[3]:

print b


# In[4]:

a=100
b=200
c=a
a=a+10
print a
print b


# In[5]:

a=100
b=200
a=b
a=a+b
print a
print b


# In[6]:

a=22.4
print a


# In[7]:

#sum of two float values
s1=10.24
s2=25.44
print s1+s2


# In[8]:

#sum of float and int
s1=17.4566
s2=100
print s1+s2


# In[9]:

#sum of two int
s1 = 10
s2=20
print s1+s2


# In[10]:

#sum of string and int
s1="str"
s2=10
print s1+s2


# In[11]:

print str(s1)+int(s2)
                


# In[12]:

s1=20
s2=40
print int(s1)+int(s2)
                


# In[13]:

print 10+20*10/2


# In[14]:

price=24.4
price_str=price
result="product price: "+price_str


# In[16]:

price=24.4
price_str=str(price)
result="product price: "+price_str
print result


# In[17]:

price=26.55555
print int(price)


# In[19]:

a1=23
b1=34
print int(a1)/int(b1)
print a1*b1
print a1+b1
print a1**b1


# In[22]:

#sum of int and float
a1=24
a2=34.44
print a1/a2


# In[23]:

a="anusha"
b=23
print a+b


# In[24]:

a=21.22
b="teja"
print a+b


# In[25]:

a=22
b="teja"
print str(b)+int(a)


# In[26]:

a=23.45666
b=34
print 10+24+a*b+a**b


# In[27]:

a=15
b=3
print a/b


# In[28]:

a=17
b=3
print a/b


# In[29]:

a=17
b=3
print int(a)/int(b)


# In[30]:

a=23.3455
b=5
print int(b)/float(a)


# In[31]:

a="anusha"
b="teja"
print a+b


# In[32]:

print a + b


# In[34]:

a="anusha "
b="teja"
print a+b


# In[35]:

a="anusha  "
b="teja"
print a+b


# In[36]:

a="anusha "
b="teja"
print a+b


# In[37]:

a=22.444
print a


# In[38]:

print int(a)


# In[39]:

a=223.4444
b=45.66666
print int(a)+int(b)


# In[40]:

print "anusha"+"teja"


# In[41]:

print "anusha "+"teja"


# In[42]:

print "anusha "+" teja "+"chandu"


# In[43]:

print "anusha "+"teja "+"chandu"


# In[44]:

print "anusha "+"23"+"chandu"


# In[45]:

s1=10
s2=20

print s1+s2


# In[46]:

s1=22.44
s3=s1
print s3


# In[48]:

s1=10.23
s2=int(s1)
print s2


# In[51]:

a=244.444
b=44
print a/b
print float(a)/b
print float(a)/float(b)
print float(a/b)


# In[52]:

print 3*1**3


# In[53]:

print 14/4+5


# In[54]:

print 5+10/5


# In[56]:

name='teja'
age=30
hight=1.5
print "name:",name,"age:",age,"hight:",1.5

print "name: "+name

# In[60]:

name=teja
print "name: "+str(name)


# In[62]:

s1=teja
print "name: "


# In[63]:

print name 


# In[64]:

print 'hello world'


# In[65]:

print"name:"


# In[66]:

s1=teja
print"name:"


# In[67]:

name=teja
print type(name)


# In[68]:

print id(name)


# In[69]:

print typ(name)


# In[70]:

a=22
print typ(a)


# In[71]:

print a


# In[72]:

price=24.4
print price


# In[73]:

a=24.4
print"the persentage of the student :",price


# In[74]:

name=teja
print "name:",name


# In[75]:

s1=teja
print"name :",s1


# In[76]:

print "name: ",str(s1)


# In[78]:

s1=10.24
print"name",s1


# In[87]:

a1=raw_input("enter a name:")
a2=raw_input("enter a age:")
a3=raw_input("enter a hight of the person:")
print "name: "+a1+"age: "+a2+"hight: "+a3


# In[90]:

print"line1\nline2"



# In[93]:

print"line1\tline2"


# In[94]:

print"%s%d%f%r"


# In[95]:

print"%s%d%f%r",('str1',22,2.1,(1,2,3))


# In[97]:

print"%s%d%f%r"%('str1',22,2.11,(1,2,3))


# In[103]:

print"%r"%("24")


# In[104]:

print"line\\line2"


# In[107]:

comment=r"teja\ndata\ttime\t23"
print comment


# In[108]:

str="hello world"


# In[109]:

print str


# In[111]:

s="hello world"
print s[0]


# In[112]:

print s[0:3]


# In[114]:

print s[3:7]


# In[115]:

print s[7:3]


# In[117]:

print s[7:3:-1]


# In[118]:

print s[-1]


# In[120]:

print s[0:10:-1]


# In[121]:

print s[::-1]


# In[122]:

print s[0:12:2]


# In[124]:

print s[0:12:1]


# In[125]:

print s.upper()


# In[126]:

print s.lower()


# In[130]:

print s.startwith("h")


# In[142]:

s="hello world"
a=s.split(" ")
print a


# In[143]:

s.count(o)


# In[144]:

print s.count("o")


# In[145]:

s.index("h")


# In[146]:

s.index("o")


# In[147]:

print s[1::2]


# In[148]:

print s[:6]


# In[149]:

print s[6:]


# In[150]:

print s[-5:]


# In[151]:

print s[-3:]


# In[152]:

s="hello world"
print s.count("h")


# In[153]:

print s.split("o")


# In[155]:

print s.index("h")

print s.upper()
# In[156]:

print s.lower()


# In[157]:

s="hello world"
print s.capitalize()


# In[159]:

s="hello WORLd"
print s.capitalize()


# In[ ]:

print"program started"
for i in "python program":
    if i==" ":
        continue
    print i
print"program ended"
    


# In[ ]:

print "program started"
i=0
while i<3:
    print"enter a valid value"
    print i
    i=i+1
print "program ended"


# In[ ]:

print"program startted"
for i in "python":
    print"iteration started"
    print i
print"program ended"


# In[ ]:



