class baba:
    car = "toyoto"
    taka = "7 crore"
    home = "9th floor"

class kaka(baba):
    brokenhome = ""
    brokenphone =""

k = kaka()
print(k.taka)

#multiple inheritance
class baba:
    car = "toyoto"
    taka = "7 crore"
    home = "9th floor"

class baba2:
    smartphone ="Iphone"
    Airconditioner ="Walton"
    Microphone ="fifine"

class baba3:
    webcam = "Iphone"
    AC = "Walton"
    microphone = "fifine"

class kaka (baba,baba2,baba3):
    brokenphone =""
    brokenhome =""

k = kaka()
print(k.webcam)
print(k.AC)
print(k.microphone)

#Multilevel inheritance
class baba:
    car = "toyoto"
    taka = "7 crore"
    home = "9th floor"

class son1(baba):
    smartphone ="Iphone"
    Airconditioner ="Walton"
    Microphone ="fifine"

class son2(son1):
    webcam = "Iphone"
    laptop = "HP"
    microphone = "fifine"

class son3 (son2):
    brokenphone =""
    brokenhome =""

k = son3

print(k.home)
print(k.laptop)
print(k.smartphone)

