line = input().split(", ")

haha = []

for user in line:
    if 3 <= len(user) <= 16:
        if "-" in user or "_" in user or user.isalnum():
            if " " not in user:
                haha.append(user)

# print(line)
# print(haha)
print(*haha, sep='\n')

