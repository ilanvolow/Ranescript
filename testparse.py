
from parser import *


fileFd = file("Abstract.rs", "r")
testString = fileFd.read()


q = RaneParser()
result = q.parse(testString)
print(result.namespace)
print(result.class_name)
print(result.super_class)
print(result.interfaces)