import math

documents = ['Гипотеза – предположение; тезис, предполагающий доказательство.',
             'Гуманитарные науки – группа научных дисциплин, направленных на изучение человека и его деятельности.',
             'Концепция – предтеория; совокупность обоснованных суждений о предмете (событии, явлении).',
             'Методика – группа исследовательских методов и приемов, связанных общей целью применения (например: методика анализа статистических источников).',
             'Методология – учение о принципах, методах и средствах познания.',
             'Научная теория – высшая форма систематизации знания; система знаний, описывающая и объясняющая определённую совокупность явлений.',
             'Общественные науки – группа научных дисциплин, направленных на всестороннее изучение социума (общества).']

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
