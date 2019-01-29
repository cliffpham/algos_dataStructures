import create_binary_tree

def inorder_traversal(root):
    if not root:
        return
    
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)

# root = create_binary_tree.Node(25)
# root.insert(15)
# root.insert(50)
# root.insert(10)
# root.insert(22)

# inorder_traversal(root)