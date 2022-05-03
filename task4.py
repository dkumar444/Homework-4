import math
# Dhanesh kumar 
# 2045141
num_calls=0

def partition(arr, low, high):
    i = (low -1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+ 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    global num_calls
    num_calls+=1
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = []

temp = ""

while temp!="-1":
    temp  = input()
    if temp!="-1":
        arr.append(temp)

n = len(arr)
quickSort(arr, 0, n - 1)

num_calls = (n*int(math.log2(n))) -1

print(num_calls)
for i in range(n):
        print(arr[i])