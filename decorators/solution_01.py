# Write a decorator that measure the time a function takes to execute.


import time

def timer(function):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = function(*args,**kwargs)
        end = time.time()
        print(f"{function.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_fuction(n):
    time.sleep(n)

example_fuction(2)