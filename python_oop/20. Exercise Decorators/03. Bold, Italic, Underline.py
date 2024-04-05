def make_bold(haha):

    def hoho(*args, **kwargs):
        result = f"<b>{haha(*args, **kwargs)}</b>"

        return result

    return hoho

def make_italic(haha):

    def hoho(*args, **kwargs):
        result = f"<i>{haha(*args, **kwargs)}</i>"

        return result

    return hoho

def make_underline(haha):

    def hoho(*args, **kwargs):
        result = f"<u>{haha(*args, **kwargs)}</u>"

        return result

    return hoho

@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

