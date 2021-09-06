def inser_sort(arr):
    """
    从第二位开始，该数比左侧小交换位置，直到该数比左侧大
    :param arr:
    :return: arr
    """
    for i in range(1, len(arr)+1):
        for j in reversed(range(1,i)):  # reversed()  反转排序函数
            if arr[j] > arr[j - 1]:
                break
            swap(arr, j, j - 1)
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
    ar = [5, 2, 5, 4, 8, 6, 4, 8, 7, 6, 4, 8, 12, 54, 11]
    ar = inser_sort(ar)
    print(ar)
