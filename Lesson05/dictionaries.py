band = {"vocals": "plant", "guitar": "Page"}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# list all values
print(band.values())

# List of key/values pairs as tuples
print(band.items())

# verify if key exists
print("guitar" in band)
print("flower" in band)

# change values
band["vocals"] = "Coverdale"
print(band)
band.update({"bass": "JPJ"})
print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bohnam"
print(band)

print(band.popitem())  # tuple
print(band)

band["drums"] = "Bohnam"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copy dictionaries

band2 = band  # creates a reference to the memory of band
print("Bad copy!")
print(band2)
print(band)

band2["Drums"] = "Dave"
print(band)

band3 = band.copy()
print("Good copy!")

print(band3)
print(band)

band3["drums"] = "George"
print(band)
print(band3)

band4 = dict(band)
print(band4)

member1 = {"name": "Plant", "instrument": "Vocals"}


member2 = {"name": "Plant", "instrument": "Guitar"}

group = {"member1": member1, "member2": member2}

print(group)
print(group["member1"]["name"])

# Sets
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(len(nums))

# no duplicates allowed in Sets

nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of zero

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# add value to a Set
nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# Merge two sets
one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everythin excetp the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
