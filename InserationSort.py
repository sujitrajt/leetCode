def insertSort(arr):
    lengthOfArray = len(arr)
    for i in range(1, lengthOfArray):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key : 
            arr[j + 1] = arr[j]
            j -= 1 
        arr[j + 1 ] = key 
    print(arr)
arr =[7,4,5,2]
insertSort(arr)
