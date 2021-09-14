"""
满足子问题等规模递归使用master公式：
       T(N)   =   a     *     T(N/b)  +    O(N^d)
    母问题规模  子过程调用次数   子过程规模    剩下时间复杂度

    logb(a) < d     O(N^d)
    logb(a) > d     O(N^(logb(a)))
    logb(a) = d     O(N^d*log(N))
"""
def process(arr, l, r):
    """
    通过递归得到数组最大值

    master计算时间复杂度：
        T(N)=2*T(N/2)+O(1)
        => a = 2   b = 2   d = 0
        => log2(2) > 1
        => O(1)
    :param arr:
    :param l:
    :param r:
    :return: 最大值
    """
    if l == r:  # 当左右相等
        return arr[l]

    mid = l + ((r - l) >> 1)  # 得到中点
    """
    通过位操作除2： num >> 1
    求中点：
           mid = (L + R) / 2
              => L + (R - L) / 2
              => L + (R - L ) >> 1
    """
    left_max = process(arr, l, mid)
    right_max = process(arr, mid + 1, r)
    return max(left_max, right_max)


if __name__ == '__main__':
    ar = [2, 5, 4, 6, 8, 88, 7, 1, 21, 45, 66, 78]
    max = process(ar, 0, len(ar) - 1)
    print(max)
