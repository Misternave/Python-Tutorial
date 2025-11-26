class JustNotCoolError(Exception):
    pass


x = 2
try:
    raise JustNotCoolError("this not cool")
    # raise Exception("i am a custom exception!")
    # print(x/0)
    # if not type(x) is str:
    #     raise TypeError("only strings are allowed")
except NameError:
    print("There is an error")
    print(NameError)
except ZeroDivisionError:
    print("please do not divide by error")
except Exception as error:
    print(error)
else:
    print("no erros!")
finally:
    print("i am going to print always")
