import os, random

#Selects a random file from the episodes folder
path = os.getcwd() + '/episodes'
files = os.listdir(path)
index = random.randrange(0, len(files))
episode = path + '/' + (files[index])

#opens the random file with omxplayer
os.system('./omxplayer -p -o hdmi ' + path)
