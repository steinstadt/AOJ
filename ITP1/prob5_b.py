# フレームの描画

while True:
    H, W = map(int, input().split())
    if H==0 and W==0: # stop condition
        break

    for h in range(H):
        for w in range(W):
            if h==0 or h==(H-1) or w==0 or w==(W-1):
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()
    
