# 2つの数の変換

while True:
    x, y = map(int, input().split())

    if x==0 and y==0:
        break

    if x>y:
        tmp = x
        x = y
        y = tmp
    print(str(x) + " " + str(y))
