# This is a sample Python script.
import argparse
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def cubed(n):
    #TODO
    return []

def squared(n):
    """returns list of numbers squared"""
    answers = []
    for i in range(1,n+1):
        answers.append(i*i)
    return answers

    #compact alternative
    #return [i*i for i in range(1,n)]

def fibonacci(n):
    """Returns the nth number of fibonacci sequence"""

    cache = {0: 0, 1: 1, 2: 1}

    def fib(n):
        if n == 0 or n == 1:
            return n
        if n in cache:
            return cache[n]
        else:
            #current number equals last two added together
            cache[n] = fib(n-2) + fib(n-1)
            return cache[n]
    return fib(n)

def pascal(n):

    """
    Returns a 2d array like such
    [1]
    [1,1]
    [1,2,1]
    [1,4,6,4,1]
    [1,5,10,10,5,1]
    [1,6,15,20,15,6,1]
    """

    if n < 1:
        return []
    answers = [[1]]
    for i in range(1, n):
        row = []
        row.append(1)
        for j in range(1, i):
            row.append(answers[i - 1][j - 1] + answers[i - 1][j])
        row.append(1)
        answers.append(row)
    return answers

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('operation', metavar='op', type=str,
                        help='the operation to do. Valid ops are pascal, fibonacci, squared, cubed')
    parser.add_argument('integer', metavar='N', type=int, help='an integer for the accumulator')

    args = parser.parse_args()

    #Should use Enum and Try/Catch but whatever
    if args.operation == 'pascal':
        print(pascal(args.integer))
    elif args.operation == 'fibonacci':
        print(fibonacci(args.integer))
    elif args.operation == 'squared':
        print(squared(args.integer))
    elif args.operation == 'cubed':
        print(cubed(args.integer))
    else:
        parser.print_help()
        print("{0} was an invalid operation!".format(args.operation))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
