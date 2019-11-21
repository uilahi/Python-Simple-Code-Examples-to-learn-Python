def add_numbers_to_100(n):
    return 100+n
number_to_add = [1,2,3,4]
output_map = map(add_numbers_to_100,number_to_add)
print("Output of only map func without converting to list")
print(output_map)
print("\nOutput of only map func after converting to list")
print(list(output_map))

output_map_lambda = map(lambda n: 100+n, number_to_add)
print("\nOutput of map+lambda func after converting to list")
print(list(output_map_lambda))


a= [10,20,30]

b = [8,9]

output_map_lambda_multiple_list_args = map(lambda n,x,y: n+x+y, number_to_add, a, b)
print("\nOutput of map+lambda func with multiple args  after converting to list")
print(list(output_map_lambda_multiple_list_args))

