def gnome_sort(arr):
    i = 1
    while i < len(arr):
        if not i or arr[i - 1] <= arr[i]:
            i+=1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i-=1
    return arr
