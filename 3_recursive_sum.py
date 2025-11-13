numbers = [7, 4, 2, 3, 5, 6, 1, 8, 9]
print('Реальная сумма:', sum(numbers))

def recursive_sum(elems):
    '''Функция рекурсивно суммирует список'''
    if elems == []:
        return 0
    return elems[0] + recursive_sum(elems[1:])
print('Сумма рекурсией:', recursive_sum(numbers))

def recursive_count(elems):
    '''Функция рекурсивно подсчитывает количество элементов в списке'''
    if elems == []:
        return 0
    return 1 + recursive_count(elems[1:])
print('Длина списка рекурсией:', recursive_count(numbers))

def recursive_max(elems):
    '''Функция находит наибольший элемент в списке'''
    if len(elems) < 2:
        return elems[0]
    return max(elems[1], recursive_max(elems[1:]))
print('Максимум рекурсией:', recursive_max(numbers))

def recursive_binary_search(elems, num):
    '''Рекурсивный бинарный поиск'''
    left = 0
    right = len(elems)
    mid = left + ((right - left) // 2)
    if elems[mid] == num:
        return mid
    if elems[mid] > num:
        return recursive_binary_search(elems[:mid], num)
    if elems[mid] < num:
        return recursive_binary_search(elems[mid:], num)
print('Позиция числа', recursive_binary_search(sorted(numbers), 2))
