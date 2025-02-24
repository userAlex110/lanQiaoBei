"""
要求是格式化输出
"""

total_seconds = int(input())
# 直接整除得到时
HH = total_seconds // 3600000
# 剩下秒数
remainder_seconds = total_seconds % 3600000
# 显示分钟
MM = remainder_seconds // 60
# 显示秒钟
SS = remainder_seconds % 60


print(f"{HH:>02}:{MM:>02}")