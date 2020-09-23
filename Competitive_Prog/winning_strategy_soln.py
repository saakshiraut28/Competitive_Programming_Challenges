T = int(input())
count = 0
for i in range(0,T):
    N = int(input())
    ary = list(map(int, input().strip().split()))[:N]
    if N%2 == 0:
        print("draw")
    elif N == 1:
        print("frist")
    else:
        print("second")
        