x = input()

# def password():
#     x = input()
#     if 6 <= len(x) <= 10:
#         if x.isalnum():
#             if any(h.isdigit() for h in x):
#                 return "Password is valid"
#             else:
#                 return "Password must have at least 2 digits"
#         else:
#             return "Password must consist only of letters and digits"
#     else:
#         return "Password must be between 6 and 10 characters"

passed = 0

if 6 <= len(x) <= 10:
    passed += 1
else:
    print("Password must be between 6 and 10 characters")

if x.isalnum():
    passed += 1
else:
    print("Password must consist only of letters and digits")

haha = 0
for h in x:
    if h.isnumeric():
        haha += 1
if haha >= 2:
    passed += 1
else:
    print("Password must have at least 2 digits")

if passed == 3:
    print("Password is valid")


# print(password())

#  and passed == 2
# if any(h.isnumeric() for h in x):
# if len([h for h in x if h.isdigit()]) > 2: