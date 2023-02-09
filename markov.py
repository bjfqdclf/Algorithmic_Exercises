import numpy as np


def markov():
    transfer_matrix = np.array([[0.9, 0.075, 0.025],
                                [0.15, 0.8, 0.05],
                                [0.25, 0.25, 0.5]])
    tmp = transfer_matrix
    for i in range(1000):
        res = np.dot(tmp, transfer_matrix)
        print(f'{i}:  {res}')
        tmp = res


if __name__ == '__main__':
    markov()
