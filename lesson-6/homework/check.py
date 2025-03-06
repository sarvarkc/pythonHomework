def check(func):
    def wrapper(a,b):
        if b!=0:
            return func(a,b)
        else:
            return "Denominator can't be zero"
    return wrapper

@check
def div(a,b):
    return a/b

print(div(6,0))
print(div(6,2))