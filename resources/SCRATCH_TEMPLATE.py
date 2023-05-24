#!/usr/bin/env python3

import json, re, os


################
#### SUBSTRING AND REPLACE
b = "Hello, World!"
print(b[7:12])

b = "Hello, World!"
print(b[:5])

a = "Hello, World!"
print(a.replace("H", "J"))


################
#### IF STATEMENT
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b or b < c:
  print("a and b are equal or c is larger than b")
else:
  print("b is not greater than a and so on...")


################
#### LOOP
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


################
#### JSON FILE
myDict =  { "name":"John", "age":30, "city":"New York" }

with open(os.getenv("HOME") + "/Desktop/py_scratches/test.json", "w") as outfile:
    outfile.write(json.dumps(myDict))

f = open(os.getenv("HOME") + "/Desktop/py_scratches/test.json", "r")
jsonOutput = json.loads(f.read())
print(jsonOutput)


################
#### FUNCTION AND GLOBAL VAR
x = "awesome"
def myfunc():
  global x 
  x += " and fantastic"
  print("Python is " + x)

myfunc()


################
#### REGEX
testString = "abc@gmail.com xyz@gmail.com"
resultString = re.sub("[a-z]*@", "test@", testString)
print(resultString)
