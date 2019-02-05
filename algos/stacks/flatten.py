def flatten(nested):
    output = []

    return recur(nested, output)

def recur(nested, output):
    nested = queue_ify(nested)
    while nested:
        cur = nested.pop()
        if isinstance(cur, (list, tuple)):
            recur(cur, output)
        else:
            output.append(cur)

    return output

def queue_ify(input_stack):
    output = []
    while input_stack:
        output.append(input_stack.pop())
    return output

nests = [1, 2, [3, 4, [5],['hi']], [6, [[[7, 'hello']]]]]
print(flatten(nests))

