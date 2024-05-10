import datetime
a = datetime.datetime.now()
print(a)

#or
import datetime

#a = datetime.datetime(2027,3,10)
a =datetime.datetime.now()

print(a.strftime("%B"))
print(a.strftime("%A"))
print(a.strftime("%d"))
print(a.strftime("%m"))
print(a.strftime("%h"))