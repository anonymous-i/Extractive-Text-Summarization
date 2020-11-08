from nltk.tokenize import word_tokenize
import nltk
class SentenceScoring:
    def __init__(self):
        self.sentenceScore = dict()
        self.tfidf=0

    def calculateScore(self,tkn,pre):
        for sentence in tkn.sentences:
            sentence_wordcount = (len(word_tokenize(sentence)))
            for word_weight in pre.frequency_table:
                if word_weight in sentence.lower():
                    self.tfidf += 1
                    if sentence in self.sentenceScore:
                        self.sentenceScore[sentence] += pre.frequency_table[word_weight]
                    else:
                        self.sentenceScore[sentence] = pre.frequency_table[word_weight]
                        self.sentenceScore[sentence] = int(self.sentenceScore[sentence] / self.tfidf)
        ncount =0
        sncount =0
        for sentence in tkn.sentences:
            word= word_tokenize(sentence)
            pos = nltk.pos_tag(word)
            pdict = dict(pos)
            for key in pdict:
                if (pdict[key] == "NNP" or pdict[key] == "NNPS"):
                    ncount = ncount + 1
        
        for sentence in tkn.sentences:
            word= word_tokenize(sentence)
            pos = nltk.pos_tag(word)
            pdict = dict(pos)
            for key in pdict:
                if (pdict[key] == "NNP" or pdict[key] == "NNPS"):
                    sncount = sncount+1
            self.sentenceScore[sentence] += int(sncount/ncount)
                    
                    
    def returnScore(self)->dict:
        return self.sentenceScore
        
        
        
