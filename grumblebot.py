import socket
import sys
import time
import random
import os

bottracker = 0
bots = ["taiya", "fwipbot", "goatbot"]
nick = "grumblebot"
serv = "irc.gamesurge.net"
port = 6667
chan = "#limittheory"
about = "Created by Grumblesaur. Work in progress. Mind the roaches."
roach = "http://www.homestarrunner.com/sbemail137.html"

def roachwatch(data):
	if "grumblebot roach" in data:
		irc.send("PRIVMSG " + chan + " : " + roach + "\r\n")

def aboutwatch(data):
	if "grumblebot about" in data:
		irc.send("PRIVMSG " + chan " :" + about + "\r\n")

def helpwatch(data):
	if "grumblebot help" in data:
		irc.send("PRIVMSG " + chan + " :lc roll hi\r\n")

def linecount(data):
	if "grumblebot lc" in data or "grumblebot linecount" in data:
		os.system("linecount grumblebot.py")
		lines = open("linecount.txt")
		counter = 0
		for line in lines:
			irc.send("PRIVMSG " + chan + " :" + line + "\r\n")
			counter += 1
			if counter == 4:
				return
			
def botwatch(data):	
	global bottracker
	global bots
	data = data.lower()
	for bot in bots:
		if bot in data:
			bottracker += 1
			if bottracker % 25 == 0:
				irc.send("PRIVMSG " + chan + " :Do not feed the bots.\r\n")

def rollwatch(data):
	data = data.split()
	cap = 10
	for item in data:
		if item.isdigit() == True:
			cap = int(item)
			break
	if cap == 0:
		irc.send("PRIVMSG " + chan + "Invalid RNG cap!\r\n")
		return
	value = random.randrange(cap) + 1
	irc.send("PRIVMSG " + chan + " " + str(value) + "\r\n")

def quitwatch(data):
	global irc
	global chan
	if "grumblebot quit" in data:
		irc.send("PRIVMSG " + chan + "Goodbye!\r\n")
		sys.exit()

def taiyawatch(data):
	ticket = random.randrange(1053)
	if "taiya" in data and ticket > 1024:
		irc.send("PRIVMSG " + chan + " :Good girl, Taiya.\r\n")
	
def greetwatch(data):
	if "hi grumblebot" in data or "hello grumblebot" in data:
		irc.send("PRIVMSG " + chan + " :Hello!\r\n")
	if "hey grumblebot" in data or "heyaa grumblebot" in data:
		irc.send("PRIVMSG " + chan + " :Hello, probably Talvieno.\r\n")
	if "yo grumblebot" in data:
		irc.send("PRIVMSG " + chan + " :Hello, probably Jetison333.\r\n")
	if "grumblebort" in data:
		irc.send("PRIVMSG " + chan + " :My name is not 'Grumblebort'!\r\n")
	if "grundlebot" in data:
		irc.send("PRIVMSG " + chan + " :'Grundlebot' tain't my name!\r\n")
	if "damnit" in data or "damn it" in data:
		irc.send("PRIVMSG " + chan + " :It's 'dammit', there's no 'n'.\r\n")

	
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((serv, port))

irc.recv(4096)
irc.send("NICK " + nick + "\r\n")
irc.send("USER " + nick + " " + nick + " " + nick + ":Grumblesaur IRC\r\n")
irc.send("JOIN " + chan + "\r\n")
irc.send("PRIVMSG " + chan + " :Hello.\r\n")

connected = False

while True:
	data = irc.recv(512)
	sys.stdout.write(str(data))
	if data.find("PING") != -1:
		irc.send("PONG " + data.split()[1] + "\r\n")
	
	if connected == False:
		irc.send("JOIN " + chan + "\r\n")
	
	if "@Bele" in data:
		connected = True
		sys.stdout.write("Connected.\n")
		irc.send("PRIVMSG " + chan + " :Hello LT IRC!\r\n")
	
	data = data.lower()
	for char in data:
		if char in "?.!/;:,()[]{}#$%^&*@!":
			data = data.replace(char,"")

	greetwatch(data)
	botwatch(data)			
	taiyawatch(data)
	linecount(data)
	helpwatch(data)	
	if data.find("grumblebot roll") != -1:
		rollwatch(data)
	
	quitwatch(data)
	
		
