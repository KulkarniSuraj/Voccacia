class Word:
	"""Word and its related attributes"""
	def __init__(self, word):
		super(Word, self).__init__()
		if word.strip().isalpha():
			self.word = word
		else:
			raise ValueError("Invalid word")