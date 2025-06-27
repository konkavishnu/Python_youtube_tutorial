# Question - Find the most repeated character in the string ?

sentence = "This is a common interview question"
sen_1 = sentence.replace(" ","")
print(sen_1)
char_rep = {}

for char in sen_1:
    if char in char_rep:
        char_rep[char] +=1
    else:
        char_rep[char] = 1
        
sort_dict=list(sorted(char_rep.items() , key= lambda item : item[1],reverse=True))  # --> since dict are unordered we use sorted func       
print(sort_dict[1])  


# newList = [3, 2, 1, 4, 5]
# newList.sort(reverse=True)  # --> sorts the list , note - we can sort only with same data type in the list
# print(newList)  


users = ["Vishnu", 34 , "Vardhan"]
print(users[0:1])
print(users[:2])
print(users[0:])
print(users[1:])
print(len(users))

users[2:] = ['Eddie']  # --> to add / insert the element to a particular index , here it inserted at index=2
print(users)

newCopy2 = users[:]
print(newCopy2)