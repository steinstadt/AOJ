# 長方形の描画

while True:
    H, W = map(int, input().split())
    if H==0 and W==0:
        break

    # display process
    for h in range(H):
        for w in range(W):
            print("#", end="")
        print()
    print()
