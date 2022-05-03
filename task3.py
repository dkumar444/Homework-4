# Dhanesh kumar 
# 2045141

def display(array):
    for item in array:
        print(f"{item} ",end = "")

def selection_sort_descend_trace(array):
    for i in range(len(array)):
        max_index = i
        for j in range(i + 1, len(array)):
            if array[j] > array[max_index]:
                max_index = j
        array[i], array[max_index] = array[max_index], array[i]

        # print(array)
        if i < len(array) - 1:
            display(array)
            print()
    return array

if __name__ == '__main__':
    array = []
    array = list(map(int, input().split(" ")))
    array  = selection_sort_descend_trace(array)