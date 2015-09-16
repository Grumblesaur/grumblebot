import socket
import sys
import time
import random

def botwatch(data):	
	bottracker = 0
	data = data.lower()
	if data.find("taiya") != -1 or data.find("goatbot") != -1:
		bottracker += 1
		if bottracker % 25 == 0:
			irc.send("PRIVMSG " + channel + " :Do not feed the bots.\r\n")

def rollwatch(data):
		data = data.split()
		cap = 10
		for item in data:
			if item.isdigit() == True:
				cap = int(item)
				break
		value = random.randrange(cap)
		irc.send("PRIVMSG " + channel + " " + str(value) + "\r\n")
	
nick = "grumblebot"
server = "irc.gamesurge.net"
port = 6667
channel = "#limittheory"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))

irc.recv(4096)
irc.send("NICK " + nick + "\r\n")
irc.send("USER " + nick + " " + nick + " " + nick + ":Grumblesaur IRC\r\n")
irc.send("JOIN " + channel + "\r\n")
irc.send("PRIVMSG " + channel + " :Hello.\r\n")

connected = False

while True:
	data = irc.recv(4096)
	sys.stdout.write(str(data))
	if data.find("PING") != -1:
		irc.send("PONG " + data.split()[1] + "\r\n")
	
	if connected == False:
		irc.send("JOIN " + channel + "\r\n")
	
	if "@Bele" in data:
		connected = True
		irc.send("PRIVMSG " + channel + " :Hello LT IRC!\r\n")
	
	# clean the data stream for botwatch and rollwatch
	data.lower()
	for char in data:
		if char in "?.!/;:,()[]{}#$%^&*@!":
			data = data.replace(char,"")
	
	botwatch(data)			
	
	if data.find("grumblebot roll") != -1:
		rollwatch(data)

	
