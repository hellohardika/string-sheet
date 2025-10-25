A="aabababaa"
B="ba"
n=len(A)
m=len(B)
pos=-1
for i in range(n-m+1):
    if A[i:i+m]==B:
        pos=i
        break
print(pos)
