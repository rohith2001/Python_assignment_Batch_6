#!/usr/bin/env python
# coding: utf-8

# In[2]:


print(" sum of n numbers with help of for loop. ")
n = 10
sum = 0
for num in range(0, n+1, 1):
    sum = sum+num
print("Output: SUM of first ", n, "numbers is: ", sum )


# In[3]:


print(" sum of n numbers with help of while loop. ")
num = int(input("Enter the value of n: "))
hold = num 
sum = 0 


if num <= 0: 
    print("Enter a whole positive number!") 
else: 
    while num > 0: 
        sum = sum + num 
        num = num - 1;
        # displaying output 
print("Sum of first", hold, "natural number is: ",sum)


# In[4]:


print("Take an integer and find whether the number is prime or not")
#input from user
number = int(input("Enter any number: ")) 
# prime number is always greater than 1
if number > 1: 
    for i in range(2, number):
        if (number % i) == 0: 
            print(number, "is not a prime number")
            break 
    else: print(number, "is a prime number")
        # if the entered number is less than or equal to 1 
        # then it is not prime number 
else: print(number, "is not a prime number")


# In[ ]:




