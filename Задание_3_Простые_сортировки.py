def bubble_sort(arr):
    n = len(arr)
    sorted = False  # Флаг для проверки отсортированности списка

    while not sorted:
        sorted = True  # Предполагаем, что список уже отсортирован
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                sorted = False  # Если выполнена перестановка, список не отсортирован
        n -= 1  # Уменьшаем количество итераций на каждой итерации внешнего цикла

    return arr

# Пример использования
nums = [9, 2, 7, 4, 5, 1, 8, 3, 6]
print("Исходный список:", nums)

sorted_nums = bubble_sort(nums)
print("Отсортированный список:", sorted_nums)
