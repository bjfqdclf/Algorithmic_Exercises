"""
归并排序：
    左侧排序，右侧排序，整体排序
时间复杂度：
       T(N)=2*T(N/2)+O(N)
    => a = 2   b = 2   d = 1
    =>O(N*logN)
"""


def process(arr, l, r):
    if l == r:  # 当左右相等
        return

    mid = l + ((r - l) >> 1)  # 得到中点

    process(arr, l, mid)
    process(arr, mid + 1, r)
    merge(arr, l, mid, r)


def merge(arr, l, m, r):
    help = []  # 辅助空间:r-l+1个数的空间
    # i = 0  # help的下标指针
    p1 = l
    p2 = m + 1

    while p1 <= m and p2 <= r:  # 都不越界时，谁小拷贝到help里
        if arr[p1] <= arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1

    # 剩下的全拷进help
    while p1 <= m:
        help.append(arr[p1])
        p1 += 1
    while p2 <= r:
        help.append(arr[p2])
        p2 += 1

    for i in range(len(help)):
        arr[l + i] = help[i]


if __name__ == '__main__':
    ar = [2, 5, 4, 6, 8, 88, 7, 1, 21, 45, 66, 78]
    process(ar, 0, len(ar) - 1)
    print(ar)
