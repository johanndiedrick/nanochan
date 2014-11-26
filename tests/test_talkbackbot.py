from twisted.test import proto_helpers
from twisted.trial import unittest

from talkback.bot import TalkBackBotFactory

QUOTE = "There's nothing unusual about me. I'm normal."

class FakePicker(object):
	#always return the same quote
	
	def __init__(self, quote):
		self._quote = quote

	def pick(self):
		return self._quote

class TestTalkBackBot(unittest.SynchronousTestCase):
	_channel = "#testchannel"
	_username = "tester"
	_us = 'tbb'

	def setUp(self):
		
		factory = TalkBackBotFactory(
			self._channel,
			self._us,
			'Nano Shinonome',
			FakePicker(QUOTE),
			['twss'],
		)
		
		self.bot  = factory.buildProtocol(('127.0.0.1', 0))
		self.fake_transport = proto_helpers.StringTransport()
		self.bot.makeConnection(self.fake_transport)
		self.bot.signedOn()
		self.bot.joined(self._channel)
		self.fake_transport.clear()
	

	def test_privmsgNoTrigger(self):
		#shouldn't send a quote if message doesn't match trigger
		self.bot.privmsg(self._username, self._channel, "ohayoo")
		self.assertEqual('', self.fake_transport.value()
		)

	def test_privmsgWithTrigger(self):
		#should send a quote if message matches trigger
		self.bot.privmsg(self._username, self._channel, "twss")
		self.assertEqual(
			'PRIVMSG {channel} :{username}: {quote}\r\n'.format(
				channel=self._channel, username=self._username, quote=QUOTE
			),
			self.fake_transport.value()
		)

	
	def test_privmsgAttribution(self):
		#if someone attributes the bot in public, they get a public response
		self.bot.privmsg(self._username, self._channel, self._us + ': hakase!')
		self.assertEqual(
			'PRIVMSG {channel} :{username}: {quote}\r\n'.format(
				channel=self._channel, username=self._username, quote=QUOTE
			),
			self.fake_transport.value()
		)

	def test_privmsgPrivateMessage(self):
		#for private messages, should send quote directly to user
		self.bot.privmsg(self._username, self._us, "tadaima")
		self.assertEqual(
			'PRIVMSG {username} :{quote}\r\n'.format(
				username=self._username, quote=QUOTE
			),
			self.fake_transport.value()
		)

