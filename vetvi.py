import sqlite3
import numpy as np


def vetvi():
    R = []
    X = []
    with open("линии.txt", 'r', encoding="utf-8") as f:
        with sqlite3.connect("server_db.db") as my_data:
            sql = my_data.cursor()
            for i in f.readlines():
                sql.execute(f"SELECT r0,x0 FROM provod WHERE mark_provod = '{i.strip().split()[1]}'")
                if sql.fetchone() is None:
                    sql.execute(f"SELECT rt,xt FROM trans2 WHERE mark_trans = '{i.strip().split()[1]}'")
                    r, x = map(float, sql.fetchall()[0])
                    R.append(r)
                    X.append(x)
                else:
                    sql.execute(f"SELECT r0,x0 FROM provod WHERE mark_provod = '{i.strip().split()[1]}'")
                    r, x = map(float, sql.fetchall()[0])
                    length = float(i.strip().split()[2])
                    R.append(r * length)
                    X.append(x * length)

    Z = np.zeros(shape=(len(R), len(X))).astype(complex)
    np.fill_diagonal(Z, [complex(R[i], X[i]) for i in range(len(X))])

    return Z


def main():
    print(vetvi())


if __name__ == "__main__":
    main()
