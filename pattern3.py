n=int(input("enter size"))
for i in range (n):
    for j in range(n):
        if j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=' ')    
        else:
            print(" ",end=' ')    
    print()   