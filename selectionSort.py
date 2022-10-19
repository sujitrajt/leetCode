def selectionSort(arr):
    length = len(arr)
    for i in range(length):
        minIndex = i 
        for j in range(i+1,length):
            if arr[minIndex] > arr[j]:
                # print(arr[minIndex],arr[j])
                minIndex = j 
        arr[i] , arr[minIndex] = arr[minIndex], arr[i]
    print(arr)

arr=[64, 25, 12, 22, 11]
selectionSort(arr)