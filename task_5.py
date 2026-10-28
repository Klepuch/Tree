from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        if root is None:
            return ""
        parts = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                parts.append("#")
                continue
            parts.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        # Відкидаємо порожні вузли в кінці - вони нічого не означають
        while parts and parts[-1] == "#":
            parts.pop()
        return ",".join(parts)

    def deserialize(self, data):
        if data == "":
            return None
        parts = data.split(",")
        root = TreeNode(int(parts[0]))
        queue = deque([root])
        i = 1
        while queue and i < len(parts):
            node = queue.popleft()
            # Лівий нащадок
            if i < len(parts) and parts[i] != "#":
                node.left = TreeNode(int(parts[i]))
                queue.append(node.left)
            i += 1
            # Правий нащадок
            if i < len(parts) and parts[i] != "#":
                node.right = TreeNode(int(parts[i]))
                queue.append(node.right)
            i += 1
        return root


# ---------- Допоміжні функції ----------

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


def tree_to_list(root):
    """Перетворює дерево назад у масив формату LeetCode."""
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def check(values, expected):
    codec = Codec()
    data = codec.serialize(build_tree(values))
    result = tree_to_list(codec.deserialize(data))
    print(f"Вхід: root = {values}")
    print(f'Серіалізований рядок: "{data}"')
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 2, 3, None, None, 4, 5], [1, 2, 3, None, None, 4, 5])
    check([], [])
    check([-1000, None, 1000], [-1000, None, 1000])
