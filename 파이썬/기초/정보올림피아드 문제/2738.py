n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in a:
    b = list(map(int, input().split()))
    for x1,x2 in zip(i,b):
        print(x1+x2, end=" ")
    print()
