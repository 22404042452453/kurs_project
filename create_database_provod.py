import pandas as pd
import sqlite3

### Create_table
with sqlite3.connect("server_db.db") as my_data:
    sql = my_data.cursor()
    sql.execute("""CREATE TABLE  IF NOT EXISTS provod(
                mark_provod TEXT,
                r0  TEXT,
                x0  TEXT)""")
    my_data.commit()


###download_information
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
