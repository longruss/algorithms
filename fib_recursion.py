num = input("Какое число найти? ")
num = int(num)
def fib(number):
    if number==1 or number==2:
        return 1
    return fib(number-1) + fib(number-2)
print(str(num) + " число = " + str(fib(num)))


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
