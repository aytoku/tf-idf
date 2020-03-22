import math

arr = """
Статическое свойство TextProperty является свойством зависимостей, представляя объект System.Windows.DependencyProperty.
По соглашениям по именованию все свойства зависимостей представляют статические публичные поля (public static) с суффиксом Property.
""".split("\n")[1:-1]

A = arr[0].lower().split()
B = arr[1].lower().split()

word_set = set(A).union(set(B))

word_dict_A = dict.fromkeys(word_set, 0)
word_dict_B = dict.fromkeys(word_set, 0)

for word in A:
    word_dict_A[word] += 1

for word in B:
    word_dict_B[word] += 1


def compute_tf(word_dict, l):
    tf = {}
    sum_nk = len(l)
    for word, count in word_dict.items():
        tf[word] = count / sum_nk
    return tf


tf_A = compute_tf(word_dict_A, A)
tf_B = compute_tf(word_dict_B, B)


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


idf = compute_idf([word_dict_A, word_dict_B])


def compute_tf_idf(tf, idf):
    tf_idf = dict.fromkeys(tf.keys(), 0)
    for word, v in tf.items():
        tf_idf[word] = v * idf[word]
    return tf_idf


tf_idf_A = compute_tf_idf(tf_A, idf)
tf_idf_B = compute_tf_idf(tf_B, idf)
print(tf_idf_A)
print(tf_idf_B)