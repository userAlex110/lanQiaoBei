"""
问题描述
本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。

小蓝要把一个字符串中的字母按其在字母表中的顺序排列。

例如:LANQIAO 排列后为 AAILNOQ。

又如:GOODGOODSTUDYDAYDAYUP 排列后为 AADDDDDGGOOOOPSTUUYYY。

请问对于以下字符串，排列之后字符串是什么？

WHERETHEREISAWILLTHEREISAWAY
"""

# 如果推广使用input(),就是直接传入一个字符串。
# 并不是一个列表类型。 
s = "WHERETHEREISAWILLTHEREISAWAY"
print(s)
print(type(s)) # <class 'str'>

print()

# 在python中列表，元组，集合，字典，字符串都是可迭代对象。
# 可以使用for循环来遍历。
s = sorted(s) # sorted()函数对可迭代对象进行排序，返回一个新的列表。
print(s) # 以单个字母为元素的列表
print("".join(s)) #返回通过指定字符，连接序列中元素后生成的，新字符串。