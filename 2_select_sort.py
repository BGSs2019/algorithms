numbers = [7, 4, 2, 3, 5, 6, 1, 8, 9]

def find_smallest(elems):
    '''Функция ищет наименьший элемент списка'''
    smallest = elems[0]
    pos = 0
    for i in range(1, len(elems)):
        if elems[i] < smallest:
            smallest = elems[i]
            pos = i
    return smallest, pos

def select_sort(elems):
    '''Функция сортировки выбором'''
    result = []
    for i in range(len(elems)):
        smallest, pos = find_smallest(elems)
        result.append(smallest)
        elems.pop(pos)
    return result

print(find_smallest(numbers))
print(select_sort(numbers))