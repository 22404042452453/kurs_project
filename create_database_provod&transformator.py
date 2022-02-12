import pandas as pd
import sqlite3

### Create_table provod
with sqlite3.connect("server_db.db") as my_data:
    sql = my_data.cursor()
    sql.execute("""CREATE TABLE  IF NOT EXISTS provod(
                mark_provod TEXT,
                r0  TEXT,
                x0  TEXT)""")
    my_data.commit()


### Create_table transformator
with sqlite3.connect("server_db.db") as my_data:
    sql = my_data.cursor()
    sql.execute("""CREATE TABLE  IF NOT EXISTS trans2(
                mark_trans TEXT,
                rt  TEXT,
                xt  TEXT,
                pxx TEXT,
                qxx TEXT,
                s  TEXT)""")
    my_data.commit()



###download_information_to_provod
with sqlite3.connect("server_db.db") as my_data:
    sql = my_data.cursor()
    df = pd.read_excel("провода.xlsx")
    for i in range(len(df["mark"])):
        sql.execute(f"SELECT mark_provod FROM provod WHERE mark_provod = '{df['mark'][i]}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO provod VALUES(?,?,?)", (df["mark"][i], df["r0"][i], df["x0"][i]))
            my_data.commit()
        else:
            print("Этот провод уже имеется")


###download_information_to_transformator
with sqlite3.connect("server_db.db") as my_data:
    sql = my_data.cursor()
    df = pd.read_excel("трансформаторы.xlsx")
    for i in range(len(df["mark_trans"])):
        sql.execute(f"SELECT mark_trans FROM trans2 WHERE mark_trans = '{df['mark_trans'][i]}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO trans2 VALUES(?,?,?,?,?,?)", (df["mark_trans"][i], df["r0"][i], df["x0"][i],df["pxx"][i],
                                                                  df["qxx"][i],df["s"][i]))

            my_data.commit()
        else:
            print("Этот трансформатор уже имеется")


"""
with sqlite3.connect("server_db.db") as my_data:
    sql = my_data.cursor()
    sql.execute("DROP TABLE IF EXISTS trans")
    my_data.commit()
"""