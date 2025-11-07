person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

print("\n%s has %s  coins left." % (person, coins))
print("\n{} has {}  coins left.".format(person, coins))
print("\n{1} has {0}  coins left.".format(coins, person))
print("\n{person} has {coins}  coins left.".format(person=person, coins=coins))


player = {"person": "Dave", "coins": 3}
print("\n{person} has {coins}  coins left.".format(**player))

# f-strings!

message = f"\n{person} has {coins}  coins left."
print(message)

message = f"\n{person} has {3*5}  coins left."
print(message)

message = f"\n{person.lower()} has {3*5}  coins left."
print(message)

num = 10
print(f"\n 2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} devided by 2.25  is { num / 4.52:.2%}")
