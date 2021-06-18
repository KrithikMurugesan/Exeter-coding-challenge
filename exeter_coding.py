import csv

import re

d={}
def csvToDictionary():
    reader = csv.reader(open('french_dictionary.csv', 'r'))
    d = {}
    for row in reader:
       k, v = row
       d[k] = v

    return d
    

def textToList():
    my_file = open("find_words.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    '''    for i in content_list:
        if i not in d.keys():
            content_list.remove(i)
    my_file.close()'''
    return content_list


def inputfile():
    my_file = open("t8.shakespeare.txt", "r")
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
            if(n>0):
                entry.append(word)
                entry.append(csvDict[word])
                entry.append(n)
                writer.writerow(entry)
                inputFile=re.sub((word.lower()),( csvDict[word].lower()),inputFile)
                inputFile=re.sub((word.upper()), (csvDict[word].upper()),inputFile)
                inputFile=re.sub((word[0].upper()), (csvDict[word][0].upper()),inputFile)

                
    resultFile = open("t8.shakespeare.translated.txt", "w")
    resultFile.write(inputFile)
