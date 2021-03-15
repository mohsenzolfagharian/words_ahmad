import sqlite3


def create_db(name):
    conn = sqlite3.connect(f'{name}.db')
    conn.close()


def create_table(name_db, table_name, col_name, col_type):
    conn = sqlite3.connect(f'{name_db}.db')
    cursor = conn.cursor()
    cursor.execute(f""" CREATE TABLE '{table_name}'(
                        '{col_name[0]}' '{col_type[0]}',
                        '{col_name[1]}' '{col_type[1]}',
                        '{col_name[2]}' '{col_type[2]}')""")
    conn.commit()
    conn.close()


create_db('final')
create_table('final', 'words', ['pre', 'verb', 'post'], ['text', 'text', 'text'])
# create_table('WORDS', 'verbs', ['number', 'word'], ['INT', 'TEXT'])

