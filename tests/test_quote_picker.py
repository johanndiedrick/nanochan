import os

from twisted.trial import unittest

from talkback.quote_picker import QuotePicker

class TestQuotePicker(unittest.TestCase):
	QUOTE1 = ("Every day of youth is precious.")
	QUOTE2 = ("I think that's moe!")

	def test_pick(self):
		picker = QuotePicker(
			os.path.join(os.path.dirname(__file__), "test_quotes.txt")
		)
		quote = picker.pick()
		self.assertIn(quote, (self.QUOTE1, self.QUOTE2), "got unexpected quote :'%s'" % (quote))


