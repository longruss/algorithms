def creating(table, numb_of_keys):
    k = 1
    for k in range (numb_of_keys):
        table.update({k:[k]})
        #Вывод
    for key in range (numb_of_keys):
        print(str(key) + " | " + str(table[key]))
    return (hash_table)

def sort(array):
	i = 1
	while i < len(array):
		if not i or array[i - 1] <= array[i]:
			i+=1
		else:
			array[i], array[i - 1] = array[i - 1], array[i]
			i-=1
	return array

def hash_get(table):
    return (table.get(key, default))

#def append(table, array, table_key):
    #for key in range(table_key):

        #print(a)
                


def main(args):
    return 0


if __name__ == "__main__":
    numbers = []
    print("Введите числа для сортировки: ")
    numbers = list(map(int, input().split()))
    print(numbers)
    sort(numbers)
    print("отсортированный массив: " + str(numbers))
    k = int(input("Чему равно k?: "))
    hash_table = dict()
    creating(hash_table, k)
    #append(hash_table, numbers, k)
    print(hash_get(hash_table))
