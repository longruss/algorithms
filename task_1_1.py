import time
size_arr = int(input("Введите размер массива"))
arr = []
i = 0
while i < size_arr:
  element = input("Введите " + str(i + 1) + " элемент")
  arr.append(int(element))
  i += 1
start_time = time.time()
def compare(array):
  perest = 0
  print(array)
  print()
  #compare = 0
  for n in range(1,len(array)):
    #if array[n] >= array[n-1]:
      #compare += 1
    i = n - 1
    while (i > -1) and array[i+1] < array[i]:
        array[i+1], array[i] = array[i], array[i+1]
        i -= 1
        print(array)
        perest += 1
  print()
  print("Количество перестановок = " + str(perest))
  print()
  #print("Количество сравнений = " + str(perest + compare))
  #print()
  print("Конечный массив = " + str(array))
  print()

comp = compare(arr)

print("--- %s seconds ---" % (time.time() - start_time))