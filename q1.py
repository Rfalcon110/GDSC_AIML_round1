test_cases = int(input("enter number of test cases.\n"))
list_case=[]
for i in range(test_cases):
    s1,s2= input("enter the strings seperated by a space\n").split()
    tuple=(s1,s2)
    list_case.append(tuple)

for i in range(test_cases):    
    l1=[]
    l2=[]
    for j in list_case[i][0]:
        l1.append(j)
    for j in list_case[i][1]:
        l2.append(j)
    t1=True
    for k in l1:
        if k not in l2:
            t1=False
            break
    if t1==True:
        print("yes")
    else:
        print("no")




    