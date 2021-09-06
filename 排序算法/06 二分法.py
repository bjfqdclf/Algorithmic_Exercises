"""
1）在一个有序数组看某个数是否存在
2）在一个有序数组中找到<=某个数最左侧位置
3）局部最小问题
    在一个无需数组中，任何两个相邻的数不相等
"""


def dichotomy_sort(arr, num):
    """
    二分法找一个数
    :param arr: l1
    :param num: 找的数
    :return: 该数的下标
    """
    t = int((len(arr) + 1) / 2)
    left_index = 0
    right_index = len(arr)
    while arr[t] != num:
        if arr[t] > num:
            right_index = t
            t = int((right_index + left_index) / 2)
        else:
            left_index = t
            t = int((right_index + left_index) / 2)
    return t


def left_dichotomy_sort(arr, num):
    """
    二分法找<=某个数最左侧位置
    :param arr: l1
    :param num: 找的数
    :return: 该数的下标
    """
    t = int((len(arr) + 1) / 2)
    left_index = 0
    right_index = len(arr)
    while arr[t] != num:  # 先找到这个数
        if arr[t] < num:
            left_index = t
            t = int((right_index + left_index) / 2)
        else:
            right_index = t
            t = int((right_index + left_index) / 2)

    while int((right_index - left_index) / 2) != 0:  # 找到最左侧的这个数的
        if arr[t] == num:
            right_index = t
            t = int((right_index + left_index) / 2)
        else:
            left_index = t
            t = int((right_index + left_index) / 2)

    if arr[t] == num:
        return t
    else:
        return t + 1


def local_minimum(arr):
    """
    求一个局部最小值
    :param arr: l3
    :return: result
    """
    if arr[0] < arr[1]:
        return arr[0]
    if arr[-1] < arr[-2]:
        return arr[len(arr)]
    t = int((len(arr) + 1) / 2)  # 找到中点
    while arr[t] > arr[t - 1]:
        t = int((t + 1) / 2)  # 找到中点

    return arr[t]


if __name__ == '__main__':
    l1 = [1, 2, 3, 3, 5, 8, 9, 12, 12, 12, 14, 19, 25, 46, 87, 101, 155]
    l3 = [4, 3, 2, 4, 9, 7, 9, 48, 4, 2, 4, 5]
    # r1 = dichotomy_sort(l1, 2)
    # print(r1)
    r2 = left_dichotomy_sort(l1, 3)
    print(r2)
    # r3 = local_minimum(l3)
    # print(r3)
