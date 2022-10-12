def calc(expr):
    operator_function = {
        '-': lambda x, y: x - y,
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    nums = list()
    opers = list()

    tks = list('(' + expr + ')')

    while tks:
        tk = tks.pop(0)

        if tk.isdecimal():
            nums.append(float(tk))
        else:
            if tk == ')':
                oper = opers.pop()
                while opers and oper != '(':
                    b, a = nums.pop(), nums.pop()
                    f = operator_function[oper]
                    nums.append(f(a, b))

                    oper = opers.pop()

            else:
                opers.append(tk)

    return nums[0]


if __name__ == '__main__':
    print(calc("((1+(2*3))*2)+4"))  