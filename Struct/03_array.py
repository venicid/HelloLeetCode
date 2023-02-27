"""
数组array
    相同类型，一组连续内存，顺序存储的
扩容机制：
    先为数组分配较小的内存
    当数组容量不足时，需要重新分配更多的空间（通常是2倍）
    把之前的数据复制到新的数组，旧的释放
"""

# 定义
arr = [11, 22, 33, 44, 55]

# 遍历
for i in range(len(arr)):
    print(arr[i], end=" ")  # 11 22 33 44 55

for item in arr:
    print(item, end=" ")

for index, val in enumerate(arr):  # [ɪˈnuːməreɪt]
    print(index, val, end=" ")

p1 = 0
while p1 < len(arr):
    print(arr[p1])
    p1 += 1

"""
增删改查
"""
# 增
arr1 = ["app_name"]

# append 尾部追加
arr1.append("level")
print(arr1)  # ['app_name', 'level']

# extend 合并
arr2 = ["create_time", "update_time"]
arr1.extend(arr2)
print(arr1)  # ['app_name', 'level', 'create_time', 'update_time']

# insert 第i个下标处，增加
arr1.insert(0, "id")
print(arr1)  # ['id', 'app_name', 'level', 'create_time', 'update_time']

new_arr = []
for i in range(len(arr1)):
    if i == 4:
        new_arr.append("lang")
    new_arr.append(arr1[i])
print(new_arr)  # ['id', 'app_name', 'level', 'create_time', 'lang', 'update_time']

# 删
new_arr2 = []
for item in arr1:
    if item == "app_lang":
        continue
    new_arr2.append(item)
print(new_arr2)  # ['id', 'app_name', 'level', 'create_time', 'update_time']

del new_arr2[0]
print(new_arr2)  # ['app_name', 'level', 'create_time', 'update_time']

del new_arr2[1:2]  # [1,2)  删除第一个元素
print(new_arr2)  # ['app_name', 'create_time', 'update_time']

arr1.pop()
print(arr1)   # ['id', 'app_name', 'level', 'create_time']

arr1.remove("create_time")
print(arr1)  # ['id', 'app_name', 'level']

# 改
for i in range(len(arr1)):
    if arr1[i] == "app_name":
        arr1[i] = "APP_NAME"
print(arr1)  # ['id', 'APP_NAME', 'level']

# 查
target_index = arr1.index("level")   # 查询该元素的下标
print(target_index)   # 2

is_exist = "level" in arr1
print(is_exist)  # True

is_exist = False
for i in range(len(arr1)):
    if arr1[i] == "is_sea":
        is_exist = True
        break
print(is_exist)  # False

"""
方法
"""
# join拼接
str1 = ",".join(arr1)
print(str1)  # id,APP_NAME,level
