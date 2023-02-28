#!/usr/bin/env python
# coding: utf-8

# # Loops using while and for :

# In[2]:


#write a program to print "hello python" ten times
i=1
while i<=10:
    print("hello python")
    i=i+1


# In[3]:


#write a program to print number from 1 to 10
i=1
while i<=10:
    print(i)
    i=i+1


# In[8]:


#write a program to print sum of frist five numbers
n=5
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)


# In[9]:


#write a program to print n numbers entered by the user
n=int(input("Enter n value:"))
for i in range(1,n+1):
    print(i,end=" ")


# In[10]:


#write a program to print sum of n numbers
n=int(input("Enter n value:"))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)


# In[11]:


#write a program to print table of a number
num = int(input("enter the number"))

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


# In[13]:


#write a program to calculate the factorial of a number
num = int(input("enter the number:"))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[23]:


#write a program to print even number between 1 to 100
num = int(input("enter the number"))
max = int(input("enter the number"))
while num <= max:
    if(num % 2 == 0):
        print("{0}".format(num))
    num = num + 1


# In[21]:


#write a program to print odd number between 1 to 100
num = int(input("enter the number"))
max = int(input("enter the number"))
i=0
while i<100:
    if i%2!=0:
        print (i)
    i=i+1


# In[10]:


#write a program to check wheather a given number is palindrome or not
temp = int(input("enter a number"))
reverse = int(input("enter a number"))
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")


# In[32]:


#write a program to find the factors of a number
number = int(input("Enter a number "))
print("The factors of {} are,".format(number))

for i in range(1,number+1):
    if number % i == 0:
        print(i)


# In[2]:


#write a program to print the reverse of a number
num = int(input("enter the number:"))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))


# In[8]:


# write a program to check wheather a given number id prime or not
num = int(input("enter the number:"))

if num > 1:

    for i in range(2, int(num/2)+1):
        
        
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# In[9]:


# write a program to print prime number between 1to100
min = int(input(" Please Enter the Minimum Value: "))
max= int(input(" Please Enter the Maximum Value: "))

for Number in range (min, max + 1):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')


# In[11]:


# write a program to print number in reverse order entered by the user
n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)


# In[1]:


# write a program to print the cube of all numbers from 1 to 9 given numbers


# In[2]:


#star pattren
for i in range(5):
    for j in range(i):
        print("&",end="")
    print()


# In[3]:


for i in range(5):#outer loop
    for j in range(i): #inner loop
        print(i,end="")
    print()


# In[7]:


for i in range(i,5):#outer loop
    for j in range(i+1): #inner loop
        print(i,end="")
    print()


# In[ ]:




