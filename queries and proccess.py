import sqlite3

data_base_col = ['pre', 'verb', 'post']


def add_pre(db_name, table_name, word):
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO '{table_name}'('pre') VALUES('{word}') """)
    conn.commit()
    conn.close()


def add_post(db_name, table_name, word):
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO '{table_name}'('post') VALUES('{word}') """)
    conn.commit()
    conn.close()


def add_verb(db_name, table_name, word):
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO '{table_name}'('verb') VALUES('{word}') """)
    conn.commit()
    conn.close()


def add_all_info(db_name, table_name, col_name, words):
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO '{table_name}'('{col_name[0]}', '{col_name[1]}','{col_name[2]}') VALUES('{words[0]}',
                    '{words[1]}', '{words[2]}') """)
    conn.commit()
    conn.close()


# search with condition
def show_info(db_name, table_name, col_name):
    words_list = []
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT {col_name}
                   FROM {table_name}
                    """)
    data = cursor.fetchall()
    for data in data:
        # just showing the word
        words_list.append(data[0])
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
        words_list.append(data[0])
    conn.commit()
    conn.close()
    return words_list


def pre_verb(pre, verbs):
    words = []
    for x in pre:
        for y in verbs:
            words.append(x+y)
    return words


def verb_post(verb, post):
    words = []
    for x in verb:
        for y in post:
            word = x+y
            words.append(word)
    return words


def pre_verb_post(pre, verb, post):
    words = []
    for x in pre:
        for y in verb:
            for z in post:
                word = x+y+z
                words.append(word)

    return words


verbs = show_info('final', 'words', 'verb')
pre = show_info('final', 'words', 'pre')
post = show_info('final', 'words', 'post')


mix = verb_post(verbs, post)
mix2 = pre_verb(pre, verbs)
mix3 = pre_verb_post(pre, verbs, post)
print('verbs :', verbs)
print('pre :', pre)
print('post :', post)
print(mix)
print(mix2)
print(mix3)
