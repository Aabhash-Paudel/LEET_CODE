n = int(input("Enter number of lines: "))
for i in range(1,n):
    for j in range(1,i+1):
        print(str(j),end=' ')
    print()