def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def diameter(node):
    if node is None:
        return 0
    
    l_height = height(node.left)
    r_height = height(node.right)
    
    l_diameter = diameter(node.left)
    r_diameter = diameter(node.right)