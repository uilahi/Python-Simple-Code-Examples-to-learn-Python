from functools import reduce
output = reduce(lambda x,y: x+y, [10,20,30])
print(output)