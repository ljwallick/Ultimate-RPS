import random

choices = [
	[
		'rock',
		# Beats:
		[['pounds out', 'fire'], ['crushes', 'scissors'], ['crushes', 'human'], ['crushes', 'sponge']],
		# Loses
		['paper', 'air', 'water', 'gun']
	],
	[
		'fire',
		# Beats
		[['melts', 'scissors'], ['burns', 'human'], ['burns', 'sponge'], ['burns', 'paper']],
		# Loses
		['air', 'water', 'gun', 'rock']
	],
	[
		'scissors',
		# Beats
		[['cut', 'human'], ['cut', 'sponge'], ['cut', 'paper'], ['swish through', 'air']],
		# Loses
		['water', 'gun', 'rock', 'fire']
	],
	[
		'human',
		# Beats
		[['cleans with', 'sponge'], ['writes', 'paper'], ['breathes', 'air'], ['drinks', 'water']],
		# Loses
		['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake']
	],
	[
		'sponge',
		# Beats
		[['soaks', 'paper'], ['uses pockets of', 'air'], ['absorbs', 'water'], ['cleans', 'gun']],
		# Loses
		['rock', 'fire', 'scissors''human']
	],
	[
		'paper',
		# Beats
		[['fans', 'air'], ['covers', 'water'], ['outlaws', 'gun'], ['covers', 'rock']],
		# Loses
		['fire', 'scissors', 'human', 'sponge']
	],
	[
		'air',
		# Beats
		[['evaporates', 'water'], ['tarnishes', 'gun'], ['erodes', 'rock'], ['blows out', 'fire']],
		# Loses
		['scissors', 'human', 'sponge', 'paper']
	],
	[
		'water',
		# Beats
		[['rusts', 'gun'], ['erodes', 'rock'], ['puts out', 'fire'], ['rusts', 'scissors']],
		# Loses
		['human', 'sponge', 'paper', 'air']
	],
	[
		'gun',
		# Beats
		[['targets', 'rock'], ['targets', 'fire'], ['outclasses', 'scissors'], ['shoots', 'human']],
		# Loses
		['sponge', 'paper', 'air', 'water']
	]
]


def game_loop():
	my_error = 'error'
	while my_error == 'error':
		current_choices = get_choice()
		is_win = check_win(*current_choices)
		my_error = is_win
	print(f'{is_win[0]}\nComputer chose: {choices[current_choices[1]][0]}\nYou chose:  {current_choices[0]}\n')
	print_defeat(is_win, choices[current_choices[1]][0], current_choices[0])
	play_again()


def get_choice():
	print('\n\nChoices:')
	print(', '.join(choices[i][0] for i in range(9)))

	computer_choice = random.randint(0, 8)
	my_choice = input('\nWhat do you choose?\n\n    ')
	return [my_choice, computer_choice]

def check_win(my_choice, computer_choice):
	win = my_choice in choices[computer_choice][2]
	lose = any(my_choice in sublist for sublist in choices[computer_choice][1])
	tie = my_choice == choices[computer_choice][0]
	print('\n')
	my_idx = 0
	for i in range(0, 9):
		if my_choice in choices[i]:
			my_idx = i
			break
	if win:
		idx = get_index(my_idx, choices[computer_choice][0])
		return ['Win!', my_choice, choices[my_idx][1][idx][0]]
	elif lose:
		idx = get_index(computer_choice, my_choice)
		return ['Lose!', choices[computer_choice][0], choices[computer_choice][1][idx][0]]
	elif tie:
		return ['Tie!']
	else:
		print('Choice not found!\n(Try all lowercase letters)')
		return 'error'
	
def get_index(strt_idx, choice):
	for k in range(0, 4):
		if choices[strt_idx][1][k][1] == choice:
			return k


def play_again():
	again = input('Do you want to play again? y/n\t')
	if again == 'y':
		game_loop()
	elif again == 'n':
		print('\nThank you for playing! Bu-bye!')
	else:
		print("Invalid choice. Please use 'y' or 'n'.\n")
		play_again()

def print_defeat(winner, comp, player):
	if len(winner) == 1:
		print(f"{comp} doesn't beat {player}, yet doesn't lose to {comp}.\n")
	elif winner[1] == comp:
		print(comp, winner[2], player, '\n')
	elif winner[1] == player:
		print(player, winner[2], comp, '\n')
	else:
		print('Some error occurred when printing the defeat statement.')

		
	
game_loop()
