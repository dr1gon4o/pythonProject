def palindrome(*haha):
    # haha2 = reversed(haha[0])
    if haha[0] == haha[0][::-1]:
        return f"{haha[0]} is a palindrome"
    else:
        return f"{haha[0]} is not a palindrome"

print(palindrome("abcba", 0))
# print(palindrome("peter", 0))