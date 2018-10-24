import time
num = input("Какое число найти? ")
start_time = time.time()
num = int(num)
def fib(number):
	fib_1 = 1
	fib_2 = 1
	i = 2
	while i < number:
		res = fib_2 + fib_1
		print(res)
		fib_1 = fib_2
		fib_2 = res
		i += 1
	print()
	print(str(number) + " число = " + str(res))

fib = fib(num)
print("--- %s seconds ---" % (time.time() - start_time))
			

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
