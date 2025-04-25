#                                  DICTIONARY { }
#                                  -----------

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
print(band_nest["member1"]["instrument"])  # --> this is, <dict name>[<key of the sub-dict whose value is needed>][< key of value inside the sub-dict>] , likewise we can access the sub dicts for all layers

#                                     SETS
#                                    ------
# Sets are used to contain no duplicate values

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

# Merge 2 sets
one = {23, 45, 56}
two = {213, 4, 561}
my_New_set = one.union(two)

# Merge and keep only duplicates
my_New_set1 = one.intersection(two)
print(my_New_set1)

# exclude only duplicates
my_New_set2 = one.symmetric_difference_update(two)
print(my_New_set2)

# NOTE : use the dot operator to explore all other functions on a set

