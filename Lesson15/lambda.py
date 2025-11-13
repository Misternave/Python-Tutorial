squared = lambda num: num * num

print(squared(2))

addTwo = lambda num: num + 2

print(addTwo(12))

sum2 = lambda a, b: a + b
print(sum2(2, 3))

###########################################


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)  # 10 is the x
addTwenty = funcBuilder(20)  # 20 is the x

print(addTen(7))  # 7 is the num
print(addTwenty(7))  # 7 is the num

#############################################
# High order functions

lambda num: num * num

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))
############################


odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))

###############
from functools import reduce

lambda acc, curre: acc + curre
numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curre: acc + curre, numbers, 10)
print(total)

print(sum(numbers, 10))

names = ["Dave Gray", "Sara ito", "John Jacob jingleheimsecchmidt"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)
