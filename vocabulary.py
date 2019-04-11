from nltk.corpus import wordnet

synonyms = []
antonyms = []

word = input("Enter word : ")

for idx,syn in enumerate(wordnet.synsets(word)):
	print(f"<{idx+1}>","definition -", syn.definition())
	
	# if examples exist then print examples
	if syn.examples():
		print('examples')
		for i,ex in enumerate(syn.examples()):
			print(f"\t({i+1})", ex)
	
	# finding synonyms using lemmas
	for lemma in syn.lemmas():
		synonyms.append(lemma.name())

		# finding antonyms
		if lemma.antonyms():
			for antonym in lemma.antonyms():
				antonyms.append(antonym.name())

synonyms = set(synonyms)
antonyms = set(antonyms)

# synonyms
print('synonyms :',', '.join(synonyms))
# antonyms
print('antonyms :',', '.join(antonyms))