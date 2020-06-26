import requests
from datetime import datetime
import os
import sys
#import tensorflow as tf 
#from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import requests
import re
from scipy import spatial
#USE ME 
iVar = [255,165,0] 
#player input will implimemnted when learning as aplied

response = requests.get("https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F")
htmltext = response.text
namesAns = ""
rgbAns = ""
clonetest = ""
testString = ""
rgbOut = []
namesAnsString = []



for line in htmltext.split('\n'):
	if "<th style=\"border-left:solid 4em rgb" in line:
		namesAns += line
		namesAns += "\n"
		    
		rgbAns += line
		rgbAns += "\n"
		clonetest+= line
		clonetest += "\n"   


rgbAns = re.compile("rgb\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?")
rgbAns=rgbAns.findall(namesAns)
#print(clonetest)
#print(rgbAns)
namesAns = re.compile(">[a-zA-z\s]*")
namesAns = namesAns.findall(clonetest)
for x in namesAns:
	if not x.strip("><\n")=="":
		namesAnsString.append(x.strip("><\n"))


for x in rgbAns:
	rgbOut.append(x.strip("rgb\("))
#print(namesAnsString)
#print(len(namesAnsString))
#print(len(rgbOut))
data = []
for x in namesAnsString:
	data.append([x])
for y, value in enumerate(rgbOut):
	data[y].append([int(v) for v in value.split(",")])

#print (data)
likeness = 0.0
mostSimilar = 0



for i, x in enumerate(data):
	likeness = spatial.distance.cosine(iVar, x[1])
	if likeness < spatial.distance.cosine(iVar,data[mostSimilar][1]):
		mostSimilar = i
print(iVar," is the color ", data[mostSimilar][0])