from twisted.internet import protocol
from twisted.python import log
from twisted.words.protocols import irc


class TalkBackBot(irc.IRCClient):

	def connectionMade(self):
		#called when a connection is made
		self.nickname = self.factory.nickname
		self.realname = self.factory.realname
		irc.IRCClient.connectionMade(self)
		log.msg("connection was made!")

	def connectionLost(self, reason):
		#called when a connection is lost
		irc.IRCClient.connectionLost(self, reason)
		log.msg("connection lost :( {!r}".format(reason))

	#event callbacks
	
	def signedOn(self):
		#called when bot has sucessfully signed on to server
		log.msg("we have signed on, yay!")
		if self.nickname != self.factory.nickname:
			log.msg('your nick was already taken :(. your new nick is "{}".'
			.format(self.nickname))
		self.join(self.factory.channel)

	def joined(self, channel):
		#called when the bot joins the channel
		log.msg("[{nick} has joined {channel}]"
		.format(nick=self.nickname, channel=self.factory.channel))

	def privmsg(self, user, channel, msg):
		#called when the bot receives a msg 
		sendTo = None
		prefix = ''
		senderNick = user.split('!', 1)[0]
		if channel == self.nickname:
			#send a msg back
			sendTo = senderNick
		elif msg.startswith(self.nickname):
			#reply back in the channel
			sendTo = channel
			prefix = senderNick + ': '
		else:
			msg = msg.lower()
			for trigger in self.factory.triggers:
				if msg in trigger:
					sendTo = channel
				prefix = senderNick + ': '
				break

		if sendTo: #check to see if we have found someone to send to
			quote = self.factory.quotes.pick()
			self.msg(sendTo, prefix + quote)
			log.msg("sent message to {receiver}, triggered by {sender}:\n\t{quote}"
			.format(receiver=sendTo, sender=senderNick, quote=quote))

class TalkBackBotFactory(protocol.ClientFactory):
	
	#define the protocol that the factory will make the bot with, TalkBackBot
	protocol = TalkBackBot

	#instantiate the talkbackbot irc protocol
	def __init__(self, channel, nickname, realname, quotes, triggers):
		#initialize the boy factory with our settings 
		self.channel = channel
		self.nickname = nickname
		self.realname = realname
		self.quotes = quotes
		self.triggers = triggers
