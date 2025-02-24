x = 1
num = 1
for i in range(1, 20):
    "规律是在对角线的数字中，前一行的数 + 前一行数字的行数 * 4 = 这个对角线数"
    x +=  4*i
    num += 1
    print(x, num)