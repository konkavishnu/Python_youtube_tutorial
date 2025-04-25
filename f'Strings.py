person = "jason"
coins = 4

print("\n" + person + " has " + str(coins) + " coins.")

message = "\n%s has %s coins left." % (person, coins)
print(message)

message1 = "\n{} has {} coins left.".format(person, coins)
print(message1)

message2 = "\n{1} has {0} coins left.".format(person, coins)
print(message2)

message3 = "\n{person} has {coins} coins left.".format(person=person, coins=coins)
print(message3)

player = {'person': 'AWS', 'coins': 3}

message4 = "\n{person} has {coins} coins left.".format(**player)
print(message4)

#  f'Strings

message_new = f"\n{person} has {coins} coins left."
print(message_new)

message_new_1 = f"\n{person} has {3 + 4} coins left."
print(message_new_1)

message_new_2 = f"\n{person.lower()} has {3 + 4} coins left."
print(message_new_2)

player1 = {'person': 'AWS', 'coins': 3}

message_new_3 = f"\n{player1['person']} has {3 + 4} coins left."
print(message_new_3)

# you can pass formatting options

num = 5
print(f"\n2.25 times {num} is {2.25 * num:.2f}")  # here 2f is 2 decimal round off
