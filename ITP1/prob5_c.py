# チェスボードの描画

while True:
    H, W = map(int, input().split())
    if H==0 and W==0: # stop condition
        break

    for h in range(H):
        if h%2==0:
            for w in range(W):
                if w%2==0:
                    print("#", end="")
                else:
                    print(".", end="")
        else:
            for w in range(W):
                if w%2==0:
                    print(".", end="")
                else:
                    print("#", end="")
        print()
    print()
