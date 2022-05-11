import sys
# sys.stdin=open("./in4.txt", "r")
a = input()
b = input()
ck = dict()
for x in a:
    ck[x] = ck.get(x, 0) + 1
for x in b:
    ck[x] = ck.get(x, 0) - 1

for i in ck.values():
    if i != 0:
        print("NO")
        break
else:
    print("YES")



