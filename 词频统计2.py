

from nltk.corpus import PlaintextCorpusReader
from nltk import word_tokenize
from nltk import Text
from nltk import FreqDist

corpus_root = ''
files = PlaintextCorpusReader(corpus_root,'.*\.txt')
files.fileids()
words = word_tokenize(files.raw(fileids=files.fileids()))
cps1 = Text(words)

fdist1 = FreqDist(cps1)
wordlist = fdist1.items()
wordlist_sorted_desc = sorted(wordlist, key=lambda w:w[1], reverse=True)
wordlist_sorted_asc = sorted(wordlist, key=lambda w:w[1])



for word in wordlist_sorted_desc[0:10]:
    print(word)
for word in wordlist_sorted_asc[0:10]:
    print(word)
