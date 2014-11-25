from random import choice

class QuotePicker(object):
	
	def __init__(self, quotes_filename):
		#initialize our quote picker class with quotes from a file
		with open(quotes_filename) as quotes_file:
			self.quotes = quotes_file.readlines()
	
	def pick(self):
		#return a random quote
		return choice(self.quotes).strip()
