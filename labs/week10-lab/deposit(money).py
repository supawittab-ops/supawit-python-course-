for i in range(1, 7):
    print(''.join(chr(65 + j) for j in range(i)))

print()  

s = input("Enter a string: ")
print(s[::-1])