n=int(input("enter the number of rows"))

num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if num>n:
            num=1
        print(num,end="")
        num=num+1
    print("\n")
    