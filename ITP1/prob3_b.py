# テストケースの出力

# 0が来るまで無限ループ
count = 1
while True:
    x = int(input())
    if x==0:
        break

    print("Case %d: %d"%(count, x))
    count += 1
