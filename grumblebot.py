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

def roachwatch():
	irc.send("PRIVMSG " + chan + " : " + roach + "\r\n")

def aboutwatch():
	irc.send("PRIVMSG " + chan + " :" + about + "\r\n")

def helpwatch():
	irc.send("PRIVMSG " + chan + " :lc roll hi about roach\r\n")

def linecount():
	os.system("linecount grumblebot.py")
	lines = open("linecount.txt")
	counter = 0
	for line in lines:
		irc.send("PRIVMSG " + chan + " :" + line + "\r\n")
		counter += 1
		if counter == 4:
			return
		
def gitwatch():
	irc.send("PRIVMSG " + chan + " :http://github.com/Grumblesaur\r\n")

def botwatch(data):	
	global bottracker
	global bots
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
		irc.send("PRIVMSG " + chan + " :Invalid RNG cap!\r\n")
		return
	value = random.randrange(cap) + 1
	irc.send("PRIVMSG " + chan + " " + str(value) + "\r\n")

def quitwatch():
	irc.send("PRIVMSG " + chan + " :Goodbye!\r\n")
	sys.exit()

def taiyawatch(data):
	ticket = random.randrange(1053)
	if "taiya" in data and ticket > 1024:
		irc.send("PRIVMSG " + chan + " :Good girl, Taiya.\r\n")
	elif ":v" in data and ticket > 586:
		irc.send("PRIVMSG " + chan + " : :V\r\n")
	
def greetwatch(hi):
	if hi == 0:
		irc.send("PRIVMSG " + chan + " :Hello!\r\n")
	if hi == 1:
		irc.send("PRIVMSG " + chan + " :Heyo Talvieno!\r\n")

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
			
	for greeting in greetings:
		if (greeting + " grumblebot") in data:
			hi = greetings[greeting]
			greetwatch(hi)
	
	taiyawatch(data)
	botwatch(data)
		
