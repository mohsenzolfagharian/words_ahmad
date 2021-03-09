import sqlite3


def create_db(name):
    conn = sqlite3.connect(f'{name}.db')
    conn.close()


def create_table(table_name, col_name, col_type):
    conn = sqlite3.connect('WORDS.db')
    cursor = conn.cursor()
    cursor.execute(f""" CREATE TABLE '{table_name}'(
                        '{col_name}' '{col_type}')""")
    conn.commit()
    conn.close()


