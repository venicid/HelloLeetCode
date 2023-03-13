import queue

"""
创建一个先进先出队列对象
"""
q = queue.Queue()

# 添加元素到队列中
q.put(1)
q.put(2)
q.put(3)

# 从队列中获取元素
print(q.get())  # 输出 1
print(q.get())  # 输出 2
print(q.get())  # 输出 3

# size
print(q.qsize())

# 是否为空
print(q.empty())

"""
创建一个后进先出队列对象
"""
q = queue.LifoQueue()

# 添加元素到队列中
q.put(1)
q.put(2)
q.put(3)

# 从队列中获取元素
print(q.get())  # 输出 3
print(q.get())  # 输出 2
print(q.get())  # 输出 1

"""
创建一个优先级队列对象
"""
q = queue.PriorityQueue()

# 添加元素到队列中，第二个元素的优先级更高
q.put((1, "apple"))
q.put((3, "banana"))
q.put((2, "orange"))

# 从队列中获取元素
print(q.get())  # 输出 (1, "apple")
print(q.get())  # 输出 (2, "orange")
print(q.get())  # 输出 (3, "banana")
