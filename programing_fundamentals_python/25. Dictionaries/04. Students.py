# name, ID, course = input().split(":")
haha = []
# haha2 = None

while True:
    hoho = input()

    if ':' not in hoho:
        # haha2 = hoho
        break

    name, ID, course = hoho.split(':')
    haha.append({'name': name, 'ID': ID, 'course': course})

for i in haha:
    # print(i['name'], "-", i['ID'])

    if hoho.replace('_', ' ') in i['course']:
        print(i['name'], "-", i['ID'])
    # if hoho in haha['course'][0:3]:
    #     print(f'"{name} - {ID}"')

# vtori variant !
# for i in haha:
#     if hoho.startswith(i['course'][0:3]):
#         print(f"{i['name']} - {i['ID']}")


# print(haha)
# print(haha2)
# print(hoho)

