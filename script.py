def find_sum_between_max_min(arr):
    if len(arr) == 0:
        return 0  # Если массив пустой

    max_index = arr.index(max(arr))  # Индекс максимального элемента
    min_index = arr.index(min(arr))  # Индекс минимального элемента

    # Определение границ между max и min
    start = min(max_index, min_index) + 1
    end = max(max_index, min_index)

    # Суммирование отрицательных элементов
    negative_sum = sum(x for x in arr[start:end] if x < 0)

    return negative_sum

# Пример использования
A = [1, -3, 4, -5, 6, -2, 10]
result = find_sum_between_max_min(A)
print("Сумма отрицательных элементов:", result)
