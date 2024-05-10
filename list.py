li = [1,3,5,7,9]
print(type(li))

li[1] = 4
print(li)

#or
list = ["hasan","najmul","taijul"]
print(list)
print(type(list))

#or
lis = [False,True,False,True]
print(type(lis))

#access list item

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(len(thislist))

#change list

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#add list

thislist = ["apple", "banana", "cherry"]
thislist.append("jackfruit")
print(thislist)

#insert method

thislist = ["apple", "banana", "cherry"]
thislist.insert(1,"orange")
print(thislist)

#remove list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop method
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#pop method()-delete last string
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#del method
thislist = ["apple", "banana", "cherry"]
del thislist[2]
print(thislist)

#clear method
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for x in range(len(thislist)):
  print(x)

#while loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#lost comprehension
num = [1,3,5,7,9]
for x in num:
    print(x*2)

#or
num = [1,3,5,7,9]
D = [x * 2 for x in num]
print(D)

#sort list method
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#sort list by num:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#or
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#copy list
thislist = ["apple", "banana", "cherry"]
d = thislist.copy()
print(d)

#join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#Or you can use the extend:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)



