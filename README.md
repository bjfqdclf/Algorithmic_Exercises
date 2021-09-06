# 1 排序算法

## 1.1 冒泡排序

> 从头开始大的数往右边移动，最后一个数先排好
>
> 时间复杂度：O(n^2)
>
> 空间复杂度：O(1)

```python
def bubble_sort(arr):
    """
    从头开始大的数往右边移动，最后一个数先排好
    :param arr:
    :return:
    """
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
```

## 1.2 选择排序

> 依次找最小值的位置，与当前位置交换
>
> 时间复杂度：O(n^2)
>
> 空间复杂度：O(1)

```python
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
```

## 1.3 异或运算

- 相同为0，不同为1
- 不进位的加法

### 1.3.1 使用异或交换两数

```python
def swap(a, b):
    """
    使用异或交换a,b的值
    :param a:
    :param b:
    :return: a,b
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
  

if __name__ == '__main__':
    a = 3
    b = 4
    a, b = swap(a, b)
    print('a:', a, 'b:', b)
```

### 1.3.2 异或练习

> （1）有一组数，只有一个数重复次数为奇数次，剩下数出现次数为偶数次，找到出现奇数次的数
> （2）有一组数，只有两个数重复次数为奇数次，剩下数出现次数为偶数次，找到这两个出现奇数次的数

```python
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
```

**重点： **0 ^ 自己 = 自己
            自己 ^ 自己 = 0

​			取出一个数最右侧的1：  eor & (~eor + 1)

