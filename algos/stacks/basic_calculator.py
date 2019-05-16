import math
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
        solve("2-(5-6)"),
        3
    ),
    def test2(self):
        self.assertEqual(
        solve("(7)-(0)+(4)"),
        11
    )

OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+':1, '-':1}

def peek(stack):
    top = None
    if len(stack) >= 1:
        top = stack[len(stack) - 1]
    return top

def que_ify(stack):
    stack = list(stack)
    queue = []
    while stack:
        cur = stack.pop()
        queue.append(cur)
    return queue

def get_integer(eval):
    on = True
    res = 0
    while on:
        cur = peek(eval)
        if len(eval) >= 1 and ord(cur) >= 48 and ord(cur) <= 57:
            cur = eval.pop()
            res *= 10
            res += int(cur)
        else:
            on = False
    return res

def create_eval(stack):
    output = []
    eval = que_ify(stack)
    is_int = False
    res = 0

    while eval:
        cur = peek(eval)
        if len(eval) >= 1 and ord(cur) >= 48 and ord(cur) <= 57:
            integer = get_integer(eval)
            output.append(integer)
        else:
            output.append(eval.pop())
    return output

def infix_to_postfix(formula):
    stack = [] # only pop when the coming op has priority
    output = []
    for ch in formula:
        if ch not in OPERATORS:
            if ch != ' ':
                output.append(ch)
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop() # pop '('
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack: output += stack.pop()
   # print output
    return output

def evaluate_postfix(formula):
    stack = []
    for ch in formula:
        if ch not in OPERATORS:
            stack.append(float(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            c = {'+':a+b, '-':a-b}[ch]
            stack.append(c)
    return math.trunc(stack[-1])

def solve(formula):
    formula = create_eval(formula)
    expression = infix_to_postfix(formula)
    return evaluate_postfix(expression)

if __name__ == "__main__":
    unittest.main()
