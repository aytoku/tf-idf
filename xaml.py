import math

arr = """
XAML (eXtensible Application Markup Language) - язык разметки, используемый для инициализации объектов в технологиях на платформе .NET. Применительно к WPF (а также к Silverlight) данный язык используется прежде всего для создания пользовательского интерфейса декларативным путем. Хотя функциональность XAML только графическими интерфейсами не ограничивается: данный язык также используется в технологиях WCF и WF, где он никак не связан с графическим интерфейсом. То есть его область шире. Применительно к WPF мы будем говорить о нем чаще всего именно как о языке разметки, который позволяет создавать декларативным путем интерфейс, наподобие HTML в веб-программировании. Однако опять же повторюсь, сводить XAML к одному интерфейсу было бы неправильно, и далее на примерах мы это увидим.
XAML - не является обязательной частью приложения, мы вобще можем обходиться без него, создавая все элементы в файле связанного с ним кода на языке C#. Однако использование XAML все-таки несет некоторые преимущества:
Возможность отделить графический интерфейс от логики приложения, благодаря чему над разными частями приложения могут относительно автономно работать разные специалисты: над интерфейсом - дизайнеры, над кодом логики - программисты.
Компактность, понятность, код на XAML относительно легко поддерживать.
При компиляции приложения в Visual Studio код в xaml-файлах также компилируется в бинарное представление кода xaml, которое называется BAML (Binary Application Markup Language). И затем код baml встраивается в финальную сборку приложения - exe или dll-файл.
""".split("\n")[1:-1]

A = arr[0].lower().split()
B = arr[1].lower().split()
C = arr[2].lower().split()
D = arr[3].lower().split()
E = arr[4].lower().split()

word_set = set(A).union(set(B)).union(set(C)).union(set(D)).union(set(E))

word_dict_A = dict.fromkeys(word_set, 0)
word_dict_B = dict.fromkeys(word_set, 0)
word_dict_C = dict.fromkeys(word_set, 0)
word_dict_D = dict.fromkeys(word_set, 0)
word_dict_E = dict.fromkeys(word_set, 0)

for word in A:
    word_dict_A[word] += 1

for word in B:
    word_dict_B[word] += 1

for word in C:
    word_dict_C[word] += 1

for word in D:
    word_dict_D[word] += 1
for word in E:
    word_dict_E[word] += 1


def compute_tf(word_dict, l):
    tf = {}
    sum_nk = len(l)
    for word, count in word_dict.items():
        tf[word] = count / sum_nk
    return tf


tf_A = compute_tf(word_dict_A, A)
tf_B = compute_tf(word_dict_B, B)
tf_C = compute_tf(word_dict_C, C)
tf_D = compute_tf(word_dict_D, D)
tf_E = compute_tf(word_dict_E, E)


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


idf = compute_idf([word_dict_A, word_dict_B, word_dict_C, word_dict_D, word_dict_E])


def compute_tf_idf(tf, idf):
    tf_idf = dict.fromkeys(tf.keys(), 0)
    for word, v in tf.items():
        tf_idf[word] = v * idf[word]
    return tf_idf


tf_idf_A = compute_tf_idf(tf_A, idf)
tf_idf_B = compute_tf_idf(tf_B, idf)
tf_idf_C = compute_tf_idf(tf_C, idf)
tf_idf_D = compute_tf_idf(tf_D, idf)
tf_idf_E = compute_tf_idf(tf_E, idf)
print(tf_idf_A)
print(tf_idf_B)
print(tf_idf_C)
print(tf_idf_D)
print(tf_idf_E)