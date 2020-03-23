import math

documents = ['Технология WPF (Windows Presentation Foundation) является часть экосистемы платформы .NET и представляет собой подсистему для построения графических интерфейсов.',
             'Если при создании традиционных приложений на основе WinForms за отрисовку элементов управления и графики отвечали такие части ОС Windows, как User32 и GDI+, то приложения WPF основаны на DirectX.',
             'В этом состоит ключевая особенность рендеринга графики в WPF: используя WPF, значительная часть работы по отрисовке графики, как простейших кнопочек, так и сложных 3D-моделей, ложиться на графический процессор на видеокарте, что также позволяет воспользоваться аппаратным ускорением графики.',
             'Каждый нейрон - это вычислительная единица, принимающая числовые значения от входных связей, умножающая их на соответствующие им веса.',
             'Одной из важных особенностей является использование языка декларативной разметки интерфейса XAML, основанного на XML: вы можете создавать насыщенный графический интерфейс, используя или декларативное объявление интерфейса, или код на управляемых языках C# и VB.NET, либо совмещать и то, и другое.',
             ]

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
