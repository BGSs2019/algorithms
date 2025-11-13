import random

nums = [3, 4, 2, 1, 5, 6, 9, 8, 0, 7]

def fast_sort(nums):
    '''Быстрая сортировка'''
    if len(nums) < 2:
        return nums
    else:
        result = []
        support = [random.choice(nums)]
        less = fast_sort([elem for elem in nums if elem < support[0]])
        greater = fast_sort([elem for elem in nums if elem > support[0]])
    result = less + support + greater
    return result

print(fast_sort(nums))