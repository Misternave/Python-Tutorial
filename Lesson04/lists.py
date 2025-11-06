users = ["Dave", "John", "Sara"]

data = ["Dave", 42, True]

emptylist = []

print("Dave" in users)
print(users[0])
print(users[-1])

print(users.index("Sara"))
print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))
users.append("Elsa")
print(users)
users += ["Jason"]
print(users)
users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)
users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["Robert", "JPJ"]
print(users)

users.remove("Bob")
print(users)

print(users.pop())  # returns tha value and removes the last value
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ["dave"]

users.sort()  # lower case goes after the uppercase
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 25, 64, 5, 12]
nums.reverse()
print(nums)
nums.sort()
print(nums)
# nums.sort(reverse=True)
print(nums)

print(sorted(nums, reverse=True))  # reverse without changing the original list
print(nums)


numscopy = nums.copy()
print(numscopy)
mynums = list(nums)
print(mynums)
mycopy = nums[:]

print("test")
print(nums)
print(numscopy)
print(mynums)
print(mycopy)

# Tuples -- tuples cannot be changed

mytuple = tuple(("dave", 42, True))
print(mytuple)
anothertuple = (1, 4, 2, 8)

(one, two, *hey) = anothertuple

print(one)
print(two)
print(hey)
