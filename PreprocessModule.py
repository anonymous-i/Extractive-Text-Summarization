from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

'''
Class for preprocessing the data
'''
class Preprocess:
    
    def __init__(self):
        self.frequency_table = dict()
        self.symbols =['\n',' ','!']
    
    def filterDocument(self,tkn)->dict:
        stopWords = set(stopwords.words("english"))
        rootWords = PorterStemmer()
        for wd in tkn.words:
            wd = rootWords.stem(wd)
            if wd in stopWords or wd in self.symbols:
                continue
            if wd in self.frequency_table:
                self.frequency_table[wd] += 1
            else:
                self.frequency_table[wd] = 1
        return self.frequency_table
'''
Class for tokenizing the data
'''
class TokenizeSentences:
    def __init__(self,inputData):
        self.inputData = inputData
        self.words =list()
        self.sentences=list()
    def getTokens(self):
        self.sentences = sent_tokenize(self.inputData)
        
    def tokenizeWords(self,sentence):
        self.words = word_tokenize(sentence)
        
    
