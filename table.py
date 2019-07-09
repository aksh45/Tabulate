#no of rows in table
n=int(input("Enter no of rows for table "))
coloumns=int(input("Enter no of coloumns for table"))
li=[]#table
length=[]#list of max length of each coloumn
#input table
for x in range(n):
    lis=input().split()
    li.append(lis)
for x in range(coloumns):
    maxn=None
    for i in range(n):
        lgth=len(li[i][x])
        if maxn==None:
            maxn=lgth
        elif maxn<lgth:
            maxn=lgth
    length.append(maxn)
sumn=0
for x in range(n):
    sumn+=length[x]
sumn+=4*(coloumns-1)+n+1
print(" ",end="")
for x in range(sumn):
    print("_",end="")
print()
for x in range(n):
    print("|",end="")
    for i in range(coloumns):
        if i==0:
            spaces=li[x][i]+(length[i]+2-len(li[x][i]))*" "+"|"
        else:
            spaces=" "*2+li[x][i]+(length[i]+2-len(li[x][i]))*" "+"|"
        print(spaces,end="")
    print()

