
A = "aabbcc"
B = 98

#Convert ASCII code to its character
target = chr(B)   

#Assume the character is not found
index = -1


for i in range(len(A)):
    if A[i] == target:   
        index = i       
        break           


if index == -1:
    print(f"Character '{target}' not found in the string.")
else:
    print(f"Character '{target}' found at index {index}.")
