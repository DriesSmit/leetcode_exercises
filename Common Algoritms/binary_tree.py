class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# In-order DFS: Left, Root, Right
def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.data, end=' ')
    in_order_dfs(node.right)

# Pre-order DFS: Root, Left, Right
def pre_order_dfs(node):
    if node is None:
        return
    print(node.data, end=' ')
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)

# Post-order DFS: Left, Right, Root
def post_order_dfs(node):
    if node is None:
        return
    post_order_dfs(node.left)
    post_order_dfs(node.right)
    print(node.data, end=' ')

# BFS: Level order traversal
def bfs(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

if __name__ == "__main__":
    # Creating the tree
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print("In-order DFS: ", end='')
    in_order_dfs(root)
    print("\nPre-order DFS: ", end='')
    pre_order_dfs(root)
    print("\nPost-order DFS: ", end='')
    post_order_dfs(root)
    print("\nLevel order: ", end='')
    bfs(root)