from Common import genIntArray

def bubble_sort(arr : list[int]) -> list[int]:

    array_size = len(arr)
    for i in range(array_size):

        swaps=0
        for j in range (0, array_size-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swaps += 1

            if(swaps ==0):
                exit
        print(arr)
    return arr

if __name__ == "__main__":
    
    arr = genIntArray(5, 100)
    print(f"Input -> {arr}")
    print(f"Output -> {bubble_sort(arr)}")