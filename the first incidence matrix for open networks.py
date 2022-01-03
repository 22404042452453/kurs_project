import numpy as np

def first_matrix(model):
    z = np.eye(len(model), dtype=np.int64) * -1
    start, end = [int(i.split('-')[0]) for i in model], [int(i.split('-')[1]) for i in model]
    try:
        for i in range(len(start) - 1):
            if start[i] != 0 and end[i - 1] == start[i]:
                for j in end[i - 1:]:
                    z[i - 1, j - 1] = -1
            elif start[i] != 0:
                z[start[i] - 1, end[i] - 1] = -1
            else:
                continue

        return z

    except Exception as ex:

        return 'Something_wrong'

def main():
    model = input('Введите свою сеть по узлам:').split()
    print(first_matrix(model))

if __name__ == '__main__':
    main()
