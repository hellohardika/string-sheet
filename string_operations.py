A = "aeiOUz"                       

#join string with itself
A = A + A   

# remove capital letters       
small = ""
for ch in A:
    if ch.islower():      # keep only small letters
        small = small + ch

#replace vowels with '#'
result = ""
for ch in small:
    if ch in "aeiou":     # if letter is vowel
        result = result + "#"
    else:
        result = result + ch

print(result)
