def sort(arr, num, l, r, min):
    min = int((r - l) / 2 + l)
    if num == arr[min]:
        return min
    if arr[min] < min:
        r = min
        return sort(arr, num, l, r, min)
    else:
        l = min
        return sort(arr, num, l, r, min)


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 7, 9, 45, 155]
    result = sort(list, 45, 0, len(list), len(list) / 2)
    print(result)
