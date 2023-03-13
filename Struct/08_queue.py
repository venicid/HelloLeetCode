"""队列"""
"""遍历 + 访问"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def traverse(self):
        result = []
        while not self.is_empty():
            result.append(self.dequeue())
        return result


if __name__ == '__main__':
    # 创建一个队列对象
    q = Queue()

    # 添加元素
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # 从队列头部删除元素
    print(q.dequeue())  # 输出 1

    # 判断队列是否为空
    print(q.is_empty())  # 输出 False

    # 查看队列中元素的数量
    print(q.size())  # 输出 2

    # 遍历
    print(q.traverse())
