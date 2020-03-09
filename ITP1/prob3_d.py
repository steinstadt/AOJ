# 約数の数

# input process
a, b, c = map(int, input().split())

# initialization
count = 0

# loop process
for i in range(a, b+1):
    if c%i==0:
        count += 1

print(count)
