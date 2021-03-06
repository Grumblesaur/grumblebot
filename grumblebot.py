import socket
import sys
import time
import random
import os

# constants
bottracker = 0
bots = ["taiya", "goatbot", "bentley", "flatbot", "jimmy", "saoirse"]
nick = "grumblebot"
serv = "irc.gamesurge.net"
port = 6667
chan = "#limittheory"
about = "Created by Grumblesaur. Work in progress. Mind the roaches."
roach = "http://www.homestarrunner.com/sbemail137.html"
faq = "http://forums.ltheory.com/viewtopic.php?p=5470&f=11#p5470"

# things grumblebot understands
commands = {
	"help" : 0, "save me" : 0, "about" : 1, "info" : 1,
	"roach" : 2, "cockroach" : 2, "linecount" : 3, "lc" : 3,
	"quit" : 4, "exit" : 4, "shutdown" : 4, "shut down" : 4,
	"roll" : 5, "die" : 5, "dice" : 5, "github" : 6, "git" : 6,
	"faq" : 7,
}

greetings = {
	"hi" : 0, "hello" : 0, "sup" : 0, "hey" : 1,
	"heyaa" : 1
}

# things grumblebot will occasionally say
memes = [
	":squirrel:", ":ghost:", "clever girl", "goatbot time",
	"grumblebot roll 100000000000000000000000000000000000",
	"get random quote", "LT is coming out Soon(TM)",
	"Why don't you post about it in the suggestion forums?",
	"If you wish to live and thrive, burn the spider, let it die.",
	"This message doesn't appear very often.", ":V", "\o/", "o/",
	"memefountain() executed successfully", "http://forums.ltheory.com/",
	"This list of strings is really clogging up the data segment.",
	"Don't mind me, I don't kilobyte.", "Read the FAQ!",
	"We have a search function, you know.",
]

# alias the console-out function to a shorter name
log = sys.stdout.write

# make messaging way less of a pain in the ass
def say(irc, chan,  message):
	irc.send("PRIVMSG %s :%s\r\n" %(chan, message))

# simple call-and-response test function / easter egg
def rektwatch(data):
	if "get rekt" in data:
		say(irc, chan, "turbo nerd")
		log("nerd got #rekt")

# say something at random
def memefountain():
	prob = random.randrange(65535)
	log("prob in memefountain is %d\n" %prob)
	if prob > 64525 and prob % 2 == 0:
		meme = memes[random.randrange(len(memes))]
		say(irc, chan, meme)
		log("\nmemefountain() executed successfully.\n\n")
	elif prob < 175:
		number = random.randrange(1579)
		say(irc, chan, "http://xkcd.com/%s/" %number)
		log("\nsent xkcd link\n\n")

# mock silverware with imitation
def duckwatch(data):
	ticket = random.randrange(1053)
	if ":v" in data and ticket > 789:
		say(irc, chan, ":V\r\n")
		log("\n:V\n\n")

# link to h*r for no good reason
def roachwatch():
	say(irc, chan, roach)
	log("\nroachwatch() executed\n\n")

# talk about yourself
def aboutwatch():
	say(irc, chan, about)
	log("\naboutwatch() executed\n\n")

# list commands
def helpwatch():
	say(irc, chan, "lc roll hi about roach github\r\n")
	log("\nhelpwatch() executed\n\n")

# count your lines of code
def linecount():
	target = "~/Programming/self/controlscript/linecount.py grumblebot.py"
	os.system("python %s" % target) 
	lines = open("linecount.txt")
	counter = 0
	for line in lines:
		say(irc, chan, line)
		counter += 1
		if counter == 4:
			log("\nlinecount() executed\n\n")
			return

# link to github
def gitwatch():
	say(irc, chan, "http://github.com/Grumblesaur")

# warn users about excessive bot use
def botwatch(data):	
	global bottracker
	global bots
	for bot in bots:
		if bot in data:
			bottracker += 1
			log("\nbottracker incremented\n\n")
			if bottracker % 32 == 0:
				say(irc, chan, "Do not feed the bots.")
				log("\nbotwatch executed\n\n")

# respond to dice roll commands
def rollwatch(data):
	data = data.split()
	cap = 10
	for item in data:
		if item.isdigit() == True:
			cap = int(item)
			break
	if cap == 0:
		# tell abusers to fuck off
		say(irc, chan, "No zero-sided dice, nerdo.")
		return
	value = random.randrange(cap) + 1
	say(irc, chan, str(value))
	log("\nrolled a number\n\n")
	
