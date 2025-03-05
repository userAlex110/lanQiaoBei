"""
优化执行：
目标减少复杂度
我们可以将年份，月和日分开求数位和，这样就不用遍历每一天了
"""


def digit_sum(num):
    """计算整数的数位和"""
    return sum(int(digit) for digit in str(num))

def is_leap_year(year):
    """判断是否为闰年"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_valid_date(year, month, day):
    """检查日期是否合法"""
    if month < 1 or month > 12:
        return False
    if month == 2:
        days = 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        days = 30
    else:
        days = 31
    return 1 <= day <= days


count = 0
# 遍历年份
for year in range(1900, 10000):
    year_sum = digit_sum(year)
    # 遍历月份
    for month in range(1, 13):
        month_sum = digit_sum(month)
        # 计算日期数位和的可能范围
        for day in range(1, 32):
            day_sum = digit_sum(day)
            if year_sum == month_sum + day_sum and is_valid_date(year, month, day):
                count += 1

print(f"符合条件的天数有{count}天")
