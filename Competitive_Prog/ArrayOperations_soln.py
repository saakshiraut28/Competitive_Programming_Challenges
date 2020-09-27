T = int(input())
t=0
while t<T:
    N = int(input())
    ary = list(map(int, input().strip().split()))
    new_ary = []
    n = 1
    for i in range(N):
        sub = ary[i]-n
        new_ary.append(sub)
        n+=1
    total = sum(new_ary)
    if total == 0:
        print("YES")
    else:
        print("NO")
    t+=1