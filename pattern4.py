n=int(input("enter size"))
for i in range (n):
    for j in range(n):
        if i==j or j==0 or i==n-1:
            print("*",end=' ')    
        else:
            print(" ",end=' ')    
    print()   