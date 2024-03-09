import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:]

        merge_sort(L) 
        merge_sort(R) 

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def python_sort(arr):
    return sorted(arr)

def time_sorting_algorithms(test_data):
    insertion_sort_time = timeit.timeit(
        lambda: [insertion_sort(arr.copy()) for arr in test_data], 
        number=1
    )

    merge_sort_time = timeit.timeit(
        lambda: [merge_sort(arr.copy()) for arr in test_data], 
        number=1
    )

    timsort_time = timeit.timeit(
        lambda: [sorted(arr.copy()) for arr in test_data], 
        number=1
    )

    return insertion_sort_time, merge_sort_time, timsort_time

def main():
    size_of_array = 1000
    number_of_tests = 10
    test_data = [random.sample(range(size_of_array), size_of_array) for _ in range(number_of_tests)]

    results = time_sorting_algorithms(test_data)

    print(f"Insertion Sort Time: {results[0]}")
    print(f"Merge Sort Time: {results[1]}")
    print(f"Timsort Time: {results[2]}")

if __name__ == "__main__":
    main()
