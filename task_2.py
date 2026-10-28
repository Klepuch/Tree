from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_mirror(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (a.val == b.val
            and is_mirror(a.left, b.right)
            and is_mirror(a.right, b.left))


def is_symmetric(root):
    if root is None:
        return True
    return is_mirror(root.left, root.right)


# ---------- Допоміжна функція ----------

def build_tree(values):
    """Будує дерево з масиву у форматі LeetCode (обхід по рівнях, None - порожньо)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def check(values, expected):
    result = is_symmetric(build_tree(values))
    print(f"Вхід: root = {values}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 2, 2, 3, 4, 4, 3], True)
    check([1, 2, 2, None, 3, None, 3], False)
    check([1, 2, 1], False)
    check([1], True)
