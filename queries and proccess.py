import sqlite3

# set a list of columns in table
table_words_col = ['pre', 'verb', 'post']


def add_pre(db_name, table_name, word):
    # just add pre
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO '{table_name}'('pre') VALUES('{word}') """)
    conn.commit()
    conn.close()


def add_post(db_name, table_name, word):
    # just add post
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO '{table_name}'('post') VALUES('{word}') """)
    conn.commit()
    conn.close()


def add_verb(db_name, table_name, word):
    # just add verbs
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO '{table_name}'('verb') VALUES('{word}') """)
    conn.commit()
    conn.close()


def add_all_info(db_name, table_name, col_name, words):
    # add data to all columns in a command
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
    # all data in a list with 3 block tuples in it
    # structure [(post, verb, pre), (post, verb, pre), ..., (post, verb, pre)]
    words_list = []
    conn = sqlite3.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM {table_name} """)
    data = cursor.fetchall()
    for data in data:
        # just showing the word
        words_list.append(data)
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


# add data with command below
# add_all_info('final', 'words', table_words_col, ['', '', ''])

# how to call data
verbs = show_info('final', 'words', 'verb')
pre = show_info('final', 'words', 'pre')
post = show_info('final', 'words', 'post')
all_data = show_all_info('final', 'words')
# how to use functions to mix data
mix = verb_post(verbs, post)
mix2 = pre_verb(pre, verbs)
mix3 = pre_verb_post(pre, verbs, post)

# print data alone
print('verbs :', verbs)
print('pre :', pre)
print('post :', post)
print('all data : ', all_data)
# print mixed data
print(mix)
print(mix2)
print(mix3)
