"""
这个问题算是厉害了，我知道Python有个关于时间的库可以调用来做，奈何本人不会。
问题问从1900年1月1日开始，到9999年12月31日结束，有多少天。
还有满足，年份的数位数字之和等于月的数位数字之和加日的数位数字之和。
丸辣，感觉是不是用多个条件来判断，闰年，然后每月月份也得注意。。。
"""

import datetime




start_date = datetime.date(1900, 1, 1)
end_date = datetime.date(9999, 12, 31)
delta = end_date - start_date
count = 0

# 遍历每一天.注意datetime.date支持的范围就到9999年12月31日，不要超出范围了
while start_date < end_date:
    #  Python 没有直接的内置函数可以获取整数的每一位数字，所以需要先将整数转换为字符串，再进行处理。
    year_sum = sum(map(int, str(start_date.year)))
    month_sum = sum(map(int, str(start_date.month)))
    day_sum = sum(map(int, str(start_date.day)))

    if year_sum == month_sum +day_sum:
        count += 1
    # 加一天
    start_date += datetime.timedelta(days=1)

print(f"从1900年1月1日到9999年12月31日共有{delta.days}天")
print(f"符合条件的天数有{count}天")
