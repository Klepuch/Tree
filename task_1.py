from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


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


def check(p, q, expected):
    result = is_same_tree(build_tree(p), build_tree(q))
    print(f"Вхід: p = {p}, q = {q}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 2, 3], [1, 2, 3], True)
    check([1, 2], [1, None, 2], False)
    check([1, 2, 1], [1, 1, 2], False)
    check([], [], True)
