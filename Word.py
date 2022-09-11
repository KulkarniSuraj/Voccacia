
class Word:

	"""Word and its related attributes"""
	def __init__(self, word):
		from nltk.corpus import wordnet
		super(Word, self).__init__()
		if word.strip().isalpha():
			self.word = word
		else:
			raise ValueError("Invalid word")
		# generate synset of the word 
		self.syns = wordnet.synsets(self.word)

	def get_synonyms(self):
		from nltk.corpus import wordnet
		synonyms = set()
		for syn in self.syns:
			# find synonyms using lemma
			for lemma in syn.lemmas():
				synonyms.add(lemma.name())
		return synonyms

	def get_antonyms(self):
		from nltk.corpus import wordnet
		antonyms = set()
		for syn in self.syns:
			for lemma in syn.lemmas():
				if lemma.antonyms():
					for antonym in lemma.antonyms():
						antonyms.add(antonym.name())
		return antonyms

	def get_definitions(self):
		from nltk.corpus import wordnet
		# defs will contain definitions and examples associated with it
		
		defs = {}
		for syn in self.syns:
			defs[syn.definition()] = [ex for ex in syn.examples() if syn.examples()]

		return defs

	def get_hyponyms(self):
		# hyponyms are generic word i.e. vehicle is hyponym of car
		hyponyms = set()
		for syn in self.syns:
			if syn.hyponyms():
				for hypo in syn.hyponyms():
					if hypo.lemmas():
						for l in hypo.lemmas():
							hyponyms.add(l.name())
		return hyponyms

	def get_hypernyms(self):
		# hypernyms are specific words i.e. car is hypernym of vehicle
		hypernyms = set()
		for syn in self.syns:
			if syn.hypernyms():
				for hyper in syn.hypernyms():
					if hyper.lemmas():
						for l in hyper.lemmas():
							hypernyms.add(l.name())
		return hypernyms

