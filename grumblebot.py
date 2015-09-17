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
	if cap < 1:
		irc.send("PRIVMSG " + chan + "Invalid RNG cap!\r\n")
		irc.send("PRIVMSG " + chan + "Taiya, tell Grumblesaur to punish them.\r\n")
		return
	value = random.randrange(cap)
	irc.send("PRIVMSG " + chan + " " + str(value) + "\r\n")

def quitwatch(data):
	if "grumblebot quit" in data:
		os.exit()

def greetwatch(data):
	if "hi grumblebot" in data:
		irc.send("PRIVMSG " + chan + "Hello!\r\n")
	if "hello grumblebot" in data:
		irc.send("PRIVMSG " + chan + "Hello!\r\n")
	
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((serv, port))

irc.recv(4096)
irc.send("NICK " + nick + "\r\n")
irc.send("USER " + nick + " " + nick + " " + nick + ":Grumblesaur IRC\r\n")
irc.send("JOIN " + chan + "\r\n")
irc.send("PRIVMSG " + chan + " :Hello.\r\n")

connected = False

while True:
	data = irc.recv(2048)
	sys.stdout.write(str(data))
	if data.find("PING") != -1:
		irc.send("PONG " + data.split()[1] + "\r\n")
	
	if connected == False:
		irc.send("JOIN " + chan + "\r\n")
	
	if "@Bele" in data:
		connected = True
		irc.send("PRIVMSG " + chan + " :Hello LT IRC!\r\n")
	
	data.lower()
	for char in data:
		if char in "?.!/;:,()[]{}#$%^&*@!":
			data = data.replace(char,"")
	
	botwatch(data)			
	
	if data.find("grumblebot roll") != -1:
		rollwatch(data)
	
	greetwatch(data)
	quitwatch(data)
	
	
