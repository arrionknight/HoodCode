#Move that mug in the right place algorithm 
def partition(array, low, high):
    n = len(array)
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    

if __name__ == "__main__":
    arr = [1,4,2,0,3]
    partition(arr, 0, len(arr) - 1)
    print(arr)
