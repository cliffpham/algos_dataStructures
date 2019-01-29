import create_binary_tree

def postorder_traversal(root):
    if not root:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data)

# root = create_binary_tree.Node(12)
# root.insert(4)
# root.insert(16)
# root.insert(3)
# root.insert(8)

# postorder_traversal(root)