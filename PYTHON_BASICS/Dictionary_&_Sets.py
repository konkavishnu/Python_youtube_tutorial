#                                  DICTIONARY { }
#                                  -----------
# Dictionaries are set of Key , value pair
# NOTE : In dictionary "Key" values should be immutable and "values" can be anything.

band = {
    "vocals": "plant",
    "guitar": "page"
}

band_2 = dict(vocals="plant", guitar="page")
print(band)
print(type(band_2))

# Access Items
print(band_2["vocals"])
print(band.get("guitar"))
print(band.get("guitar",34)) # --> band.get(<key>,<value to return if the key is not present>)
# NOTE : if the key does not present by default it will return NONE.
#        if we like to return a value if the key is not present we can do like above in "get" function.

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a key exist
print("guitar" in band)
print("name" in band)

# modify values in dictionary

band["vocals"] = "Coverall"
# or
band.update({"guitar": "rock"})  # --> remember to use { }
band.update({"bass": "JPJ"})
print(band)

# Remove items
print(band.pop("guitar"))
print(band.popitem())  # --> to remove the item as tuple
print(band)

# Update items
band.update({"bass": "jpj"})
band.update({"guitar": "rock"})

# delete & clear
del band["bass"]
print(band)
band_2.clear()
print(band_2)

band = {
    "vocals": "plant",
    "guitar": "page"
}

# Copy dictionary
band_2 = band  # --> this will create a reference i.e, pointing to the memory of the band
print(band_2)

band2 = band.copy()  # --> this is the correct way to copy
band2.update({"guitar1": "rock3"})
print(band2)

band3 = dict(band2)  # --> copying using constructor
print("This is band3 : ", band3)

# NESTED DICTIONARIES

member1 = {"name": "plant", "instrument": "guitar"}
member2 = {"name": "page", "instrument": "guitar"}
band_nest = {"member1": member1, "member2": member2}  # --> nested Dictionary
print(band_nest)

# Access nested dictionary
print(band_nest["member1"]["instrument"])  # --> this is, <dict name>[<key of the sub-dict whose value is needed>][< key of value inside the sub-dict>] , likewise we can access the sub dicts for all layers.

# Iterating through Dictionary:
for X in band : # --> while looping inside a dictionary , X will hold only the value of Keys.
    print(X , band[X]) # --> this will print(Key,value)
    
for key in band.items():
    print(key) #--> this will give us a keys tuple
    
for key,value in band.items():
    print(key,value) # --> this is same as the first one since we are using the ".items()"
    
    
# COMPREHENSIONS:
#----------------

# List:
#-----
values_comp = []

for x in range(5):
    values_comp.append(x*2)
    
values_comp =[x*2 for x in range(5)] #--> this is comprehension of the above 2 lines.
# here , x*2 - Expression | x  - the item inside the range

# Sets
#-----

values_sets = {x*2 for x in range(5)} # (only change from list is '{}')

# Tuple - there are no comprehension for Tuple , instead we use generator objects (see after 'Sets' section below)
#-------

# Dictionary
#-----------
values_dict ={x:x*2 for x in range(5)}

# UNPACKING DICTIONARY
#---------------------

first_dict = {"x": 1}
second_dict = {"x": 10 , "y": 2}

combined ={**first_dict,**second_dict}
print(combined)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                     SETS
#                                    ------
# Sets are unordered and no duplicate set of values

# NOTE : Sets do not store elements in order like List , so we cannot
#        access the elements by index , python will throw error if we do it.
#        Sets can be used only for the below actions.

set_num = {1, 2, 3, 4}
set_num2 = set((1, 2, 3, 4))
print(set_num2)
print(set_num & set_num2)
print(len(set_num))

# NOTE : in sets - 'True' is dupe of '1' and 'False' is dupe of '0'
No_duplicate = {1, True , 45 , False , 0}
print(No_duplicate)

# check if value is present or not
print(1 in No_duplicate)  # --> note that in sets we cannot check with index or key
# add
set_num.add(5)
# add element from one set to another
set_num.update(No_duplicate)
print(set_num)

# Merge or Union of 2 sets
#--------------------------
one = {23, 45, 56}
two = {213, 4, 561}
my_New_set = one.union(two)
#            (or)
my_union_set = one | two

# Merge and keep only duplicates
#-------------------------------
my_New_set1 = one.intersection(two)
#            (or)
my_inter_set = one & two

print(my_New_set1)

# Difference between sets:
#-------------------------
my_diff_set = one.difference(two)
#            (or)
my_diff_set1 = one -two

# exclude only duplicates
#------------------------
my_New_set2 = one.symmetric_difference_update(two)
#            (or)
my_Sydiff_set = one ^ two

print(my_New_set2)

# NOTE : use the dot operator to explore all other functions on a set

#---------------------------------------------------------------------------------------------------------------------------------

#                           GENERATOR OBJECTS
#                           -----------------

# Generator objects are objects which are used when working on large amount of data.
# They do not store the data like other data structures instead once they generate each data
# according to condition, they erase the data and generate the next data.
# () are used for generator objects.
# NOTE : Since Generator objects do not store , we cannot calculate the length of the generator object.
#        python will throw error.

from sys import getsizeof # --> used to get the size 

values_gen = (x * 2 for x in range(100000))

print(getsizeof(values_gen)) # --> this size will be same for all ranges above
