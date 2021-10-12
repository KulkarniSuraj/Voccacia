
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
		self.syns = []
		for syn in wordnet.synsets(self.word):
			self.syns.append(syn)

	def get_synonyms(self):
		from nltk.corpus import wordnet
		synonyms = set()
		for syn in self.syns:
			# find synonyms using lemma
			for lemma in syn.lemmas():
				synonyms.add(lemma.name())
		return synonyms


