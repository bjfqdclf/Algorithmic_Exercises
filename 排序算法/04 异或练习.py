"""
（1）有一组数，只有一个数重复次数为奇数次，剩下数出现次数为偶数次，找到出现奇数次的数
（2）有一组数，只有两个数重复次数为奇数次，剩下数出现次数为偶数次，找到这两个出现奇数次的数
    重点：0 ^ 自己 = 自己
         自己 ^ 自己 = 0

         取出一个数最右侧的1：  eor & (~eor + 1)
"""


def func1(arr):
    """
    题目1
    :param arr:
    :return: 出现奇数次的数
    """
    eor = 0
    for i in arr:
        eor ^= i
    return eor


def func2(arr):
    """
    题目2
    :param arr:
    :return: 两个出现奇数次的数
    """
    eor = 0  # r1^r2
    eor_one = 0  # 第一个结果
    for i in arr:
        eor ^= i

    right_one = eor & (~eor + 1)  # 取出最右侧的1，一个结果最右则该位有1，另一个结果最右则该位没有有1

    for i in arr:
        if i & right_one == 0:  # 将第一个结果与第二个结果分为两类（某一位上是1的和不是1的）
            eor_one ^=

    eor_other = eor ^ eor_one  # 取到另一个数
    return eor_one, eor_other


if __name__ == '__main__':
    a1 = [1, 5, 1, 5, 1, 54, 8, 8, 1, 5, 5]
    a2 = [1, 5, 1, 5, 1, 54, 54, 8, 8, 1, 5, 5, 5, 7, 7, 66]
    # r1 = func1(a1)
    # print(r1)
    r2 = func2(a2)
    print(r2)
