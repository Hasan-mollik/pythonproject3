a = 33
b = 200
if b > a:
  print("b is greater than a")

#Elif condition
a = 37
b = 33
if b > a:
  print("b is greater than a")
elif a>b:
  print("a is greater than b")

#or
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Else condition
a = 200
b = 33
if b > a:
  print("b is greater than a")

else:
  print("a is greater than b")

#or
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#or
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")
#or
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#The not keyword is a logical operator:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

