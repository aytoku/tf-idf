import math

n = int(input())
arr = [input() for i in range(n)]

letter = [arr[i].lower().split() for i in range(n)]
word_set = {}
for i in range(n):
    word_set = set(word_set).union(set(letter[i]))

word_dict_arr = [dict.fromkeys(word_set, 0) for i in range(n)]
for i in range(n):
    for word in letter[i]:
        word_dict_arr[i][word] += 1


def compute_tf(word_dict, l):
    tf = {}
    sum_nk = len(l)
    for word, count in word_dict.items():
        tf[word] = count / sum_nk
    return tf


tf_arr = [compute_tf(word_dict_arr[i], arr[i].lower().split()) for i in range(n)]


def compute_idf(strings_list):
    n = len(strings_list)
    idf = dict.fromkeys(strings_list[0].keys(), 0)
    for l in strings_list:
        for word, count in l.items():
            if count > 0:
                idf[word] += 1

    for word, v in idf.items():
        idf[word] = math.log(n / float(v), math.e)
    return idf


idf = compute_idf(word_dict_arr)


def compute_tf_idf(tf, idf):
    tf_idf = dict.fromkeys(tf.keys(), 0)
    for word, v in tf.items():
        tf_idf[word] = v * idf[word]
    return tf_idf


tf_idf_arr = [compute_tf_idf(tf_arr[i], idf) for i in range(n)]
for i in range(n):
    print(tf_idf_arr[i])