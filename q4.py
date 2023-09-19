n=int(input("enter the number of test cases\n"))
test_cases=[]
for r in range(n):
    num=input("enter the number\n")
    test_cases.append(num)

for number in test_cases:
    n1=[]
    for i in number:
        n1.append(i)
    a=len(n1)
    for i in range(int(len(n1)/2)):
        if n1[i]!=n1[len(n1)-1-i]:
            continue
        else:
            a=i
            break
    if a==len(n1):
        print('0')
    else:
        for i in range(a):
            n1.pop(0)
            n1.pop()
        print(len(n1))


