from threading import Thread
import random
import os
import time
import emoji

def faz_tabuleiro():
	linha = []
	for x in range(0, 5):
		for y in range(0, 40):
			linha.append(tabuleiro[(x*40)+y])
		print(*linha, sep = " ")
		linha = []

def dado():
	d6 = random.randint(1, 6)
	return d6

def andar(macaco):
	#o personagem anda no tabuleiro pela soma de dois d6
	if macaco.cabo == False:
		macaco.dado1 = dado()
		macaco.dado2 = dado()
	if macaco.andar == True:
		macaco.preso = "Não"
		macaco.posicao += macaco.dado1 + macaco.dado2
		macaco.jogadas += 1
		if ((macaco.posicao+1) % 2) == 0:
			macaco.dinheiro += 79.99
		else:
			macaco.dinheiro += 53.21
	#se os valores dos dados forem iguais o personagem fica preso
	if macaco.dado1 == macaco.dado2 and macaco.cabo == False:
			if macaco.andar == True:
				macaco.preso = emoji.emojize("TA PRESO PORRA :cop: :police_car: :rotating_light:", use_aliases = True)
				macaco.andar = False
			else:
				macaco.preso = emoji.emojize("Se Soltou :running:", use_aliases = True)
				macaco.andar = True
	#quando o personagem chega no final do tabuleiro ele para de andar e espera até todos chegarem la
	if macaco.posicao >= 199:
		macaco.posicao = 201
		macaco.andar = False
		macaco.preso = "Não"
		macaco.cabo = True

class macaco:
	def __init__(self, nome, preso, dinheiro, jogadas, sprite, posicao, dado1, dado2, andar, cabo):
		self.nome = nome
		self.preso = preso
		self.dinheiro = dinheiro
		self.jogadas = jogadas
		self.posicao = posicao
		self.sprite = sprite
		self.dado1 = dado1
		self.dado2 = dado2
		self.andar = andar
		self.cabo = cabo

#começou o jogo
tabuleiro = []
pode_andar = False
acabou = False

for x in range(0, 220):
	tabuleiro.append("_")
	if x == 199:
		tabuleiro[x] = emoji.emojize(":checkered_flag:", use_aliases = True)

os.system("clear")

#nomes
nome1 = input("Digite o nome do Jogador 1: ")
nome2 = input("Digite o nome do Jogador 2: ")
nome3 = input("Digite o nome do Jogador 3: ")
nome4 = input("Digite o nome do Jogador 4: ")

sprite1 = emoji.emojize(":sunglasses:", use_aliases = True)
sprite2 = emoji.emojize(":smiling_imp:", use_aliases = True)
sprite3 = emoji.emojize(":innocent:", use_aliases = True)
sprite4 = emoji.emojize(":alien:", use_aliases = True)

macaco1 = macaco(nome1, "Não", 0, 0, sprite1, 0, 0, 0, True, False)
macaco2 = macaco(nome2, "Não", 0, 0, sprite2, 1, 0, 0, True, False)
macaco3 = macaco(nome3, "Não", 0, 0, sprite3, 2, 0, 0, True, False)
macaco4 = macaco(nome4, "Não", 0, 0, sprite4, 3, 0, 0, True, False)

while acabou == False:
	os.system("clear")
	
	#ui
	tabuleiro[macaco1.posicao] = macaco1.sprite
	tabuleiro[macaco2.posicao] = macaco2.sprite
	tabuleiro[macaco3.posicao] = macaco3.sprite
	tabuleiro[macaco4.posicao] = macaco4.sprite
	faz_tabuleiro()
	print("\n\n")
	
	print(emoji.emojize("Nome: " + macaco1.nome + " -> " + macaco1.sprite + "\n:moneybag: " + str(macaco1.dinheiro) + "\nMovimento :game_die:: " + str(macaco1.dado1) + " + " + str(macaco1.dado2) + "\nTa Preso? " + str(macaco1.preso) + "\nJogadas: " + str(macaco1.jogadas) + "\n", use_aliases = True))
	print(emoji.emojize("Nome: " + macaco2.nome + " -> " + macaco2.sprite + "\n:moneybag: " + str(macaco2.dinheiro) + "\nMovimento :game_die:: " + str(macaco2.dado1) + " + " + str(macaco2.dado2) + "\nTa Preso? " + str(macaco2.preso) + "\nJogadas: " + str(macaco2.jogadas) + "\n", use_aliases = True))
	print(emoji.emojize("Nome: " + macaco3.nome + " -> " + macaco3.sprite + "\n:moneybag: " + str(macaco3.dinheiro) + "\nMovimento :game_die:: " + str(macaco3.dado1) + " + " + str(macaco3.dado2) + "\nTa Preso? " + str(macaco3.preso) + "\nJogadas: " + str(macaco3.jogadas) + "\n", use_aliases = True))
	print(emoji.emojize("Nome: " + macaco4.nome + " -> " + macaco4.sprite + "\n:moneybag: " + str(macaco4.dinheiro) + "\nMovimento :game_die:: " + str(macaco4.dado1) + " + " + str(macaco4.dado2) + "\nTa Preso? " + str(macaco4.preso) + "\nJogadas: " + str(macaco4.jogadas) + "\n", use_aliases = True))

	tabuleiro[macaco1.posicao] = "_"
	tabuleiro[macaco2.posicao] = "_"
	tabuleiro[macaco3.posicao] = "_"
	tabuleiro[macaco4.posicao] = "_"

	#thread de movimento por personagem
	persongem1 = Thread(target=andar,args=[macaco1])
	persongem2 = Thread(target=andar,args=[macaco2])
	persongem3 = Thread(target=andar,args=[macaco3])
	persongem4 = Thread(target=andar,args=[macaco4])

	persongem1.start()
	persongem2.start()
	persongem3.start()
	persongem4.start()
	
	tabuleiro[199] = emoji.emojize(":checkered_flag:", use_aliases = True)

	#cabo
	if macaco1.cabo == True and macaco2.cabo == True and macaco3.cabo == True and macaco4.cabo == True:
		acabou = True
		os.system("clear")
		print(emoji.emojize("Nome: " + macaco1.nome + " -> " + macaco1.sprite + "\n:construction: Total de Jogadas: " + str(macaco1.jogadas) + "\nTotal Arrecadado :dollar:: " + str(macaco1.dinheiro) + "\n", use_aliases = True))
		print(emoji.emojize("Nome: " + macaco2.nome + " -> " + macaco2.sprite + "\n:construction: Total de Jogadas: " + str(macaco2.jogadas) + "\nTotal Arrecadado :dollar:: " + str(macaco2.dinheiro) + "\n", use_aliases = True))
		print(emoji.emojize("Nome: " + macaco3.nome + " -> " + macaco3.sprite + "\n:construction: Total de Jogadas: " + str(macaco3.jogadas) + "\nTotal Arrecadado :dollar:: " + str(macaco3.dinheiro) + "\n", use_aliases = True))
		print(emoji.emojize("Nome: " + macaco4.nome + " -> " + macaco4.sprite + "\n:construction: Total de Jogadas: " + str(macaco4.jogadas) + "\nTotal Arrecadado :dollar:: " + str(macaco4.dinheiro) + "\n", use_aliases = True))

	time.sleep(2)