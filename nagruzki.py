import sqlite3
import numpy as np


def nagruzka(name_list, k, cosa, m):
    Unom = 10
    res_list = []
    with open(name_list, 'r', encoding='utf-8') as f:
        with sqlite3.connect("server_db.db") as my_data:
            sql = my_data.cursor()
            for i in f.readlines():
                if i.strip().split()[1] == '0':
                    res_list.append(0)
                elif len(i.strip().split()[1:]) == 1 and i.strip().split()[1].endswith('n') == False:
                    sql.execute(f"SELECT s FROM trans2 WHERE mark_trans = '{i.strip().split()[1]}'")
                    res_list.append(float(sql.fetchone()[0]))
                elif len(i.strip().split()[1:]) == 1 and i.strip().split()[1].endswith('n') == True:
                    sql.execute(f"SELECT pxx,qxx FROM trans2 WHERE mark_trans = '{i.strip().split()[1][:-1]}'")
                    pxx, qxx = map(float, sql.fetchone())
                    res_list.append(complex(pxx, qxx))
                else:
                    my_list = (i.strip().split()[1:])
                    my_list.remove("+")
                    result = 0
                    for i in my_list:
                        sql.execute(f"SELECT pxx,qxx FROM trans2 WHERE mark_trans = '{i}'")
                        pxx, qxx = map(float, sql.fetchone())
                        result += complex(pxx, qxx)
                    res_list.append(result)

    res_list.remove(0)
    #Расчет на комлексную форму
    Icp_max = (sum(res_list) * k) / (Unom * pow(3, 0.5))
    Inb = [(Icp_max * i) / sum(res_list) for i in res_list]
    Pnb = np.array([i * cosa * Unom * pow(3, 0.5) for i in Inb])
    Qnb = np.array([i * (1 - cosa ** 2) ** 0.5 * Unom * pow(3, 0.5) for i in Inb])
    Snb = np.rot90(np.array([[complex(Pnb[i], Qnb[i]) for i in range(len(Pnb))]]), k=-1)
    Snl = Snb * m

    return Snb,Snl


def main():
    name_nagruzka = 'нагрузки.txt'
    print(nagruzka(name_list=name_nagruzka, k=0.65, cosa=0.91, m=0.2))


if __name__ == "__main__":
    main()
