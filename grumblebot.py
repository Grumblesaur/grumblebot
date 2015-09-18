import socket
import sys
import time
import random
import os
import time

bottracker = 0
bots = ["taiya", "goatbot"]
nick = "grumblebot"
serv = "irc.gamesurge.net"
port = 6667
chan = "#limittheory"
about = "Created by Grumblesaur. Work in progress. Mind the roaches."
roach = "http://www.homestarrunner.com/sbemail137.html"

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

memes = [
	":squirrel:", ":ghost:", "clever girl", "goatbot time",
	"grumblebot roll 100000000000000000000000000000000000",
	"get random quote", "LT is coming out Soon(TM)",
	"Why don't you post about it in the suggestion forums?",
	"If you wish to live and thrive, burn the spider, let it die.",
	"This message doesn't appear very often.", ":V", "\o/", "o/",
	"memefountain() executed successfully", "http://forums.ltheory.com/",
	"This list of strings is really clogging up the data segment.",
	"Don't mind me, I don't kilobyte.", "http://xkcd.com/221",
]

def memefountain():
	prob = random.randrange(65535)
	sys.stdout.write("prob in memefountain is %d\n" %prob)
	if prob > 63525:
		meme = memes[random.randrange(len(memes))]
		irc.send("PRIVMSG " + chan + " :" + meme + "\r\n")
		sys.stdout.write("\nmemefountain() executed successfully.\n\n")

def duckwatch(data):
	ticket = random.randrange(1053)
	if ":v" in data and ticket > 789:
		irc.send("PRIVMSG " + chan + " ::V\r\n")
		sys.stdout.write("\n:V\n\n")

def roachwatch():
	irc.send("PRIVMSG " + chan + " : " + roach + "\r\n")
	sys.stdout.write("\nroachwatch() executed\n\n")

def aboutwatch():
	irc.send("PRIVMSG " + chan + " :" + about + "\r\n")
	sys.stdout.write("\naboutwatch() executed\n\n")

def helpwatch():
	irc.send("PRIVMSG " + chan + " :lc roll hi about roach github\r\n")
	sys.stdout.write("\nhelpwatch() executed\n\n")

def linecount():
	target = "~/Programming/self/controlscript/linecount.py grumblebot.py"
	os.system("python %s" % target) 
	lines = open("linecount.txt")
	counter = 0
	for line in lines:
		irc.send("PRIVMSG " + chan + " :" + line + "\r\n")
		counter += 1
		if counter == 4:
			sys.stdout.write("\nlinecount() executed\n\n")
			return
		
def gitwatch():
	irc.send("PRIVMSG " + chan + " :http://github.com/Grumblesaur\r\n")

def botwatch(data):	
	global bottracker
	global bots
	for bot in bots:
		if bot in data:
			bottracker += 1
			sys.stdout.write("\nbottracker incremented\n\n")
			if bottracker % 25 == 0:
				irc.send("PRIVMSG " + chan + " :Do not feed the bots.\r\n")
				sys.stdout.write("\nbotwatch executed\n\n")

def rollwatch(data):
	data = data.split()
	cap = 10
	for item in data:
		if item.isdigit() == True:
			cap = int(item)
			break
	if cap == 0:
		irc.send("PRIVMSG " + chan + " :Invalid RNG cap!\r\n")
		return
	value = random.randrange(cap) + 1
	irc.send("PRIVMSG " + chan + " " + str(value) + "\r\n")
	sys.stdout.write("\nrolled a number\n\n")
	
def quitwatch():
	irc.send("PRIVMSG " + chan + " :Goodbye!\r\n")
	os._exit(0)

def taiyawatch(data):
	ticket = random.randrange(1053)
	if "taiya" in data and ticket > 1024:
		irc.send("PRIVMSG " + chan + " :Good girl, Taiya.\r\n")
		sys.stdout.write("\ncomplimented taiya\n\n")
	if "goatbot" in data and ticket < 30:
		irc.send("PRIVMSG " + chan + " :Goatbot what?\r\n")
		sys.stdout.write("\npoked goatbot\n\n")
	
def greetwatch(hi):
	if hi == 0:
		irc.send("PRIVMSG " + chan + " :Hello!\r\n")
		sys.stdout.write("\ngreeted user\n\n")
	if hi == 1:
		irc.send("PRIVMSG " + chan + " :Heyo Talvieno!\r\n")
		sys.stdout.write("\ngreeted talvieno\n\n")

def typowatch(data):
	if "grumblebort" in data:
		irc.send("PRIVMSG " + chan + " :My name is not 'Grumblebort!'\r\n")
		sys.stdout.write("\ngrumblebort\n\n")
	if "grundlebot" in data:
		irc.send("PRIVMSG " + chan + " :'Grundlebot' tain't my name!\r\n")
		sys.stdout.write("\ngrundlebot\n\n")
	if "damn it" in data or "damnit" in data:
		irc.send("PRIVMSG " + chan + " :It's 'dammit', dammit!\r\n")
		sys.stdout.write("\ndammit\n\n")
	
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
	sys.stdout.write(str(data))
	if data.find("PING") != -1:
		irc.send("PONG " + data.split()[1] + "\r\n")

	# ensure that we are in the channel
	if connected == False:
		irc.send("JOIN " + chan + "\r\n")
	if "@Bele" in data:
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
	
	# interact with taiya or silverware
	taiyawatch(data)

	# monitor amount of bot activity
	botwatch(data)
	
	# scold users for certain typos
	typowatch(data)
	
	# output phrases at random
	memefountain()		
