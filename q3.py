n=int(input("rank of matrix"))
m1=[]
m2=[]
m3=[]
row1=[]
print("for 1st matrix")
for i in range(n):
    row=input("enter row with entries sepereated by a space\n").split()
    m1.append(row)

print("for 2nd matrix")
for i in range(n):
    row=input("enter row with entries sepereated by a space\n").split()
    m2.append(row)

for i in range(n):
    
    for j in range(n):
        value=0    
        for k in range(n):
            value=value+int(m1[i][k])*int(m2[k][j])
        row1.append(value)
    m3.append(row1)
    row1=[]    
tr=0
for i in range(n):
    for j in range(n):
        if i==j:
            tr=tr+m3[i][j] 
print(tr)

for i in range(n):
    print(m3[i])
