import create_binary_tree

def find_node(root, target):
    if not root:
        return False

    found = [False]
    visit(root, target, found)
    
    return found[0]

def visit(root,target,found):
    if not root:
        return 

    if root.data == target:
        found[0] = True
        return 

    visit(root.left, target, found)
    visit(root.right, target, found)

    return found

# root = create_binary_tree.Node(12)
# root.insert(4)
# root.insert(16)
# root.insert(3)
# root.insert(8)

# print(find_node(root, 3))
# print(find_node(root, 20))
