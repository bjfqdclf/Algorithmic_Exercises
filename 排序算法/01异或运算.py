def swap(a, b):
    """
    使用异或交换a,b的值
    异或：
        相同为0，不同为1
        不进位的加法
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
