def select_sort(arr):
    """
    依次找最小值的位置，与当前位置交换
    时间复杂度：n^2
    空间复杂度：1
    :param arr:
    :return:
    """
    if arr is False or len(arr) < 2:  # arr小于2长度时不排序
        return arr
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            min_index = j if arr[j] < arr[min_index] else min_index
            # if arr[j] < arr[min_index]:
            #     min_index = j
        swap(arr, i, min_index)
    return arr


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


if __name__ == '__main__':
    ar = [2, 5, 4, 8, 6, 4, 8, 7, 6, 4, 8, 12, 54]
    ar = select_sort(ar)
    print(ar)
