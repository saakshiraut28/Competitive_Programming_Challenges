
# Link to Problem: https://blancode.wordpress.com/codechef-contests/may18/xoragn/

T = int(input())

for i in range(T):
    n=int(input())
    l1=list(map(int,input().split()))
    a=l1[0]+l1[0]
    for j in range(1,n):
        a=a^(2*l1[j])
    print(a)

