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
    :param arr:
    :return:
    """
    if arr is None or len(arr) < 2:  # arr小于2长度时不排序
        return arr
    for i in reversed(range(len(arr)-1)):
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
    :param arr:
    :return: arr
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
>（2）有一组数，只有两个数重复次数为奇数次，剩下数出现次数为偶数次，找到这两个出现奇数次的数

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
		"""
		eor = r1 ^ r2
		eor != 0
		eor必有一个位置上是1
		"""
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

## 1.4 插入排序

> 从第二位开始，该数比左侧小交换位置，直到该数比左侧大
>
> 时间复杂度：O(n^2)
>
> 空间复杂度：O(1)

`reversed()  反转排序函数`

```python
def inser_sort(arr):
    """
    :param arr:
    :return: arr
    """
    for i in range(1, len(arr) + 1):
        for j in reversed(range(1, i)):  # reversed()  反转排序函数
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
```

## 1.5 二分法

> 时间复杂度：O(log2(N))
>
> 空间复杂度：O(1)

```
1）在一个有序数组看某个数是否存在
2）在一个有序数组中找到<=某个数最左侧位置
3）局部最小问题
    在一个无需数组中，任何两个相邻的数不相等
```

```python
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
```

## 1.6 对数器

对数器概念和使用：<br>
    1）有一个要测的方法a<br>
    2）实现复杂度不好但是容易实现的方法b<br>
    3）实现一个随机样本产生器<br>
    4）把方法a和方法b跑相同的随机样本，看看得到的结果是否一样<br>
    5）如果有一个随机样本使得对比结果不一致，打印样本进行人工干预，改对方法a或者方法b<br>
    6）当样本数量很多时比对测试依然正确，可以确定方法a已经正确<br>

`random.randrange(下限,上限,步长)`

```python
import random


def random_number_list(max_size, max_value):
    """
    生成随机数列
    random.random()             [0,1)所有小数，等概率返回一个
    random.random() * N         [0,N)所有小数，等概率返回一个
    int(random.random() * N)    [0,N-1]所有整数，等概率返回一个

    random.randrange(下限,上限,步长)

    :param max_size: 最大长度
    :param max_value: 最大值
    :return: arr
    """
    arr=[]
    len = random.randrange(1,max_size)  # 长度随机
    for i in range(len):
        arr.append(random.randrange(0, max_value))
    return arr
```

