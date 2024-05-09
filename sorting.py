import time
import random

def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp

def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

def counting_sort(a):
    M = max(a)
    count_array = [0] * (M + 1)
    output_array = [0] * len(a)

    for num in a:
        count_array[num] += 1

    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    for i in range(len(a) - 1, -1, -1):
        output_array[count_array[a[i]] - 1] = a[i]
        count_array[a[i]] -= 1

    return output_array

def digit_count_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        digit_count_sort(arr, exp)
        exp *= 10

def partition(array, left, right):
    pivot = array[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and array[i] < pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    array[left], array[j] = array[j], array[left]
    return j

def quicksort(array, left, right):
    if left < right:
        j = partition(array, left, right)
        quicksort(array, left, j - 1)
        quicksort(array, j + 1, right)

def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


arr = [random.randint(1, 999) for _ in range(10000)]
arr1 = arr.copy()
arr2 = arr.copy()
arr3 = arr.copy()
arr4 = arr.copy()
arr5 = arr.copy()
arr6 = arr.copy()
arr7 = arr.copy()

start = time.time()
bubble_sort(arr1)
end = time.time()
totalTime = end - start
print('bubble: ', totalTime)

start = time.time()
insertion_sort(arr2)
end = time.time()
totalTime = end - start
print('insertion: ', totalTime)

start = time.time()
selection_sort(arr3)
end = time.time()
totalTime = end - start
print('selection: ', totalTime)

start = time.time()
quicksort(arr4, 0, len(arr4) - 1)
end = time.time()
totalTime = end - start
print('quick: ', totalTime)

start = time.time()
mergesort(arr5)
end = time.time()
totalTime = end - start
print('merge: ', totalTime)

start = time.time()
radix_sort(arr6)
end = time.time()
totalTime = end - start
print('radix: ', totalTime)

start = time.time()
arr = counting_sort(arr7)
end = time.time()
totalTime = end - start
print('counting: ', totalTime)
