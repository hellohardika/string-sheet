A="bobob"
count=0
for i in range(len(A)-2):
    if A[i:i+3]=="bob":
        count+=1

print(count)