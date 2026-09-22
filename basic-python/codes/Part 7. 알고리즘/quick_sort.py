import random


def quick_sort(arr):
    # 순서를 보자면
    # 피벗을 뽑기
    # 왼쪽 배열에 피벗보다 작은 값을 담는다
    # 오른쪽 배열에 피벗보다 큰 값을 담는다.
    # 왼쪽 배열을 대상으로 퀵소트를 재수행한다
    # 오른쪽 배열을 대상으로 퀵소트를 재수행한다
    # 왼쪽 배열과 오른쪽 배열을 결합한다

    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    less = []
    greater = []
    equal = []

    for item in arr:
        if item > pivot:
            greater.append(item)
        elif item < pivot:
            less.append(item)
        else:
            equal.append(item)

    return quick_sort(less) + equal + quick_sort(greater)


arr1 = [7, 2, 9, 1, 5, 8, 3, 6, 4]
arr2 = [3, 8, 1, 6, 4, 9, 2, 7, 5]
arr3 = [5, 1, 6, 9, 2, 4, 8, 3, 7]

print(quick_sort(arr1))
print(quick_sort(arr2))
print(quick_sort(arr3))
