"""
对数器概念和使用：
    1）有一个要测的方法a
    2）实现复杂度不好但是容易实现的方法b
    3）实现一个随机样本产生器
    4）把方法a和方法b跑相同的随机样本，看看得到的结果是否一样
    5）如果有一个随机样本使得对比结果不一致，打印样本进行人工干预，改对方法a或者方法b
    6）当样本数量很多时比对测试依然正确，可以确定方法a已经正确
"""
import random


def random_number_list(max_size, max_value):
    """
    生成随机数列
    random.random()             [0,1)所有小数，等概率返回一个
    random.random() * N         [0,N)所有小数，等概率返回一个
    int(random.random() * N)    [0,N-1]所有整数，等概率返回一个

    random.randrange(下限，上限，步长)

    :param max_size: 最大长度
    :param max_value: 最大值
    :return: arr
    """
    arr=[]
    len = random.randrange(1,max_size)  # 长度随机
    for i in range(len):
        arr.append(random.randrange(0, max_value))
    return arr


if __name__ == '__main__':
    print(random_number_list(50, 55))
