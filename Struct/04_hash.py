"""
散列表 哈希表 hash table

时间复杂度
    插入、删除、查找 O(1)

原理：数组、链表、扩容
    使用1个数组，快速确定，元素在哈希表中的位置
    元素的位置，为它的哈希值除以数组的长度的余数

    多个哈希值不同的元素，可能被存入同一位置(余数相同)
    数组的每一个位置都对应一个链表
    存入同一位置的多个元素，都被添加到同一个链表中

    为了确保链表的长度不会太长，需要计算哈希表中元素的个数与数组长度的比值
    当这个比值超过某个阈值，就对数组进行扩容(通常是2倍)，并重新分配哈希表中的元素

装配因子 0.75
    时间和空间成本的权衡 ==> 决定了扩容因子是0.75 ==>决定了泊松分布的参数λ是0.5
    ==> 计算出泊松分布结果为8时，概率为亿分之六 ==> 决定了树化节点为8.

    https://zhuanlan.zhihu.com/p/396019103


"""

# 定义
hash_map1 = {"id": 1, "name": "AppCMDB"}

# 遍历
for key in hash_map1:
    print(key, hash_map1.get(key), hash_map1[key])  # id 1 1

for val in hash_map1.items():
    print(val)  # ('id', 1)  ('name', 'AppCMDB')

for key in hash_map1.keys():
    print(key)  # id name

for index, key in enumerate(hash_map1):
    print(index, key, hash_map1[key])  # 0 id 1   # 1 name AppCMDB

"""
增删改查
"""
# 增
hash_map1.update({"age": 22})
print(hash_map1)  # {'id': 1, 'name': 'AppCMDB', 'age': 22}

hash_map1["salary"] = 50
print(hash_map1)  # {'id': 1, 'name': 'AppCMDB', 'age': 22, 'salary': 50}

# 删
hash_map1.pop("age")
print(hash_map1)  # {'id': 1, 'name': 'AppCMDB', 'salary': 50}

del hash_map1["salary"]
print(hash_map1)  # {'id': 1, 'name': 'AppCMDB'}

# 改
hash_map1["name"] = "appCmdb"
print(hash_map1)  # {'id': 1, 'name': 'appCmdb'}

# 查
val = hash_map1.get("name")
page_number = hash_map1.get("page_number")
page_size = hash_map1.get("page_size", 10)

print(val)  # appCmdb
print(page_number)  # None
print(page_size)  # 10

"""
方法
"""
# 存在
print("id" in hash_map1)  # True

is_exist = False
for key in hash_map1:
    if hash_map1.get(key) == 1:
        is_exist = True
        break
print(is_exist)  # True

# keys  values items
keys = hash_map1.keys()
print(keys, type(keys))  # dict_keys(['id', 'name']) <class 'dict_keys'>
print(list(keys), type(list(keys)))  # ['id', 'name'] <class 'list'>

values = hash_map1.values()
print(values, type(values))    # dict_values([1, 'appCmdb']) <class 'dict_values'>

items = hash_map1.items()
print(items, type(items))   # dict_items([('id', 1), ('name', 'appCmdb')]) <class 'dict_items'>
print(list(items), type(list(items)))  # [('id', 1), ('name', 'appCmdb')] <class 'list'>

# 深浅copy
d1 = {"ip": "1.1.1.1"}
d2 = d1

print(id(d1))  # 4406457536
print(id(d2))  # 4406457536

# 浅copy
d2["ip"] = "2.2.2.2"
print(d2)  # {'ip': '2.2.2.2'}
print(d1)  # {'ip': '2.2.2.2'}
print(id(d1))  # 4378109184
print(id(d2))  # 4378109184

# 深copy
import copy

d3 = copy.deepcopy(d2)
print(id(d2))  # 4378109184
print(id(d3))  # 4378509824

d3["ip"] = "3.3.3.3"
print(d2)  # {'ip': '2.2.2.2'}
print(d3)  # {'ip': '3.3.3.3'}
print(id(d2))  # 4378509824
print(id(d3))  # 4509962816
