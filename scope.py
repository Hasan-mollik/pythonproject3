def myfunc():
  x = 300
  print(x)

myfunc()

#Global scope
x = 700

def myfunc():
  print(x)

myfunc()

print(x)