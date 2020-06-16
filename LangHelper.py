from nltk import word_tokenize
from readWordFile import *
from Cosine import *
from nltk.stem.isri import ISRIStemmer
import os
import math
import csv

directory = r'D:\Work\NLP\word files'
listOfFiles = []
for filename in os.listdir(directory):
    if filename.endswith(".doc") or filename.endswith(".docx"):
        listOfFiles.append(os.path.join(directory, filename))
    else:
        continue

NumberOfFiles = len(listOfFiles)
DocumentsStore = []
print("reading files Started")
for file in listOfFiles:
    fileContent = ReadWordFile(file)
    DocumentsStore.append(fileContent)

print("reading files Ended")
FilesStemsDic = {}
st = ISRIStemmer()
index = 0
AllRoots = []
print("Steming files Started")
for fileContent in DocumentsStore:
    fileStems = []
    for word in word_tokenize(fileContent):
        fileStems.append((st.stem(word)))
    FilesStemsDic[listOfFiles[index]] = fileStems
    index = index + 1

print("Steming files Ended")
index = 0
DistinctStemsList = []
print("building Distinct Stems List started")
for key in FilesStemsDic:
    for stem in FilesStemsDic[key]:
        if stem not in DistinctStemsList:
            DistinctStemsList.append(stem)

print("building Distinct Stems List Ended")
StemFileMatrix = [[0 for i in range(len(FilesStemsDic))] for j in range(len(DistinctStemsList))]
r = 0
for stem in DistinctStemsList:
    f = 0
    for key in FilesStemsDic:
        for fileStem in FilesStemsDic[key]:
            if stem == fileStem:
                StemFileMatrix[r][f] = StemFileMatrix[r][f] + 1
        f = f + 1
    r = r + 1

r = 0
for i in range(len(StemFileMatrix)):
    numbersPow2 = []
    for n in StemFileMatrix[i]:
        numbersPow2.append(n ** 2)

    itemsSum = sum(numbersPow2)
    f = 0
    for n in StemFileMatrix[i]:
        StemFileMatrix[r][f] = n / math.sqrt(itemsSum)
        f = f + 1
    r = r + 1

csvFileData = [["File Name", "File Name", "Similarity"]]
for i in range(NumberOfFiles):
    for j in range(NumberOfFiles):
        col1 = [val[i] for val in StemFileMatrix]
        col2 = [val[j] for val in StemFileMatrix]
        similarityVal = GetCos(col1, col2)
        csvFileData.append([listOfFiles[i], listOfFiles[j], similarityVal])

myFile = open('similarity.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(csvFileData)
