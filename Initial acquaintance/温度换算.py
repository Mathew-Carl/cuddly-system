#tempconvert.py
tempstr = input("请输入带有符号的温度值:")
if tempstr[0] in ['F','f']:
    C = (eval (tempstr[1:-1]) - 32)/1.8
    print("{:.2f}C".format(C))
elif tempstr[0] in ['C','c']:
    F = 1.8 * eval(tempstr[1:-1]) + 32
    print("{:.2f}F".format(F))
else:
    print("输入格式错误")
