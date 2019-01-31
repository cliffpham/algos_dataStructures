# generic recursion skeleton 

def recur_skeleton(counter, index, mutable_param, output):
    if index == counter: # aka a list, a num
        return output
    #go down one side of the recursion tree
    recur_skeleton(counter, index+1, mutable_param, output)

    do_something(mutable_param)
    recur_skeleton(counter, index, mutable_param, output)

    return

def do_something(param):
    return

