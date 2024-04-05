def logged(haha):

    def hoho(*args, **kwargs):
        name = haha(*args, **kwargs)
        result = f"you called {haha.__name__}{args}\n" \
                 f"it returned {name}"
        return result
    return hoho

@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

