my_list = input().split(', ')

blacklist = []
lostlist = 0

for name in my_list:
    command = input()
    if command == f"Blacklist {name}":
        blacklist.append(name)

        if name in my_list:
            print(f"{name} was blacklisted.")
            # blacklist += 1
        else:
            print(f"{name} was not found.")
    elif command == f"Error {name}":
        if name in len(my_list):
            print(f"{name} was lost due to an error.")
        else:
            pass
    # elif command == f"Change {index} {new name}":
        pass
    elif command == "Report":
        print(f"Blacklisted names: {len(blacklist)}")
        print(f"Lost names: {lostlist}")



print(f"Blacklisted names: {len(blacklist)}")
print(f"Lost names: {lostlist}")
print(my_list)
