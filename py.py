import pandas as pd
import sklearn as sk
import math

# load up our sample sentences
first = 'The car is driven on the road'
second = 'The truck is driven on the highway'
# split so each word have their own string
first = first.split(" ")
second = second.split(" ")
# join them to remove common duplicate words
total = set(first).union(set(second))
# Now lets add a way to count the words using a dictionary key-value pairing for both sentences
wordDictA = dict.fromkeys(total, 0)
wordDictB = dict.fromkeys(total, 0)
for word in first:
    wordDictA[word] += 1

for word in second:
    wordDictB[word] += 1
# put them in a dataframe and then view the result:
pd.DataFrame([wordDictA, wordDictB])
print(pd.DataFrame([wordDictA, wordDictB]))