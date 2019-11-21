import re

str = "The rain in Spain"

x = re.search(r"\bS\w+", str)
print("========================")
print(x.string)
print("========================")

print(x.span())
print("========================")

print(x.group())
print("========================")

x = re.findall("Portugal", str)
print(x)
print("========================")

x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())
print("========================")

x = re.search("Portugal", str)
print(x)
print("========================")

x = re.split("\s", str)
print(x)
print("========================")

x = re.split("\s", str, 1)
print(x)
print("========================")

x = re.sub("\s", "9", str)
print(x)
print("========================")

x = re.sub("\s", "9", str, 2)
print(x)
print("========================")

x = re.search("ai", str)

print(x)
print("========================")
