thistuple = ("apple", "banana", "cherry")
print(thistuple)

#To determine how many items a tuple has, use the len() function:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#or
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#tuple access
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#negative index
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#range of index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#or
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#update tuple

x = ("apple", "banana", "cherry")
y = list(x)
y.append("orange")
print(y)

z =tuple(y)
print(z)

#unpack tuple
fruits = ("apple", "banana", "cherry")
(a,b,c) = fruits
print(a)
print(b)
print(c)

#Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(*yellow, green) = fruits
print(yellow)
print(green)

#or
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits
print(red)
print(green)

#tuple for loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#range and len
thistuple = ("apple", "banana", "cherry")
for x in range(len(thistuple)):
  print(x)
  print(thistuple[x])

#tuple while loop
thistuple = ("apple", "banana", "cherry")
x = 0
while x < len(thistuple):
  print(thistuple[x])
  x +=  1

#join tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#tuple method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(7)
print(x)

#or
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(1)
print(x)
