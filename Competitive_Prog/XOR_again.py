
# Link to Problem: https://blancode.wordpress.com/codechef-contests/may18/xoragn/

T = int(input())

for i in range(T):
    final_ary = list()
    total=0
    N = int(input())
    num = list(map(int, input().strip().split()))
    for i in num:
        for j in num:
            total = j+i
            final_ary.append(total)
    total = sum(final_ary)
    print(final_ary)
    print(total)
