#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Opening the data.txt & storing values into a list

f = open("data.txt", "r")

numbersList = [float(ln.rstrip()) for ln in f] #the list will be called "numbersList"


# In[2]:


#To plot the graph, I must know the how many numbers there are.

#The nth item is 5473 in the data file.

#print(len(numbersList)) I used this to find out how many items.

#Check the unsorted list by erasing the hash.
#print(numbersList)

items = list(range(0,5473))  #This gives a list of numbers from 0 until 5473.

from matplotlib import pyplot as plt
plt.plot(numbersList, items)
plt.xlabel("data")
plt.ylabel("item")


# In[3]:


# Bubble sort algorithm/function made

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


# In[4]:


#The time function will begin as the bubble sort begins and stop as the bubble sort stops.

import time

data= list(numbersList) #Renaming the numbers list variable as "data"

start_time = time.time() #time starts
bubbleSort(data)         #algorithm starts at the same time
stop_time = time.time()  #Algorithm ends so the time is stopped and recorded.

duration = stop_time - start_time #total time between the two time functions

print('Sorted Array using Bubble Sort:')
print("time elapsed (1) = ",duration, "s")

#Newly sorted list: BubbleSort
#print(data1)


# In[5]:


#Gnome Sort algorithm/function
def gnomeSort(arr, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1
 
    return arr


# In[6]:


data2 = list(numbersList) #Renaming the numbers list variable

start_time2 = time.time()    #time starts
gnomeSort(data2, len(data2)) #algorithm starts at the same time
stop_time2 = time.time()     #Algorithm ends so the time is stopped and recorded.

duration2 = stop_time2 - start_time2  #total time between the two time functions
print('Sorted Array using Gnome Sort:')
print("time elapsed (2) = ",duration2, "s")

#Newly sorted list: Gnome
#print(data2)


# In[7]:


data2 = list(numbersList) #Renaming the numbers list variable
plt.plot(data2, items) #plot of the sorted data using the Gnome sort. Same outcome though.
plt.xlabel("data")
plt.ylabel("item")


# In[8]:


print("Bubble Sort is the faster algorithm, not Gnome Sort")
print()
print("The speed up percentage is from Gnome to Bubble", ((duration/duration2)*100),"%") 


# In[ ]:




