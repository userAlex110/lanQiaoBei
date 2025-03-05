"""
这个代码抄自蓝桥杯题解的大佬
"""

# 请在此输入您的代码
def isLeap(x):  # 判断是否为闰年
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        return True
    return False

def numAdd(x):  # 计算年份个数位的数字和
    sums = 0
    while x:
        sums += x % 10
        x //= 10
    return sums


start, end = 1900, 9999
ans = 0
day = [1, -2, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]  # 每个月天数和30天的差值
data = []
hstable = dict()  # key:月份1~12，value:每个月份月份数位和+日的数位和的区间，如1月份为(2, 32)
for j in range(1,32):  # 计算日数位和
    data.append(numAdd(j))
for i in range(1, 13):  # 初始化哈希表
    t = numAdd(i)  # 月数位和
    for j in range(day[i - 1] + 30):  # 遍历一个月的每一天将月数位和加上日数位和
        addt = t + data[j]
        if addt not in hstable:
            hstable[addt] = 1  
        else:
            hstable[addt] += 1  # 哈希表中对应的天数加一

for i in range(start, end + 1):  # 遍历每一年
    yearsum = numAdd(i)  # 计算年的数位和
    if yearsum in hstable:  # 若年的数位和在哈希表中存在则答案加上对应的天数
        ans += hstable[yearsum]
    if isLeap(i) and yearsum == 13:  # 闰年2月份多一天，位数和为13
        ans += 1

print(ans)