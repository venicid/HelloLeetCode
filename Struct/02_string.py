"""
字符串
    不能被修改，只能读操作
    写操作，只能重新定义
"""
# 定义
str1 = "hello world!"

# 遍历
for i in range(len(str1)):
    print(str1[i], end=" ")  # h e l l o   w o r l d !

for item in str1:
    print(item, end=" ")  # h e l l o   w o r l d !

# 指针法
p1 = 0
while p1 < len(str1):
    print(str1[p1], end="")
    p1 += 1

"""
增删改查
"""

# 增
str2 = str1 + " let go \n"
str3 = "%s %s %s" % (str1, "hello code!", 33)
str4 = "I am {}. I am {} ".format("alex", 29)
print(str2)  # hello world! let go
print(str3)  # hello world! hello code! 33
print(str4)  # I am alex. I am 29

# 删
new_str = ""
for i in range(len(str1)):
    if str1[i] == "l":
        continue
    new_str += str1[i]
print(new_str)  # heo word!

# 改
new_str1 = ""
for i in range(len(str1)):
    if str1[i] == "l":
        new_str1 += "L"
    else:
        new_str1 += str1[i]
print(new_str1)  # heLLo worLd!
print(new_str1.replace("h", "H"))  # HeLLo worLd!

# 查
is_exist = False
for i in range(len(str1)):
    if str1[i] == "!":
        is_exist = True
print(is_exist)  # True

print(str1.find("d"), str1[str1.find("d")], str1.find("d") != -1)  # 10 d True

"""
方法
"""
# 拼接、格式化
str2 = str1 + " let go \n"
str3 = "%s %s %s" % (str1, "hello code!", 33)
str4 = "I am {}. I am {} ".format("alex", 29)

# 生成字符串
array1 = ["1.1.1.1", "3306"]
ip_port = ":".join(array1)
print(ip_port)  # 1.1.1.1:3306

# 反转
str8 = "hello world!"
print(str8[::-1])  # !dlrow olleh

# split
arr8 = str8.split()
print(arr8)  # ['hello', 'world!']
