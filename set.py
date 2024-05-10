thisset = {"apple", "banana", "cherry"}
print(thisset)

#len function
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#or
thisset = {"apple", "banana", "cherry"}
print(type(thisset))

#access set item
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#or
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#add set item
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print(thisset)
#update method
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)

#remove set item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

print(thisset)

#discard method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")

print(thisset)

#pop method
thisset = {"apple", "banana", "cherry"}
thisset.pop()

print(thisset)

#clear method
thisset = {"apple", "banana", "cherry"}
thisset.clear()

print(thisset)

#set for loop
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#join set-union method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#update method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

