def cubes(n):

    result = []
    for i in range(n):
        result.append(i**3)
    return result


for j in cubes(3):
    print(j)


def cubes_with_generator(n):

    for i in range(n):
        yield i**3

cubes_with_generator(3)
print(type((cubes_with_generator(3))))

print(type(list(cubes_with_generator(3))))
for k in cubes_with_generator(3):
    print(k)