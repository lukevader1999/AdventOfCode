ls = [0,1,2,3,4,5]
lsls = []
for i in range(0,6):
    lsls.append(ls)

for i in range(0,len(lsls)):
    print("\n")
    for j in range(0,len(lsls[i])):
        print(f"({i},{j})", end=" ")

for i in range(0,len(lsls)):
    print("\n")
    for j in range(0,len(lsls[i])):
        print(f"{lsls[i][j]}", end=" ")