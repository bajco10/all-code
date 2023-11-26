"""import timeit
import random

print(f"{'n':10s}{'list':>10s}{'dict':>10s}")
for i in range(10_000, 1_000_001, 20_000):
    t = timeit.Timer(f"random.randrange({i}) in x",
    "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    dict_time = t.timeit(number=1000)
    print(f"{i:<10,}{lst_time:>10.3f}{dict_time:>10.3f}")"""

class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)

def rev_string(my_str):
    m = Stack()
    for i in my_str:
        m.push(i)
    r = ""
    while not m.is_empty():
        r+=m.pop()
    return r

# print(rev_string("apple"))
# print(rev_string("1234567890"))

# checkign if parentheses are valid using stacks
def par_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()

    return s.is_empty()

# checking for multiple types of parentheses
def balance_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(), symbol):
                    return False

    return s.is_empty()

def matches(sym_left, sym_right):
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)

# converting decimal numbers into binary

def divide_by_2(decimal_num):
    b_stack = Stack()
    while decimal_num > 0:
        b_stack.push(decimal_num%2)
        decimal_num = decimal_num//2
    b_string = ""
    while not b_stack.is_empty():
        b_string=b_string+str(b_stack.pop())
    return b_string

def base_converter(decimal_num, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res_stack = Stack()
    while decimal_num > 0:
        rem = decimal_num % base
        res_stack.push(digits[rem])
        decimal_num = decimal_num // base
    
    res_string = ""
    while not res_stack.is_empty():
        res_string = res_string + str(res_stack.pop())
    
    return res_string

print(base_converter(26, 26))

# converting expression into postfix type

def infix_to_postfix(infix_expr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)

print(infix_to_postfix("5 * 3 ^ (4 - 2)"))

# evaluating postfix expressions
def postfix_eval(postfix_expr):
    operand_stack = Stack()
    tokens = postfix_expr.split()
    for token in tokens:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            res = do_math(token, op1, op2)
            operand_stack.push(res)
    return operand_stack.pop()

def do_math(op, op1, op2):
    if op == "+":
        return op1+op2
    elif op == "-":
        return op1-op2
    elif op == "*":
        return op1*op2
    elif op == "^":
        return op1^op2
    else:
        return op1/op2

# print(postfix_eval("17 10 + 3 * 9 /"))