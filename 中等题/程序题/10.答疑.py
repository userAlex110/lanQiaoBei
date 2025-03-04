"""
首先阶梯的思路就是，学生的答疑关键在于，收拾东西时间ei。
目标就是让ei从小到大排列这样让学生更快开始答疑，这样每个人的总答疑时间其实是固定的
我们设置的只是让收拾最慢的同学，排在最后不要耽误了其他学生答疑
"""
# 更正，第一次思考错误。我们的目标是：
# 输出一个整数，表示同学们在课程群里面发消息的时刻之和最小是多少。
# 其实是找同学发消息的间隔时间最短。
# 也就是上一个同学的收拾时间，与本同学的答疑时间。
# 所以应该对这两个时间进行排序

# 感觉困难的地方
"""
1.输入格式，有两部分n 和 表格时间
怎么使用二维的列表，或者说怎么保存这种表格格式
"""

students = int(input())
total_time_list = []

for _ in range(students):
    use_time = list(map(int, input().split()))
    total_time_list.append(use_time)

# 按照ei时间排序
# 这是错误的total_time_list.sort(key = lambda x: x[2])

# 对si 和 ai 进行排序
total_time_list.sort(key = lambda x: x[0] + x[1])

# 计算总时间
cur = 0
ans = 0
for time_info in total_time_list:
    # cur累加当前同学的进入时间和答疑时间，用于计算该同学发消息时刻
    cur += time_info[0] + time_info[1]
    # 将当前同学发消息时刻累加到ans中
    ans += cur
    # cur再加上当前同学离开时间，更新累计时间用于下一位同学计算
    cur += time_info[2]
print(ans)


# 这样写只有40分。哭>_<哭