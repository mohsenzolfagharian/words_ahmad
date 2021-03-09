import sqlite3


def add_info(db_name, table_name, col_name, word):
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO '{table_name}'('{col_name}') VALUES('{word}') """)
    conn.commit()
    conn.close()


def show_info(db_name, table_name, col_name, word):
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM '{table_name}' WHERE {col_name} = '{word}' """)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    print(data)
# add_info("WORDS", "people", "name", "abbas")


# show_info('WORDS', 'people', 'name', 'abbas')

