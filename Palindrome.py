string = input("Enter string = ")
L = []
for i in range(0, len(string)):
    L.append(string[i].lower())
org_L = L
L.reverse()
if L == org_L:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
