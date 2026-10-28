import sys
from collections import deque

sys.setrecursionlimit(10000)

NOT_COVERED = 0
HAS_CAMERA = 1
COVERED = 2


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_camera_cover(root):
    cameras = 0

    def dfs(node):
        nonlocal cameras
        if node is None:
            return COVERED

        left = dfs(node.left)
        right = dfs(node.right)

        if left == NOT_COVERED or right == NOT_COVERED:
            cameras += 1
            return HAS_CAMERA
        if left == HAS_CAMERA or right == HAS_CAMERA:
            return COVERED
        return NOT_COVERED

    if dfs(root) == NOT_COVERED:
        cameras += 1
    return cameras


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
    result = min_camera_cover(build_tree(values))
    print(f"Вхід: root = {values}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([0, 0, None, 0, 0], 1)
    check([0, 0, None, 0, None, 0, None, None, 0], 2)
    check([0], 1)
