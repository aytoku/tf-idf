import math

documents = ['Данный урок оказался немного оторванным от остального курса, поэтому нужно добавить информации перед его прохождением.',
             'Речь пойдёт об алгоритме для подбора параметров нейронных сетей, так что вкратце обговорим их  устройство, чтобы понимать о чём идёт речь.',
             'Нейронные сети можно представлять как набор нейронов, соединённых связями.',
             'Каждый нейрон - это вычислительная единица, принимающая числовые значения от входных связей, умножающая их на соответствующие им веса.',
             'Затем получившиеся результаты складываются, и к ним применяется активационная функция нейрона.',
             'Результат передаётся по выходным связям.',
             'То есть нейронную сеть можно представить как граф, где вершинами являются нейроны, а рёбрами - связи между ними.',
             'Пространственно нейроны обычно организованы в виде слоёв, и информация (значения переменных во входных данных и результаты вычислений нейронов) передаётся слева направо.',
             'Об одном из способов подбора этих параметров и пойдёт речь.']

#---Calculate term frequency --

#First: tokenize words
dictOfWords = {}

for index, sentence in enumerate(documents):
    tokenizedWords = sentence.split(' ')
    dictOfWords[index] = [(word,tokenizedWords.count(word)) for word in tokenizedWords]

#print(dictOfWords)

#second: remove duplicates
termFrequency = {}

for i in range(0, len(documents)):
    listOfNoDuplicates = []
    for wordFreq in dictOfWords[i]:
        if wordFreq not in listOfNoDuplicates:
            listOfNoDuplicates.append(wordFreq)
        termFrequency[i] = listOfNoDuplicates
#print(termFrequency)

#Third: normalized term frequency
normalizedTermFrequency = {}
for i in range(0, len(documents)):
    sentence = dictOfWords[i]
    lenOfSentence = len(sentence)
    listOfNormalized = []
    for wordFreq in termFrequency[i]:
        normalizedFreq = wordFreq[1]/lenOfSentence
        listOfNormalized.append((wordFreq[0],normalizedFreq))
    normalizedTermFrequency[i] = listOfNormalized

#print(normalizedTermFrequency)


#---Calculate IDF

#First: put al sentences together and tokenze words

allDocuments = ''
for sentence in documents:
    allDocuments += sentence + ' '
allDocumentsTokenized = allDocuments.split(' ')

#print(allDocumentsTokenized)

allDocumentsNoDuplicates = []

for word in allDocumentsTokenized:
    if word not in allDocumentsNoDuplicates:
        allDocumentsNoDuplicates.append(word)


#print(allDocumentsNoDuplicates)

#Second calculate the number of documents where the term t appears

dictOfNumberOfDocumentsWithTermInside = {}

for index, voc in enumerate(allDocumentsNoDuplicates):
    count = 0
    for sentence in documents:
        if voc in sentence:
            count += 1
    dictOfNumberOfDocumentsWithTermInside[index] = (voc, count)

#print(dictOfNumberOfDocumentsWithTermInside)


#calculate IDF

dictOFIDFNoDuplicates = {}


for i in range(0, len(normalizedTermFrequency)):
    listOfIDFCalcs = []
    for word in normalizedTermFrequency[i]:
        for x in range(0, len(dictOfNumberOfDocumentsWithTermInside)):
            if word[0] == dictOfNumberOfDocumentsWithTermInside[x][0]:
                listOfIDFCalcs.append((word[0],math.log(len(documents)/dictOfNumberOfDocumentsWithTermInside[x][1])))
    dictOFIDFNoDuplicates[i] = listOfIDFCalcs

#print(dictOFIDFNoDuplicates)

#Multiply tf by idf for tf-idf

dictOFTF_IDF = {}
for i in range(0,len(normalizedTermFrequency)):
    listOFTF_IDF = []
    TFsentence = normalizedTermFrequency[i]
    IDFsentence = dictOFIDFNoDuplicates[i]
    for x in range(0, len(TFsentence)):
        listOFTF_IDF.append((TFsentence[x][0],TFsentence[x][1]*IDFsentence[x][1]))
    dictOFTF_IDF[i] = listOFTF_IDF

print(dictOFTF_IDF)


def test_tf(term, text):
    newText = text.split(' ')
    print(text.count(term))
    print(len(newText))
