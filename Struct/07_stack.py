"""栈"""
"""遍历+访问"""


class MyStack:
    """使用list模拟栈"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """栈为空"""
        return not len(self.items)

    def size(self):
        return len(self.items)

    def push(self, item):
        """增：入栈"""
        self.items.append(item)

    def pop(self):
        """删：出栈"""
        return self.items.pop()

    def peek(self):
        """查：查看栈顶"""
        if not self.is_empty():
            return self.items[-1]

    def traverse(self):
        """遍历"""
        res = []
        while not self.is_empty():
            res.append(self.pop())

        return res


if __name__ == '__main__':
    my_stack = MyStack()

    for i in range(10):
        my_stack.push(i)

    res1 = my_stack.traverse()
    print(res1)
