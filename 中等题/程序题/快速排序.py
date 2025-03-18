def quick_sort(arr: list[int]) -> list:
	# 终止条件
	if len(arr) <= 1:
		return arr
	pivot = arr[-1]
	left = [x for x in arr[:-1] if x <= pivot]
	right = [x for x in arr[:-1] if x > pivot]

	# 递归合并
	return quick_sort(left) + [pivot] + quick_sort(right)

# 示例  
arr = [3, 6, 8, 10, 1, 2, 1]  
sorted_arr = quick_sort(arr)  
print(sorted_arr) # 输出: [1, 1, 2, 3, 6, 8, 10]