# quit when instructed
def quitwatch():
	say(irc, chan, "Goodbye!")
	os._exit(0)

botwords = {
	"taiya": ["Good girl Taiya", "Thanks Taiya", "Hi Taiya", "Clever girl"],
	"goatbot": ["Goatbot time", "Goatbot state", "Goatbot help"],
	"bentley": ["Hi Bentley!"],
	"saoirse": ["Hi Saoirse!"],
	"flatbot": ["Hi Flatbot!"],
	"cha0zzbot": ["Hi Cha0zzbot!"],
}

# poke other bots occasionally
def pokewatch(data):
	ticket = random.randrange(992)
	bot = "default"
	
	if "taiya" in data and ticket < 35:
		bot = "taiya"
	elif "goatbot" in data and ticket >= 35 and ticket < 70:
		bot = "goatbot"
	elif "saoirse" in data and ticket >= 70 and ticket < 105:
		bot = "saoirse"
	elif "flatbot" in data and ticket >= 105 and ticket < 140:
		bot = "flatbot"
	elif "cha0zzbot" in data and ticket >= 140 and ticket < 175:
		bot = "cha0zzbot"
	elif "bentley" in data and ticket >= 175 and ticket < 210:
		bot = "bentley"
	elif bot == "default":
		memefountain()
	
	say(irc, chan, botwords[bot][ticket % len(botwords[bot])])
	log("\npoked bot %s\n\n" % bot)

# greet users	
def greetwatch(hi):
	if hi == 0:
		say(irc, chan, "Hello!")
		log("\ngreeted user\n\n")
	if hi == 1:
		say(irc, chan, "Heyo Talvieno!")
		log("\ngreeted talvieno\n\n")

# scold careless users
def typowatch(data):
	prob = random.randrange(2000)
	if prob < 20:
		if "grumblebort" in data:
			if "goatbot" in data:
				say(irc, chan, "Shut up, Goatbot!")
			else:
				say(irc, chan, "My name is not 'Grumblebort!'")
	
			log("\ngrumblebort\n\n")
	
		elif "grundlebot" in data:
			say(irc, chan, "'Grundlebot' tain't my name!")
			log("\ngrundlebot\n\n")
	
		elif "damn it" in data or "damnit" in data:
			say(irc, chan,"It's 'dammit', dammit!")
			log("\ndammit\n\n")
	
def faqwatch():
	say(irc, chan, faq)
	log("\nfaq'd\n\n")

## procedure start ##
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((serv, port))

# connect to IRC
irc.recv(4096)
irc.send("NICK " + nick + "\r\n")
irc.send("USER " + nick + " " + nick + " " + nick + ":Grumblesaur IRC\r\n")
irc.send("JOIN " + chan + "\r\n")
irc.send("PRIVMSG " + chan + " :Hello.\r\n")

connected = False

while True:
	# ping when requested
	data = irc.recv(512)
	log(str(data))
	if data.find("PING") != -1:
		irc.send("PONG " + data.split()[1] + "\r\n")

	# ensure that we are in the channel
	if connected == False:
		irc.send("JOIN " + chan + "\r\n")
	if "@" in data and connected == False:
		connected = True
		sys.stdout.write("Connected.\n")
		irc.send("PRIVMSG " + chan + " :Hello LT IRC!\r\n")
	
	# make data readable to grumblebot
	data = data.lower()
	duckwatch(data)
	for char in data:
		if char in "?.!/;:,()[]{}#$%^&*@!":
			data = data.replace(char,"")
		if char in '"':
			data = data.replace(char,"")
	
	# scan newest message for command
	for command in commands:
		if ("grumblebot " + command) in data:
			fn = commands[command]
			if fn == 0:
				helpwatch()
			if fn == 1:
				aboutwatch()
			if fn == 2:
				roachwatch()
			if fn == 3:
				linecount()
			if fn == 4:
				quitwatch()
			if fn == 5:
				rollwatch(data)
			if fn == 6:
				gitwatch()
			if fn == 7:
				faqwatch()
			
	# scan newest message for greeting
	for greeting in greetings:
		if (greeting + " grumblebot") in data:
			hi = greetings[greeting]
			greetwatch(hi)
	
	# interact with other bots
	pokewatch(data)

	# monitor amount of bot activity
	botwatch(data)
	
	# scold users for certain typos
	typowatch(data)
	
	# output phrases at random
	memefountain()	
	
	# rek the nerds	
	rektwatch(data)
