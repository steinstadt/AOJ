# 不足しているカードの発見

# input process
n = int(input())

# initialization
card_list = {}
card_type = ['S', 'H', 'C', 'D']
for c in card_type:
    card_list[c] = [0]*13

# remove process
for i in range(n):
    t, n = input().split()
    n = int(n)
    card_list[t][n-1] = 1

# output process
for c in card_list:
    for i in range(len(card_list[c])):
        if card_list[c][i]==0:
            print("%s %d"%(c, i+1))
