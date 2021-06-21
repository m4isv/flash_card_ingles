import random
from os import system
import time
system('clear')

def arte():
	print('''\n\t\t\033[1;32m
    ╔══╗╔╗─╔══╗╔══╗╔╗╔╗╔═╗╔══╗╔═╗╔══╗
    ║═╦╝║║─║╔╗║║══╣║╚╝║║╔╝║╔╗║║╬║╚╗╗║
    ║╔╝─║╚╗║╠╣║╠══║║╔╗║║╚╗║╠╣║║╗╣╔╩╝║
    ╚╝──╚═╝╚╝╚╝╚══╝╚╝╚╝╚═╝╚╝╚╝╚╩╝╚══╝\033[m''')


arte()

#palavras para lembra
cards = [
['he', 'ele'],
['she', 'ela'],
['it', 'isso'],
['thin', 'magro'],
['a snack', 'um lanche'],
['a lemon', 'um limao'],
['certo; direita', 'right'],
['é claro', 'of course'],
['ela é deslumbrante', "she's stunning"],
['meat', 'carne'],
["I don't like ", 'eu nao gosto'],
['oque', 'what'],
['coffee is delicious', 'cafe e delicioso'],
['awesom', 'incrivel'],
["I think it's cool", 'eu acho que isso e legal'],
['are you American?', 'voce e americano?']
]

roza = '\033[5;45m'
feixa = '\033[m'
verde = '\033[1;32m'
red = '\033[1;41m'

while True:
	escolhe = random.choice(cards)
	
	print(f'\n\n\t\t {roza}{escolhe[0]}{feixa}')
	
	nome = input(f'\n\t\t {verde}traduzi:{feixa}  ').lower()
	
	if nome == escolhe[1]:
		print(f'\t\t {verde}ACERTOU{feixa}')
		time.sleep(2.1)
		
		system('clear')
		arte()
		continue
	
	else:
		print(f'\t\t {red} ERROU {feixa} Certo e {verde}{escolhe[1]}{feixa}')
		time.sleep(2.1)
		system('clear')
		arte()
		continue
	
	
	
