# 計算機

while True:
    calc_formula = input()
    op = calc_formula.split()
    a = int(op[0])
    b = int(op[2])
    if op[1]=="?": # stop condition
        break

    if op[1]=="+":
        print(a + b)
    elif op[1]=="-":
        print(a - b)
    elif op[1]=="*":
        print(a * b)
    else:
        print(a // b)
