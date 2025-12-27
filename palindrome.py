



for_list = list(input())
print(list)

print(f"now let us check if the contents of the list are falling in Pallindrome syndrome :)")

found= []
i = 1
for i in range(1,len(for_list)-1):
        if (for_list[i-1]==for_list[i+1]):
                     found.append(i)

print(found)






for_list = list(input("Enter items: "))
# Corrected the print statement: you must print the variable 'for_list', not the keyword 'list'
print(for_list)

print("Checking if the contents are falling in Palindrome syndrome :)")

# Optimal 2025 method for checking a full palindrome
if for_list == for_list[::-1]:
    print("Yes, the entire list is a Palindrome!")
else:
    print("No, it is not a Palindrome.")

