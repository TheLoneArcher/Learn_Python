def sumofnums(*args):
    print("-------------Function *args-------------")
    print("*args: ", args)
    print("Sum of numbers: ", sum(args))
    print()
def kwargs(**kwargs):
    print("-------------Function **kwargs-------------")
    print("**kwargs: ", kwargs)
    print()
def mixed_args(arg1, arg2, *args, **kwargs):
    print("-------------Function Mixed Args-------------")
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("*args: ", args)
    print("**kwargs: ", kwargs)
    print()

sumofnums(1, 2, 3, 4, 5)
# **kwargs stores the keyword arguments (key-value pairs with =) as dictionary {key: value, ...}
kwargs(name="Alice", age=30, city="New York")
mixed_args("Hello", "World", 1, 2, 3, key1="value1", key2="value2")
# I've tried removing the second argument to see if it works
# but it requires at least two positional arguments, the *args and **kwargs can be empty
mixed_args("Python", "Programming")