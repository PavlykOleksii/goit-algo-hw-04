import random
import timeit

# 1. Insertion Sort (Сортування вставками)
def insertion_sort(arr):
    arr = arr.copy()  # Копіюємо, щоб не змінювати вихідний масив
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# 2. Merge Sort (Сортування злиттям)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 3. Quick Sort (Швидке сортування)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Функція для запуску вимірювання часу
def benchmark():
    sizes = [100, 1000, 5000]  # Розміри тестових масивів
    print(f"{'Розмір':<10} | {'Insertion':<12} | {'Merge':<12} | {'Quick':<12} | {'Timsort':<12}")
    print("-" * 68)

    for size in sizes:
        # Ґенеруємо випадковий масив чисел
        data = [random.randint(0, 10000) for _ in range(size)]

        # Вимірюємо час для кожного алгоритму (в секундах)
        t_insertion = timeit.timeit(lambda: insertion_sort(data), number=50) / 5
        t_merge = timeit.timeit(lambda: merge_sort(data), number=50) / 5
        t_quick = timeit.timeit(lambda: quick_sort(data), number=50) / 5
        t_timsort = timeit.timeit(lambda: sorted(data), number=50) / 5

        print(
            f"{size:<10} | {t_insertion:<12.6f} | {t_merge:<12.6f} | {t_quick:<12.6f} | {t_timsort:<12.6f}"
        )


if __name__ == "__main__":
    benchmark()