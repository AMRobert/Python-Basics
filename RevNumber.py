N = int(input())
Rev = 0
while(N>0):
    Remainder = N %10
    Rev = (Rev *10) + Remainder
    N = N//10
print(Rev)


# N = 1233
# N % 10 = 3
# Rev ??
# 123//10 = 12
