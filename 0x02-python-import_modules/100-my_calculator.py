#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    import calculator_1

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    calc = calculator_1
    func = {'+': calc.add, '-': calc.sub, '/': calc.div, '*': calc.mul}
    a = sys.argv[1]
    op = sys.argv[2]
    b = sys.argv[3]

    if op in '-+/*':
        print("{} {} {} = {}".format(a, op, b, func[op](int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
