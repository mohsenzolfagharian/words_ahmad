import sqlite3

data_base_col = ['number', 'word']


def add_info(db_name, table_name, col_name, number, word):
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO '{table_name}'('{col_name[0]}', '{col_name[1]}') VALUES('{number}', '{word}') """)
    conn.commit()
    conn.close()


# search with condition
def show_info(db_name, table_name, col_name, word):
    words_list = []
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM '{table_name}' WHERE {col_name} = '{word}' """)
    data = cursor.fetchall()
    for data in data:
        # just showing the word
        words_list.append(data[1])
    conn.commit()
    conn.close()
    return words_list


# simple search
def show_all_info(db_name, table_name):
    words_list = []
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM '{table_name}' """)
    data = cursor.fetchall()
    for data in data:
        # just showing the word
        words_list.append(data[1])
    conn.commit()
    conn.close()
    return words_list


# add_info('WORDS', 'pre', data_base_col, 1, 'می')
# show_info('WORDS', 'verbs', 'word', 'دویدن')

def pre_verb(pre, verbs):
    words = []
    for x in pre:
        for y in verbs:
            words.append(x+y)
    return words


pre = show_all_info('WORDS', 'pre')
verbs = show_all_info('WORDS', 'verbs')
print(pre)
print(verbs)
print(pre_verb(pre, verbs))


