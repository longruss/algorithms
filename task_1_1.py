#insertion sort

import time
import random
		
def compare(array):
	try:
		start_time = time.time()
		perest = 0
		print(array)
		#if len(array) < 101:
		for n in range(1,len(array)):
			i = n - 1
			while (i > -1) and array[i+1] < array[i]:
				array[i+1], array[i] = array[i], array[i+1]
				i -= 1
				perest += 1
		print("\nКоличество перестановок = " + str(perest) + '\n')
		print("Количество сравнений = " + str(perest + (len(array) - 1)) + '\n')
		print("Отсортированный массив = " + str(array) + '\n')
		print("--- %s seconds ---" % (time.time() - start_time) + '\n')
		#else:
		#	for n in range(1,len(array)):
		#		#while (i > -1) and array[i+1] < array[i]:
		#		for k in range(n, len(array)):
		#			if array[k-1] != 0 and array[k - 1] <= array[k]:
		#				compare += 1
        	#		while (i > -1) and array[i+1] < array[i]:
		#			array[i+1], array[i] = array[i], array[i+1]
		#			i -= 1
		#			perest += 1
		#print("\nКоличество перестановок = " + str(perest) + '\n')
      	#print("Количество сравнений = " + str(perest + compare) + '\n')
		#print("Отсортированный массив = " + str(array) + '\n')
		#print("--- %s seconds ---" % (time.time() - start_time) + '\n')
	except TypeError:
		print("Некорректный ввод")

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
print(compare(menu()))
