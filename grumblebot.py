import socket
import sys
import time
import random
import os

# constants
bottracker = 0
bots = ["taiya", "goatbot", "bentley", "flatbot", "cha0zzbot", "saoirse"]
nick = "grumblebot"
serv = "irc.gamesurge.net"
port = 6667
chan = "#limittheory"
about = "Created by Grumblesaur. Work in progress. Mind the roaches."
roach = "http://www.homestarrunner.com/sbemail137.html"

# things grumblebot understands
commands = {
	"help" : 0, "save me" : 0, "about" : 1, "info" : 1,
	"roach" : 2, "cockroach" : 2, "linecount" : 3, "lc" : 3,
	"quit" : 4, "exit" : 4, "shutdown" : 4, "shut down" : 4,
	"roll" : 5, "die" : 5, "dice" : 5, "github" : 6, "git" : 6,
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
	
def rektwatch(data):
	if "get rekt" in data:
		say(irc, chan, "turbo nerd")
		log("nerd got #rekt")

def memefountain():
	prob = random.randrange(65535)
	log("prob in memefountain is %d\n" %prob)
	if prob > 63525:
		meme = memes[random.randrange(len(memes))]
		say(irc, chan, meme)
		log("\nmemefountain() executed successfully.\n\n")
	elif prob < 175:
		number = random.randrange(1579)
		say(irc, chan, "http://xkcd.com/%s/" %number)
		log("\nsent xkcd link\n\n")
	
def duckwatch(data):
	ticket = random.randrange(1053)
	if ":v" in data and ticket > 789:
		say(irc, chan, ":V\r\n")
		log("\n:V\n\n")

def roachwatch():
	say(irc, chan, roach)
	log("\nroachwatch() executed\n\n")

def aboutwatch():
	say(irc, chan, about)
	log("\naboutwatch() executed\n\n")

def helpwatch():
	say(irc, chan, "lc roll hi about roach github\r\n")
	log("\nhelpwatch() executed\n\n")

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
		
def gitwatch():
	say(irc, chan, "http://github.com/Grumblesaur")

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

def rollwatch(data):
	data = data.split()
	cap = 10
	for item in data:
		if item.isdigit() == True:
			cap = int(item)
			break
	if cap == 0:
		say(irc, chan, "No zero-sided dice, nerdo.")
		return
	value = random.randrange(cap) + 1
	say(irc, chan, str(value))
	log("\nrolled a number\n\n")
	
def quitwatch():
	say(irc, chan, "Goodbye!")
	os._exit(0)

def pokewatch(data):
	ticket = random.randrange(1053)
	
	#TODO: add randomized phrases for each bot
	
	if "taiya" in data and ticket > 1024:
		say(irc, chan, "Good girl, Taiya.")
		log("\ncomplimented taiya\n\n")
	if "goatbot" in data and ticket < 30:
		say(irc, chan, "Goatbot what?\r\n")
		log("\npoked goatbot\n\n")
	#TODO: add to these later
	if "saoirse" in data and ticket > 30 and ticket < 70:
		pass
	if "flatbot" in data and ticket > 70 and ticket < 110:
		pass
	if "cha0zzbot" in data and ticket > 110 and ticket < 150:
		pass
	if "bentley" in data and ticket > 150 and ticket < 190:
		pass
	
def greetwatch(hi):
	if hi == 0:
		say(irc, chan, "Hello!")
		log("\ngreeted user\n\n")
	if hi == 1:
		say(irc, chan, "Heyo Talvieno!")
		log("\ngreeted talvieno\n\n")

def typowatch(data):
	if "grumblebort" in data:
		if "goatbot" in data:
			say(irc, chan, "Shut up, Goatbot!")
		else:
			say(irc, chan, "My name is not 'Grumblebort!'")

		log("\ngrumblebort\n\n")

	if "grundlebot" in data:
		say(irc, chan, "'Grundlebot' tain't my name!")
		log("\ngrundlebot\n\n")

	if "damn it" in data or "damnit" in data:
		say(irc, chan,"It's 'dammit', dammit!")
		log("\ndammit\n\n")
	
# procedure start
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
