# Write a decorator that measure the time a function takes to execute.


import time

def timer(function):
    def wrapper(*args,**kwargs):
        