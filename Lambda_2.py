from functools import reduce

numbers =[1,2,3,4,5,1]

total = reduce(lambda acc,curr : acc + curr,numbers)
# reduce --> is same like java reduce
print(int(total))

total_2 = reduce(lambda acc,curr : acc + curr,numbers,10)
# reduce --> is same like java reduce, with starting value 10

print(total_2)

# We also have builtin function called SUM ,

total_3 = sum(numbers)
print(total_3)