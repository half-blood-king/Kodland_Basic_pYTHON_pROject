non_zero=[0,4,0,5,0,3,0,0,5,0,0]
for i in range(0,non_zero.count(0)):
    non_zero.remove(0)
    non_zero.append(0)
print(non_zero)
