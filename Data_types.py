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

# escaping special characters
sentence = "I 'm back \t Hey! \n\n where this at\\located?"
print(sentence)

# string methods
print(first)
print(first.lower())
print(first.upper())
print(first)
print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)
print(len(multiline))
multiline = "                                               " + multiline
multiline += "                                                 "
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a Menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "1€".rjust(4))
print("Water".ljust(16, ".") + "2€".rjust(4))
print("Bread".ljust(16, ".") + "4€".rjust(4))
