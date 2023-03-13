"""
树
"""


# 定义

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree():
    """
            1
        2       3
    4     5   6   7
    :return:
    """
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    return node1


"""
遍历
"""


def mid_traverse(tree, result):
    if tree is not None:
        mid_traverse(tree.left, result)

        # print(tree.val)
        result.append(tree.val)

        mid_traverse(tree.right, result)
    return result


def pre_traverse(tree, result):
    if tree is not None:
        # print(tree.val)
        result.append(tree.val)

        pre_traverse(tree.left, result)
        pre_traverse(tree.right, result)
    return result


def tail_traverse(tree, result):
    if tree is not None:
        tail_traverse(tree.left, result)
        tail_traverse(tree.right, result)

        # print(tree.val)
        result.append(tree.val)
    return result


# 迭代遍历
# 左 根 右
def in_order_traverse(tree):
    result = []
    stack = []
    cur = tree
    while cur is not None or len(stack) != 0:

        while cur is not None:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right

    return result

# 根，左，右
def pre_order_traverse(tree):
    result = []
    stack = []
    cur = tree
    while cur is not None or len(stack) != 0:

        while cur is not None:
            result.append(cur.val)
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        cur = cur.right

    return result


# 左 右 根
def post_order_traverse(tree):
    result = []
    stack = []
    cur = tree
    pre = None
    while cur is not None or len(stack) != 0:

        while cur is not None:
            stack.append(cur)
            cur = cur.left

        cur = stack[-1]
        if cur.right is not None and cur.right != pre:
            cur = cur.right
        else:
            stack.pop()
            result.append(cur.val)
            pre = cur
            cur = None

    return result


if __name__ == '__main__':
    tree1 = build_tree()

    res_mid = []
    res_pre = []
    res_tail = []

    print(mid_traverse(tree1, res_mid))
    print(pre_traverse(tree1, res_pre))
    print(tail_traverse(tree1, res_tail))
    print()

    print(in_order_traverse(tree1))
    print(pre_order_traverse(tree1))
    print(post_order_traverse(tree1))
