
# coding: utf-8

# In[1]:

#find the min, maximum, sum, average
list=[22,33,44,6,77,88,56,55]
sum=0
print min(list)
print max(list)
for i in list:
    sum=sum+i
print"sum of the elements:",sum
avg=sum/len(list)
print"average of elements:",avg


# In[3]:

#31. Taake numbers from the user and findout min, maximum, sum, average
a=input("enter the values:")
print a
sum=0
print min(a)
print max(a)
for j in a:
    sum=sum+j
print"sum of elements:",sum
avg=sum/len(a)
print "average:",avg


# In[4]:

#l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists
l1=[1,2,3,4]
l2=[5,6,7,8]
sum=0
for i in l2:
    l1.append(i)
print l1
for j in l1:
    sum=sum+j
print"sum of the two lists:",sum


# In[5]:

#l=['1','2','3'] get the sum of the list
l=['1','2','3']
l1=[]
type(l)
for i in l:
    l1.append(int(i))
print l1
sum=0
for i in l1:
    sum=sum+i
print "sum of the list:",sum


# In[6]:

#input = 1,2,3,4,5,6,8,10 output = odd,even,odd,even,odd,even,even,even
input=[1,2,3,4,5,6,8,10]
for i in input:
    if i%2==0:
        print"even value:",i
    else:
        print"odd value:",i


# In[7]:

#Remove duplicates from the list: a=[1,2,3,2,3,4,1,,3,4]
list=[1,2,3,4,1,3,4]
d={}
d3=d.fromkeys(list,'0')
print d3
a=d3.keys()
print "list ofter removing the duplicates:",a


# In[8]:

#WAP> 10 -> 000010
#      100 ->  000100
#      1000 ->  001000
# 2345678  ->  2345678
input=raw_input("enter the value:")
print input.rjust(6,'0')


# In[9]:

#WAP> 10 -> 000010
#      100 ->  000100
#      1000 ->  001000
# 2345678  ->  2345678
input=raw_input("enter the value:")
print input.ljust(6,'0')


# In[10]:

##names ="emp1,emp2,emp3,emp4" iterate through the employee names.
names="emp1,emp2,emp3,emp4"
l=names.split(',')
for i in l:
    print i


# In[11]:

# Find third max value of element in a without sorting a list.
list=[1,2,3,33,44,99,7,444,78]
for i in xrange(len(list)):
    for j in xrange(len(list)):
        if list[i]>list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print"the sorted elements of the list:",list
print "the third max value of the element:",list[2]


# In[12]:

#find the third max value of element by sorting the list;
list=[33,44,55,66,88,4,56,8,213,67]
list.sort()
print "the sorted element of the list:",list
print"the third max value of the elements:",list[-3]


# In[13]:

#to check the given number is prime or not
num=raw_input("enter the number:")
prime=[]
for i in xrange(len(num)):
        count=0
    for j in range(2,len(num)):
        if(num[i]%j==0):
            count=1
    if count == 0:
        prime.append(i)
print"the prime numbers of the list:",prime       


# In[ ]:
## l2=[1,2,3,4,[6,7,8],[9,10]]
a=[1,2,3,4,[6,7,8],[9,10]]
a2=[]
for i in a:
    if type(i)==int:
        a2.append(i)
    elif type(i)==list:
        a2.extend(i)
print a2


