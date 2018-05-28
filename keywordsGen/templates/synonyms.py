#Getting Started with Synonyms generations for keywords

import nltk
from nltk.corpus import wordnet
synonyms = []
antonyms = []
 
for syn in wordnet.synsets("buy"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
 
print(set(synonyms))
print(set(antonyms))