from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_traversal(root):
    nodes = []  # трійки (col, row, val)

    # Обхід у ширину з координатами
    queue = deque([(root, 0, 0)])
    while queue:
        node, row, col = queue.popleft()
        if node is None:
            continue
        nodes.append((col, row, node.val))
        queue.append((node.left, row + 1, col - 1))
        queue.append((node.right, row + 1, col + 1))

    nodes.sort()

    result = []
    prev_col = None
    for col, row, val in nodes:
        if col != prev_col:
            result.append([])  # почався новий стовпець
            prev_col = col
        result[-1].append(val)

    return result


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
    result = vertical_traversal(build_tree(values))
    print(f"Вхід: root = {values}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]])
    check([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]])
    check([1, 2, 3, 4, 6, 5, 7], [[4], [2], [1, 5, 6], [3], [7]])
