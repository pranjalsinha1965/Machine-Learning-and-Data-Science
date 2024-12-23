# for figuring out such things we will be using pos library 
from nltk import pos_tag 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import state_union 
text = state_union.raw("2006-GWBush.text")
text 
print(text)
pos = pos_tag(word_tokenize(text))
pos
print(pos) 
