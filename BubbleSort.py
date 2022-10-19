def BubbleSort(arr):
    length = len(arr) 
    for i in range(length):
        for j in range(0,length-i-1):
            print(arr[j])
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] ,arr[j]
    print(arr)
arr=[64, 25, 12, 22, 11]
BubbleSort(arr)