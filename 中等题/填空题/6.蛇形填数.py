init = 1
for i in range(1, 20):
    "规律是在对角线的数字中，前一行的数 + 前一行数字的行数 * 4 = 这个对角线数"
    res = init + 4*i