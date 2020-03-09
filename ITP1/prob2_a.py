# Small, Large and Equal

a, b = map(int, input().split())

ans = ""
if a>b:
    ans = "a > b"
elif a<b:
    ans = "a < b"
else:
    ans = "a == b"

print(ans)
