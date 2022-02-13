import sqlite3


def nagruzka():
    res_list = []
    with open("нагрузки.txt", 'r', encoding='utf-8') as f:
        with sqlite3.connect("server_db.db") as my_data:
            sql = my_data.cursor()
            for i in f.readlines():
                if i.strip().split()[1] == '0':
                    res_list.append(0)
                elif len(i.strip().split()[1:]) == 1 and i.strip().split()[1].endswith('n') == False:
                    sql.execute(f"SELECT s FROM trans2 WHERE mark_trans = '{i.strip().split()[1]}'")
                    res_list.append(sql.fetchone()[0])
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

        for i in range(len(res_list)):
            if isinstance(res_list[i], str):
                new_number = complex(float(res_list[i]) * 0.8, 80)
                res_list[i] = new_number
            else:
                continue

    return res_list


def main():
    print(nagruzka())


if __name__ == "__main__":
    main()
