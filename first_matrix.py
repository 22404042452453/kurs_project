import numpy as np

def first_matrix(model):
    start, end = [int(i.split('-')[0]) for i in model], [int(i.split('-')[1]) for i in model]
    M = np.zeros(shape=[max(end), max(start)])
    try:
        for i in range(len(start)):
            M[start[i]-1,i] = 1
            M[end[i]-1, i] = -1

        M = M[1:, :].astype(np.int32)

        return np.linalg.inv(M)
    except Exception as ex:

        return "Something_wrong"

def main():
    model = input().split()
    print(first_matrix(model))

if __name__ == '__main__':
    main()


