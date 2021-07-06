

import csv

import re

d={}
def csvToDictionary():
    reader = csv.reader(open('/content/drive/MyDrive/Exeter/french_dictionary.csv', 'r'))
    d = {}
    for row in reader:
       k, v = row
       d[k] = v

    return d
    

def textToList():
    my_file = open("/content/drive/MyDrive/Exeter/find_words.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    return content_list


def inputfile():
    my_file = open("/content/drive/MyDrive/Exeter/t8.shakespeare.txt", "r")
    content = my_file.read()
    my_file.close()
    return content    


if __name__ == "__main__":
    csvDict=csvToDictionary()  
    text=textToList()
    inputFile=inputfile()
    with open('frequency.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        heading=['English word','French word','Frequency']
        writer.writerow(heading)
        for word in text:    
            entry=[]
            n=inputFile.count(word)
            entry.append(word)
            entry.append(csvDict[word])
            entry.append(n)
            writer.writerow(entry)
            if(n>0):
                obj=re.compile((word.lower()))
                inputFile=obj.sub((csvDict[word].lower()),inputFile)
                #inputFile=re.sub((word.lower()),(csvDict[word].lower()),inputFile)
                #inputFile=inputFile.replace((word.lower()),(csvDict[word].lower()))
            n=inputFile.count(word)
            if(n>0):
                obj=re.compile((word.capitalize()))
                inputFile=obj.sub((csvDict[word].capitalize()),inputFile)
                #inputFile=re.sub((word.capitalize()), (csvDict[word].capitalize()),inputFile)
                #inputFile=inputFile.replace((word.capitalize()),(csvDict[word].capitalize()))
                
            n=inputFile.count(word)
            if(n>0):
                obj=re.compile((word.upper()))
                inputFile=obj.sub((csvDict[word].upper()),inputFile)
                #inputFile=re.sub((word.upper()),( csvDict[word].upper()),inputFile)
                #inputFile=inputFile.replace((word.upper()),(csvDict[word].upper()))

            n=inputFile.count(word)
            if(n>0):
                obj=re.compile(word,flags=re.IGNORECASE)
                inputFile=obj.sub((csvDict[word]),inputFile)
                #inputFile=re.sub(word,csvDict[word],inputFile,flags=re.IGNORECASE)


    resultFile = open("t8.shakespeare.translated.txt", "w")
    resultFile.write(inputFile)