def kwargs_length(**names):
    return len(names)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
