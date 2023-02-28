"""
链表
"""


# 定义
class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def init():
    node1 = LinkNode(1)
    node2 = LinkNode(2)
    node3 = LinkNode(3)

    node1.next = node2
    node2.next = node3

    return node1


# 遍历
def traverse(head):
    res = []
    p1 = head
    while p1 is not None:
        res.append(p1.val)
        p1 = p1.next
    return res


"""
增删改查
"""


# 增-头部
def add_head(head, item):
    node = LinkNode(item)
    node.next = head
    return node


# 增-尾部
def add_tail(head, item):
    node = LinkNode(item)

    if not head:
        return node

    p1 = head
    while p1.next is not None:
        p1 = p1.next
    p1.next = node

    return head


# 增 - 中间
def add_mid(head, index, item):
    node = LinkNode(item)
    if index == 0:
        node.next = head
        return node

    p1 = head
    cnt = 0
    while p1 is not None:
        if cnt == index - 1:
            node.next = p1.next
            p1.next = node
            break
        p1 = p1.next
        cnt += 1
    return head


def add(head, index, item):
    if index == 0:
        node = LinkNode(item)
        node.next = head
        return node
    else:
        pre = head
        for i in range(index - 1):
            if pre.next is not None:
                pre = pre.next
            else:
                return head
        node = LinkNode(item)
        node.next = pre.next
        pre.next = node
        return head


# 删
def remove(head, item):
    if head is None:
        return None

    if head.val == item:
        return head.next

    p1 = head
    while p1.next is not None:
        if p1.next.val == item:
            p1.next = p1.next.next
            break
        p1 = p1.next
    return head


def remove_dummy(head, item):
    dummy = LinkNode(0)
    dummy.next = head

    p1 = dummy
    while p1.next is not None:
        if p1.next.val == item:
            p1.next = p1.next.next
            break
        p1 = p1.next
    return dummy.next


def remove_index(head, index):
    if index == 0:
        head = head.next
        return head
    else:
        pre = head
        for i in range(index - 1):
            if pre.next is not None:
                pre = pre.next
            else:
                return head
        pre.next = pre.next.next
        return head


# 改
def update(head, old, new):
    p1 = head
    while p1 is not None:
        if p1.val == old:
            p1.val = new
            break
        p1 = p1.next
    return head


def update_index(head, index, item):
    p1 = head
    for i in range(index - 1):
        if p1.next is not None:
            p1 = p1.next
        else:
            return head

    p1.val = item
    return head


# 查
def query(head, item):
    p1 = head
    cnt = 0
    while p1 is not None:
        if p1.val == item:
            return cnt
        p1 = p1.next
        cnt += 1
    return None


def query_index(head, index):
    p1 = head
    for i in range(index - 1):
        if p1.next is not None:
            p1 = p1.next
        else:
            return False
    return True


if __name__ == '__main__':
    # 定义
    linked_list = init()
    print(linked_list)  # <__main__.LinkNode object at 0x10118c520>
    print(linked_list.val)  # 1
    print(linked_list.next)  # <__main__.LinkNode object at 0x1012870d0>

    # 遍历
    result = traverse(linked_list)
    print(result)  # [1, 2, 3]

    """
    增删改查
    """
    # 增
    head1 = add_head(linked_list, 99)
    print(traverse(head1))  # [99, 1, 2, 3]

    head2 = add_tail(head1, 100)
    print(traverse(head2))  # [99, 1, 2, 3, 100]

    head3 = add_mid(head2, 11, 88)
    print(traverse(head3))  # [99, 1, 2, 3, 100]

    head4 = add(head3, 4, 77)
    print(traverse(head4))  # [99, 1, 2, 3, 77, 100]

    # 删
    head5 = remove(head4, 99)
    print(traverse(head5))  # [1, 2, 3, 77, 100]

    head5 = remove_dummy(head4, 99)
    print(traverse(head5))  # [1, 2, 3, 77, 100]

    head6 = remove_index(head5, 4)
    print(traverse(head6))  # [1, 2, 3, 77]

    # 改
    head7 = update(head6, 1, 22)
    print(traverse(head7))  # [22, 2, 3, 77]

    head8 = update_index(head7, 3, 66)
    print(traverse(head8))  # [22, 2, 66, 77]

    # 查
    result = query(head8, 77)
    print(result)  # 3

    result2 = query_index(head8, 2)
    print(result2)  # True
