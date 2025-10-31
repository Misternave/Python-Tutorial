first = "Dave"
last = "Gray"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# construction function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)

# Concatenation
fullname = first + "" + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = """
Hey, how are you

i was just checking in.
                All good?
"""
print(multiline)
