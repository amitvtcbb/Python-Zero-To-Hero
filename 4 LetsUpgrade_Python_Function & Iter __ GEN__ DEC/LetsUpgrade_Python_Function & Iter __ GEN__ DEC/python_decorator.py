# Example : 1
# def func():
#     return 1
#
# f = func()
# print(f)

def hello(name="letsupgrade"):
    return "Hello " + name
hello()
greet = hello
print(greet)
f = greet()
print(f)