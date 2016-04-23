from __future__ import division
import sys
import re
import nltk, re, pprint
from nltk import word_tokenize
from bs4 import BeautifulSoup

filename = sys.argv[-1]
file_pointer=open(filename , 'r')
file_in_memory=file_pointer.read().decode('utf-8')
file_in_memory=file_in_memory.lower()
raw=BeautifulSoup(file_in_memory,"lxml").get_text()
tokens=word_tokenize(raw)
file_pointer.close()
write_file_pointer=open(filename,'w')
tokens=' '.join(tokens).encode('utf-8')
write_file_pointer.write(tokens)
write_file_pointer.close()

