import random
from os import system
import time
from cards import Card

#palavras para lembra

cartoes = Card()

while True:
	escolhe = random.choice(cartoes)
	
	print(escolhe[0])
	
	nome = input('traduzi:  ').lower()
	
	if nome == escolhe[1]:
		print('acertou')
		time.sleep(2.1)
		
		system('clear')
		continue
	
	else:
		print('errou')
		time.sleep(2.1)
		system('clear')
		continue
	
	
	