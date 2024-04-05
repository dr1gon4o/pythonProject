
def type_check(expected_type):
    def decorator(func):
        def wrapper(element):
            if not isinstance(element, expected_type):
                return f"Bad Type"

            return func(element)

        return wrapper

    return decorator
