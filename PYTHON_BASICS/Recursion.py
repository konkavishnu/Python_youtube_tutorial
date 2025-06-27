def add_one(num):
    if num >= 9:
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


my_new_total = add_one(0)
print(my_new_total)

value2 = "Y"
while value2:      # --> we can also use data type as condition , here since the String has become integer the loop stopped.
    print(value2)
    value2 = 0

value3 = True
while value3:     # --> we can also use boolean as condition , this is same as value3 == True
    print(value3)
    value3 = False
