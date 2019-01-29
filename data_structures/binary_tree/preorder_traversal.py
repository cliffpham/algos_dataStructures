import create_binary_tree

def preorder_traversal(root):
    if not root:
        return

    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)

# root = create_binary_tree.Node(12)
# root.insert(4)
# root.insert(16)
# root.insert(3)
# root.insert(8)

# preorder_traversal(root)