numbers = range(1,10)

output_even = filter(lambda x: x%2==0,numbers)
output_odd = filter(lambda x: x%2,numbers)
print("\nOutput of filter+lambda func without converting to list")
print(output_even)

print("\nOutput of filter+lambda func satifying even condition after converting to list")

print(list(output_even))
print("\nOutput of filter+lambda func satifying odd condition after converting to list")

print(list(output_odd))

