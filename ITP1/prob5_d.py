# 構造化プログラミング

n = int(input())

i = 1
while i<=n:
    x = i
    if x%3==0:
        print(" %d"%(i), end="")
        i = i + 1
        continue
    while True:
        if x%10==3:
            print(" %d"%(i), end="")
            break
        x = x // 10
        if x==0:
            break
    i = i + 1
print()
