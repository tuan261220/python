import os
import math
def countCharacter(filename):
    d = dict()
    text = open(filename,'r',encoding='utf-8')
    for line in text:
        line = line.strip().lower()
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word] +=1
            else:
                d[word] = 1

    return  d

def combinefile():
    with open('Test3.txt', 'w', encoding='utf-8') as outfile:
        for names in os.listdir():
            if names == 'bai9.py' :
                continue
            else:
                with open(names, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())

                outfile.write("\n")

    return 'Test3.txt'

def calTF(query_dict):
    Maxword = max(query_dict.values())
    for key in query_dict.keys():
        query_dict[key] = float(query_dict[key]/Maxword)

    return query_dict

def calIDF(w):
    idf = dict()
    n = len(w)
    for document in w:
        for key in document.keys():
            if key in idf:
                idf[key] += 1
            else:
                idf[key] = 1
    for key,value in idf.items():
        idf[key] = math.log(n/float(value))

    return idf

def calTFIDF(tf,idf):
    tfidf = dict()
    for key in idf.keys():
        tfidf[key] = tf[key] *idf[key]

    return tfidf

# a = combinefile()
d = countCharacter("test2.txt")
a = countCharacter("test1.txt")
s = calTF(d)
# print(max(d.values()))
# print(d)
print(s)
q = calIDF([d,a])
print(q)
print(calTFIDF(q,s))

