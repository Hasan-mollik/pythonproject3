x = 1
while x < 6:
  print(x)
  x += 1

#break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#or
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

  #or
  fruits = ["apple", "banana", "cherry"]
  for x in fruits:
    if x == "banana":
      continue
    print(x)

#else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
