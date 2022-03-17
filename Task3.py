row1=int(input())
col1=int(input())
row2=int(input())
col2=int(input())
move=[row1,col1,row2,col2]
for i in range(0,len(move)):
    if move[i]>8:
        move[i]=1
if move[0]==move[2] or move[1]==move[3] or abs(move[0]-move[2])==abs(move[1]-move[3]):
    print("yes")
else:
    print("no")
