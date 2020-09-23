T = int(input())
while T:
    num = list(map(int, input().strip().split()))[:2]
    H = num[0]
    P = num[1]
    if P > H:
        print('1')
    for A in range(0, P): 
        H = H-P
        P = P//2
    if H > P and H == 0:
        print("0")
    else: 
        print("1")

