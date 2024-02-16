def age_assignment(*hoho, **haha):
    haha2 = []
    for x, y in haha.items():
        for i in hoho:
            if i.startswith(x):
                # haha2[i] = y
                haha2.append(f"{i} is {y} years old.")
    # haha3 = sorted(haha2)

    return "\n".join(sorted(haha2))


# print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
