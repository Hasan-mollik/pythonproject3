#findall function
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#research function
import re

txt = "The rain in Spain"
x = re.search("portugal", txt)
print(x)

#spilit function
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#sub function
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)