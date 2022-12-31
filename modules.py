def circle_function(func):
    def wrapper(*args):
        i = 0
        while i <= 1:
            func(*args)
            i += 1
    return wrapper
