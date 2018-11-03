def gnome_sort(array):
	i = 1
	while i < len(array):
		if not i or array[i - 1] <= array[i]:
			i+=1
		else:
			array[i], array[i - 1] = array[i - 1], array[i]
			i-=1
	return array

def main(args):
    return 0

if __name__ == '__main__':
	import sys
	numb_of_nominals = int(input("Введите число номиналов "))
	print("Введите эти номиналы \n")
	arr = []
	i = 0
	while i < numb_of_nominals:
		arr.append(int(input(str(i + 1) + ": ")))
		i += 1
	arr = gnome_sort(arr)
	print("\n" + str(arr))
	numb_of_money = int(input("Введите число, которое нужно разменять \n"))
	numb_of_coins = 0
	n = len(arr)
	while n > 0:
		numb_of_coins += (numb_of_money // arr[n-1])
		numb_of_money = numb_of_money % arr[n-1]
		if numb_of_money == 0:
			break
		n -= 1
	print (numb_of_coins)
	sys.exit(main(sys.argv))
