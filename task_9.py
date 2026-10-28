from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recover_from_preorder(traversal):
    stack = []
    i = 0
    n = len(traversal)

    while i < n:
        # Рахуємо тире - це глибина вузла
        depth = 0
        while i < n and traversal[i] == "-":
            depth += 1
            i += 1

        # Читаємо число (може бути з кількох цифр)
        value = 0
        while i < n and traversal[i].isdigit():
            value = value * 10 + int(traversal[i])
            i += 1

        node = TreeNode(value)

        # Повертаємось до батька на глибині depth - 1
        while len(stack) > depth:
            stack.pop()

        if stack:
            parent = stack[-1]
            if parent.left is None:
                parent.left = node
            else:
                parent.right = node

        stack.append(node)

    return stack[0] if stack else None


# ---------- Допоміжна функція ----------

def tree_to_list(root):
    """Перетворює дерево у масив формату LeetCode (обхід по рівнях)."""
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


def check(traversal, expected):
    result = tree_to_list(recover_from_preorder(traversal))
    print(f'Вхід: traversal = "{traversal}"')
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check("1-2--3--4-5--6--7", [1, 2, 5, 3, 4, 6, 7])
    check("1-2--3---4-5--6---7", [1, 2, 5, 3, None, 6, None, 4, None, 7])
    check("1-401--349---90--88", [1, 401, None, 349, 88, 90])
