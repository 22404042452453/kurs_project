import sqlite3

### Create_table
with sqlite3.connect("server_db.db") as my_data:
    sql = my_data.cursor()
    sql.execute("""CREATE TABLE  IF NOT EXISTS provod(
                mark_provod TEXT,
                r0  TEXT,
                x0  TEXT)""")
    my_data.commit()



