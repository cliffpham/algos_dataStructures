import create_binary_tree

def smaller_values(root, target):
    if not root:
        return 0

    values = []
    visit(root, target, values)

    print('There are ' + str(len(values)) + ' values that are less than ' + str(target) + ': ', end='')
    return values

def visit(root, target, values):
    if not root:
        return

    if root.data < target:
        values.append(root.data)

    visit(root.left, target, values)
    visit(root.right, target, values) 

    return

# root = create_binary_tree.Node(12)
# root.insert(4)
# root.insert(16)
# root.insert(3)
# root.insert(8)   

# print(smaller_values(root, 4))
# print(smaller_values(root, 12))