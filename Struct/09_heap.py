import heapq

import heapq


class Heap:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, item):
        heapq.heappush(self.items, item)

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def size(self):
        return len(self.items)

    def preorder_traversal(self):
        def _traverse(i):
            if i >= len(self.items):
                return []
            node = self.items[i]
            left = _traverse(2 * i + 1)
            right = _traverse(2 * i + 2)
            return [node] + left + right

        return _traverse(0)

    def inorder_traversal(self):
        def _traverse(i):
            if i >= len(self.items):
                return []
            node = self.items[i]
            left = _traverse(2 * i + 1)
            right = _traverse(2 * i + 2)
            return left + [node] + right

        return _traverse(0)

    def postorder_traversal(self):
        def _traverse(i):
            if i >= len(self.items):
                return []
            node = self.items[i]
            left = _traverse(2 * i + 1)
            right = _traverse(2 * i + 2)
            return left + right + [node]

        return _traverse(0)


if __name__ == '__main__':
    """
     最小堆
     """
    # 实例化堆对象
    h = Heap()

    # 向堆中添加元素
    h.push(3)
    h.push(1)
    h.push(4)
    h.push(1)
    h.push(5)

    # 打印堆中的元素
    print(h.items)

    # 弹出堆顶元素
    print(h.pop())

    # 打印堆中的元素
    print(h.items)

    # 打印堆顶元素
    print(h.peek())

    # 打印堆的大小
    print(h.size())

    # 遍历堆
    print("Preorder Traversal:", h.preorder_traversal())
    print("Inorder Traversal:", h.inorder_traversal())
    print("Postorder Traversal:", h.postorder_traversal())
