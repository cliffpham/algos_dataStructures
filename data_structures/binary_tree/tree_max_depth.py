import create_binary_tree

def max_depth(root):
    level = 0
    return visit(root, level)

def visit(root, level):
    if not root:
        return level
    
    level += 1
    
    l = visit(root.left, level)
    r = visit(root.right, level)

    return max(l, r)

root = create_binary_tree.Node(12)
root.insert(4)
root.insert(16)
root.insert(3)
root.insert(8)

print(max_depth(root))