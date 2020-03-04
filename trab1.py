from threading import Thread
import random
import string

anne = []
vogais = 0
consoantes = 0

for i in range(5000):
	anne.append(random.choice(string.ascii_lowercase))

def vogais():
	global vogais
	vogais = 0
	for i in anne:
		if i in ["a", "e", "i", "o", "u"]:
			vogais += 1
	print("Número de Vogais: " + str(vogais))

def consoantes():
	global consoantes
	consoantes = 0
	for i in anne:
		if i not in ["a", "e", "i", "o", "u"]:
			consoantes += 1
	print("Número de Consoantes: " + str(consoantes))

def ordenar():
	ajuda = []
	for i in range(0, len(anne)):
		ajuda.append(ord(anne[i]))
	ajuda.sort()
	for i in range(0, len(anne)):
		anne[i] = chr(ajuda[i])
	print(anne)

testinho1 = Thread(target = vogais)
testinho2 = Thread(target = consoantes)
testinho3 = Thread(target = ordenar)
testinho3.start()
testinho2.start()
testinho1.start()