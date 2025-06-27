import sys

value = 1
# while value <= 10 :
#     print(value)
#     value += 1

while value <= 10 :
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("Done" + str(value))


names = ["GTA", "RDR2", "GT"]
for x in names:
    print(x)

for n in "VISHNU":
    print(n)

for m in range(1, 4):  # --> range(<start> , <end>)
    print(m)

for k in range(4):  # --> range(<end>)
    print(k)

for L in range(0, 10, 2):  # --> range(<start>, <end>, <increment by>)
    print(L)
else:
    print("Done at " + str(L))
    sys.exit()  # --> this will help us to exit out of the runtime

# Note : we also can have nested for loops 



