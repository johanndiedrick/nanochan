from ConfigParser import ConfigParser

from twisted.application.service import IServiceMaker, Service
from twisted.internet.endpoints import clientFromString
from twisted.plugin import IPlugin
from twisted.python import usage, log
from zope.interface import implementer

from talkback.bot import TalkBackBotFactory
from talkback.quote_picker import QuotePicker

#used to parse our configuration
class Options(usage.Options):
	#twistd shinolab --config=/path/to/settings.ini
	#twistd shinolab -c /path/to/settings.ini
	optParameters = [
		['config', 'c', 'settings.ini', 'Configuration file.'],
	]

#constructs our application using Twisted's Service class to start/stop our app
class TalkBackBotService(Service):

	#this gets called down in makeService of BotServiceMaker
	def __init__(self, endpoint, channel, nickname, realname, quotesFilename, triggers):
		#initialize out service
		self._endpoint = endpoint
		self._channel = channel
		self._nickname = nickname
		self._realname = realname
		self._quotesFilename = quotesFilename
		self._triggers = triggers	
	
	def startService(self):
		#construct a client and connect to server
		from twisted.internet import reactor
		
		def connected(bot):
			self._bot = bot
		def failure(err):
			log.err(err, _why='could not connect to specified server :/')
			reactor.stop()
		
		quotes = QuotePicker(self._quotesFilename)
		client = clientFromString(reactor, self._endpoint)
		factory = TalkBackBotFactory(
			self._channel,
			self._nickname,
			self._realname,
			quotes,
			self._triggers
		)
		
		return client.connect(factory).addCallbacks(connected, failure)

	def stopService(self):
		#disconnect
		if self._bot and self._bot.transport.connected:
			self._bot.transport.loseConnection()

#maker class that constructs our service
@implementer(IServiceMaker, IPlugin)
class BotServiceMaker(object):
	tapname = "shinolab"
	description = "have hakase build nano and invite her to our channel!"
	options = Options

	def makeService(self, options):
		#construct the talkbackbot service
		config = ConfigParser() #essentially read out settings.ini file
		config.read([options['config']])
		triggers = [
			trigger.strip()
			for trigger
			in config.get('talkback', 'triggers').split('\n')
			if trigger.strip()
		]

		return TalkBackBotService(
			endpoint = config.get('irc', 'endpoint'),
			channel = config.get('irc', 'channel'),
			nickname = config.get('irc', 'nickname'),
			realname = config.get('irc', 'realname'),
			quotesFilename = config.get('talkback', 'quotesFilename'),
			triggers=triggers
		)

				
#now construct an objecet which *provides* the relevant interfaces.
#the name is irrevelant, as long as there is some name bound to a provider of iPlugin/iServiceMaker

serviceMaker = BotServiceMaker()
