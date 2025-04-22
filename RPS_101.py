import random
import requests
import shutil
import textwrap


choices = ['Dynamite', 'Tornado', 'Quicksand', 'Pit', 'Chain', 'Gun', 'Law', 'Whip', 'Sword', 'Rock', 'Death', 'Wall', 'Sun', 'Camera', 'Fire', 'Chainsaw', 'School', 
		   'Scissors', 'Poison', 'Cage', 'Axe', 'Peace', 'Computer', 'Castle', 'Snake', 'Blood', 'Porcupine', 'Vulture', 'Monkey', 'King', 'Queen', 'Prince', 'Princess', 
		   'Police', 'Woman', 'Baby', 'Man', 'Home', 'Train', 'Car', 'Noise', 'Bicycle', 'Tree', 'Turnip', 'Duck', 'Wolf', 'Cat', 'Bird', 'Fish', 'Spider', 'Cockroach', 
		   'Brain', 'Community', 'Cross', 'Money', 'Vampire', 'Sponge', 'Church', 'Butter', 'Book', 'Paper', 'Cloud', 'Airplane', 'Moon', 'Grass', 'Film', 'Toilet', 'Air', 
		   'Planet', 'Guitar', 'Bowl', 'Cup', 'Beer', 'Rain', 'Water', 'T.V.', 'Rainbow', 'U.F.O.', 'Alien', 'Prayer', 'Mountain', 'Satan', 'Dragon', 'Diamond', 'Platinum', 
		   'Gold', 'Devil', 'Fence', 'Video Game', 'Math', 'Robot', 'Heart', 'Electricity', 'Lightning', 'Medusa', 'Power', 'Laser', 'Nuke', 'Sky', 'Tank', 'Helicopter']

def game_loop():
	print_choices = ', '.join(choices)
	Continue = 'n'
	while Continue == 'n':
		print(f"\nChoices:\n  {textwrap.fill(print_choices, width=shutil.get_terminal_size().columns)}\n")
		my_choice = get_choice()
		if my_choice[0] != 'error':
			Continue = get_outcomes(my_choice[0])
			while Continue != 'y' and Continue != 'n' and Continue != '':
				print('\nError. Please use y/n')
				Continue = get_outcomes(my_choice[0])
		else:
			Continue = 'n'
	print_win(*my_choice)
	play_again()
		

def get_choice():
	string = input('What is your choice?\t')
	pattern = string.lower().replace('.','')
	ai = random.randint(0, 100)
	for choice in choices:
		if pattern == choice.lower().replace('.',''):
			return [choice, ai]
	print('\nChoice not found. Please select something from the list of items.')
	return ['error']
			

def create_string(List):
	new_list = [item[1] for item in List]
	return ', '.join(new_list)

def get_outcomes(my_choice):
	url_outcomes = f'https://rps101.pythonanywhere.com/api/v1/objects/{my_choice}'
	response = requests.get(url_outcomes)
	outcomes = response.json()
	winning = create_string(outcomes['winning outcomes'])
	return input(f'\n{my_choice} beats:\n  {textwrap.fill(winning, width=int(shutil.get_terminal_size().columns*.5))}.\n\nAre you Sure? y/n  ')

def print_win(obj1, obj2):
	url_result = f'https://rps101.pythonanywhere.com/api/v1/match?object_one={obj1}&object_two={choices[obj2]}'
	response = requests.get(url_result)
	result = response.json()
	if obj1 == result['winner']:
		print(f"\nWin!\n{result['winner']} {result['outcome']} {result['loser']}")
	elif choices[obj2] == result['winner']:
		print(f"\nLose...\n{result['winner']} {result['outcome']} {result['loser']}")
	elif obj1 == obj2 == result['winner']:
		print(f"Tie.\n{result['winner']} {result['outcome']} {result['loser']}")
	else:
		print(f'{result}\n{obj1}\n{obj2}')

def play_again():
	again = input('Do you want to play again? y/n\t')
	if again == 'y' or again == '':
		print('You said Yes')
		game_loop()
	elif again == 'n':
		return
	else:
		print('Error. Please use y/n\n')
		play_again()
		return
	
game_loop()