from nltk.corpus import wordnet
import random

word = input("Enter word : ")
# hypernyms are generic word
hypernyms = []
# hyponyms are specific words than given words
hyponyms = []

for syn in wordnet.synsets(word):
	
	if syn.hyponyms():
		for hypo in syn.hyponyms():
			if hypo.lemmas():
				for l in hypo.lemmas():
					hyponyms.append(l.name())

	if syn.hypernyms():
		for hyper in syn.hypernyms():
			if hyper.lemmas():
				for l in hyper.lemmas():
					hypernyms.append(l.name())


hypernyms = set(hypernyms)
hyponyms = set(hyponyms)
	
print("hypernyms :", ", ".join(hypernyms))
print("\n")
print("hyponyms :", ", ".join(hyponyms))


