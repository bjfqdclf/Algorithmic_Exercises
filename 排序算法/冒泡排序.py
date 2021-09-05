def bubble_sort(arr):
    if arr is None or len(arr) < 2:  # arr小于2长度时不排序
        return arr
    for i in range(len(arr)-1):
        i=len(arr)-i-1
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
    return arr


def swap(arr, i, j):
    """
    交换i与j位置上的值
    :param arr:
    :param i:
    :param j:
    :return:
    """
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]


if __name__ == '__main__':
    ar = [2, 5, 4, 8, 6, 4, 8, 7, 6, 4, 8, 12, 54]
    ar = bubble_sort(ar)
    print(ar)
