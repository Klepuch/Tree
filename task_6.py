import sys
from collections import deque

sys.setrecursionlimit(100000)  # дерево може мати до 30 000 вузлів у глибину


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    best = root.val

    def gain(node):
        nonlocal best
        if node is None:
            return 0
        left = max(0, gain(node.left))
        right = max(0, gain(node.right))
        # Шлях, що проходить через node і обидві гілки
        best = max(best, node.val + left + right)
        # Вгору можна передати лише одну гілку
        return node.val + max(left, right)

    gain(root)
    return best


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
    result = max_path_sum(build_tree(values))
    print(f"Вхід: root = {values}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 2, 3], 6)
    check([-10, 9, 20, None, None, 15, 7], 42)
    check([-3], -3)
