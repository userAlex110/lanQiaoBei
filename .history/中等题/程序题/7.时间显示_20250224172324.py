"""
要求是格式化输出
"""

time0 = int(input())
time1 = time0 // 1000
HH = time1 // (60*60)
MM = time1 // 60 % 60



print(f"{HH:>2}:{MM:>02}")