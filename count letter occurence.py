from collections import defaultdict
def word_counts(sentense) :
    fsentence=sentense.lower().strip(".,?!")
    word_dic={}
    for word in fsentence.replace(" ",""):
        word_dic[word]=word_dic.get(word,0)
    print(word_dic)

sentence=input("enter your sentence\n")
word_counts(sentence)

