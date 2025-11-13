numbers = [1 ,2, 3, 4, 5, 6, 7, 8, 9]

def binary_search(elems, search):
    '''Функция бинарного поиска принимает
    на вход список и элемент для поиска, 
    возвращает номер элемента в списке'''
    left = 0
    right = len(elems)
    mid = len(elems) // 2

    while elems[mid] != search:
        if search < mid:
            right = mid
            mid = mid // 2
        else:
            left = mid
            mid = mid + ((right - mid) // 2)
    return mid

print(binary_search(numbers, 9))