def decorator(func):
    def wrapper(*args, **kwargs):
        print("now start")
        func(*args)
        print("now end")
    return wrapper
    

@decorator
def foo(name):
    print("I am " + name)


foo("Jack")
