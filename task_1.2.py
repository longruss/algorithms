import time
import random

def gnome_sort(array):
	i = 1
	numb_of_perest = 0
	numb_of_comp = 0
	while i < len(array):
		if not i or array[i - 1] <= array[i]:
			i+=1
			numb_of_comp += 1
		else:
			array[i], array[i - 1] = array[i - 1], array[i]
			i-=1
			numb_of_perest += 1
	print("Кол-во сравнений: " + str(numb_of_comp) + "\n"
	"Кол-во перестановок: " + str(numb_of_perest) + "\n")
	return array

def menu():
	print("1) отсортировать введенный массив\n" + 
	"2) отсортировать массив из 100 случайных элементов\n" +
	"3) отсортировать массив из 1000 случайных элементов\n")
	choose = input("Выберите, что сделать \n")
	arr = []
	i = 0
	if choose == '1':
		size_arr = int(input("Введите размер массива "))
		while i < size_arr:
			element = input(str(i + 1) + " элемент ")
			arr.append(int(element))
			i += 1
		return arr
	elif choose == '2':
		while i < 100:
			arr.append(random.randint(0, 100))
			i += 1
		return arr
	elif choose == '3':
		while i < 1000:
			arr.append(random.randint(0, 100))
			i += 1
		return arr
	else:
		return

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    print(gnome_sort(menu()))
    sys.exit(main(sys.argv))
