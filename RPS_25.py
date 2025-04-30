import random

choices = (
	(
		'rock',
		# Beats:
		(
			(' shades ', 'sun', ''),
			(' pounds out ', 'fire', ''),
			(' crushes ', 'scissors', ''),
			(' chips ', 'axe', ''),
			(' crushes ', 'snake', ''),
			(' crushes ', 'monkey', ''),
			(' crushes ', 'woman', ''),
			(' crushes ', 'man', ''),
			(' blocks ', 'tree', ' roots'),
			(' squishes ', 'cockroach', ''),
			(' crushes ', 'wolf', ''),
			(' crushes ', 'sponge', '')
		),
		# Loses
		('paper', 'moon', 'air', 'bowl', 'water', 'alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun')
	),
	(
		'sun',
		# Beats:
		(
			(' made of ', 'fire', ''),
			(' melts ', 'scissors', ''),
			(' melts ', 'axe', ''),
			(' warms ', 'snake', ''),
			(' warms ', 'monkey', ''),
			(' warms ', 'woman', ''),
			(' warms ', 'man', ''),
			(' feeds ', 'tree', ''),
			(' warms ', 'cockroach', ''),
			(' warms ', 'wolf', ''),
			(' dries up ', 'sponge', ''),
			(' shines through ', 'paper', '')
		),
		# Loses
		('moon', 'air', 'bowl', 'water', 'alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock')
	),
	(
		'fire',
		# Beats
		(
			(' melts ', 'scissors', ''),
			(' forges ', 'axe', ''),
			(' burns ', 'snake', ''),
			(' burns ', 'monkey', ''),
			(' burns ', 'woman', ''),
			(' burns ', 'man', ''),
			(' burns down ', 'tree', ''),
			(' burns ', 'cockroach', ''),
			(' burns ', 'wolf', ''),
			(' burns ', 'sponge', ''),
			(' burns ', 'paper', ''),
			(' : campfire by ', 'moon', ' light')
 		),
		# Loses
		('air', 'bowl', 'water', 'alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock', 'sun')
	),
	(
		'scissors',
		# Beats
		(
			(' are sharper than ', 'axe', ''),
			(' cut ', 'snake', ''),
			(' cut ', 'monkey', ''),
			(' cut ', 'woman', ''),
			(' cut ', 'man', ''),
			(' carve ', 'tree', ''),
			(' cut ', 'cockroach', ''),
			(' cut ', 'wolf', ''),
			(' cut ', 'sponge', ''),
			(' cut ', 'paper', ''),
			(' reflect ', 'moon', ''),
			(' swish through ', 'air', '')
		),
		# Loses
		('bowl', 'water', 'alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock', 'sun', 'fire')
	),
	(
		'axe',
		# Beats
		(
			(' chops ', 'snake', ''),
			(' cleaves ', 'monkey', ''),
			(' cleaves ', 'woman', ''),
			(' cleaves ', 'man', ''),
			(' chops down ', 'tree', ''),
			(' chops ', 'cockroach', ''),
			(' cleaves ', 'wolf', ''),
			(' chops ', 'sponge', ''),
			(' slices ', 'paper', ''),
			(' reflects ', 'moon', ''),
			(' flies through ', 'air', ''),
			(' chops ', 'bowl', '')
		),
		# Loses
		('water', 'alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock', 'sun', 'fire', 'scissors')
	),
	(
		'snake',
		# Beats
		(
			(' bites ', 'monkey', ''),
			(' bites ', 'woman', ''),
			(' bites ', 'man', ''),
			(' nests in ', 'tree', ''),
			(' eats ', 'cockroach', ''),
			(' bites ', 'wolf', ''),
			(' swallows ', 'sponge', ''),
			(' nests in ', 'paper', ''),
			(' is nocturnal with ', 'moon', ''),
			(' breathes ', 'air', ''),
			(' sleeps in ', 'bowl', ''),
			(' drinks ', 'water', '')
		),
		# Loses
		('alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock', 'sun', 'fire', 'scissors', 'axe')
	),
	(
		'monkey',
		# Beats
		(
			(' flings poop at ', 'woman', ''),
			(' flings poop at ', 'man', ''),
			(' lives in ', 'tree', ''),
			(' eats ', 'cockroach', ''),
			(' enrages ', 'wolf', ''),
			(' crips up ', 'sponge', ''),
			(' rips up ', 'paper', ''),
			(' screeches at ', 'moon', ''),
			(' breathes ', 'air', ''),
			(' smashes ', 'bowl', ''),
			(' drinks ', 'water', ''),
			(' infuriates ', 'alien', '')
		),
		# Loses
		('dragon', 'devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock', 'sun', 'fire', 'scissors', 'axe', 'snake')
	),
	(
		'woman',
		# Beats
		(
			(' tempts ', 'man', ''),
			(' plants ', 'tree', ''),
			(' steps on ', 'cockroach', ''),
			(' tames ', 'wolf', ''),
			(' cleans with ', 'sponge', ''),
			(' aligns with ', 'moon', ''),
			(' writes ', 'paper', ''),
			(' breathes ', 'air', ''),
			(' eats from ', 'bowl', ''),
			(' drinks ', 'water', ''),
			(' disproves ', 'alien', ''),
			(' subdues ', 'dragon', '')
		),
		# Loses
		('devil', 'lightning', 'nuke', 'dynamite', 'gun', 'rock', 'sun', 'fire', 'scissors', 'axe', 'snake', 'monkey')
	),
	(
		'man',
		# Beats
		(
			(' plants ', 'tree', ''),
			(' steps on ', 'cockroach', ''),
			(' tames ', 'wolf', ''),
			(' cleans with ', 'sponge', ''),
			(' writes ', 'paper', ''),
			(' travels to ', 'moon', ''),
			(' breathes ', 'air', ''),
			(' eats from ', 'bowl', ''),
			(' drinks ', 'water', ''),
			(' disproves ', 'alien', ''),
			(' slays ', 'dragon', ''),
			(' exorcises ', 'devil', '')
		),
		# Loses
		('lightning', 'nuke', 'dynamite', 'gun', 'rock', 'sun', 'fire', 'scissors', 'axe', 'snake', 'monkey', 'woman')
	),
	(
		'tree',
		# Beats
		(
			(' shelters ', 'cockroach', ''),
			(' shelters ', 'wolf', ''),
			(' outlives ', 'sponge', ''),
			(' creates ', 'paper', ''),
			(' blocks ', 'moon', ''),
			(' produces ', 'air', ''),
			(' creates ', 'bowl', ''),
			(' drinks ', 'water', ''),
			(' ensnares ', 'alien', '\'s ship'),
			(' shelters ', 'dragon', ''),
			(' imprisons ', 'devil', ''),
			(' attracts ', 'lightning', '')
		),
		# Loses
		('nuke', 'dynamite', 'gun', 'rock', 'sun', 'fire', 'scissors', 'axe', 'snake', 'monkey', 'woman', 'man')
	),
	(
		'cockroach',
		# Beats
		(
			(' sleeps in fur of ', 'wolf', ''),
			(' nests in ', 'sponge', ''),
			(' nests between ', 'paper', ''),
			(' nocturnal with ', 'moon', ''),
			(' breathes ', 'air', ''),
			(' hides under ', 'bowl', ''),
			(' drinks ', 'water', ''),
			(' stows away with ', 'alien', ''),
			(' eats eggs of ', 'dragon', ''),
			(' makes man a ', 'devil', ''),
			(' hides from ', 'lightning', ''),
			(' survives ', 'nuke', '')
		),
		# Loses
		('dynamite', 'gun', 'rock', 'sun', 'fire', 'scissors', 'axe', 'snake', 'monkey', 'woman', 'man', 'tree')
	),
	(
		'wolf',
		# Beats
		(
			(' chews up ', 'sponge', ''),
			(' chews up ', 'paper', ''),
			(' howls at ', 'moon', ''),
			(' breathes ', 'air', ''),
			(' drinks from ', 'bowl', ''),
			(' drinks ', 'water', ''),
			(' chases ', 'alien', ''),
			(' outruns ', 'dragon', ''),
			(' bites heiny of ', 'devil', ''),
			(' outruns ', 'lightning', ''),
			(': "WOLF-2" launches ', 'nuke', ''),
			(' outruns ', 'dynamite', '')
		),
		# Loses
		('gun', 'rock', 'sun', 'fire', 'scissors', 'axe', 'snake', 'monkey', 'woman', 'man', 'tree', 'cockroach')
	),
	(
		'sponge',
		# Beats
		(
			(' soaks ', 'paper', ''),
			(' looks like ', 'moon', ''),
			(' uses ', 'air', ' pockets'),
			(' cleans ', 'bowl', ''),
			(' absorbs ', 'water', ''),
			(' intrigues ', 'alien', ''),
			(' cleanses ', 'dragon', ''),
			(' cleanses ', 'devil', ''),
			(' conducts ', 'lightning', ''),
			(' cleans ', 'nuke', ''),
			(' soaks ', 'dynamite', ''),
			(' cleans ', 'gun', '')
		),
		# Loses
		('rock', 'sun', 'fire', 'scissors', 'axe', 'snake', 'monkey', 'woman', 'man', 'tree', 'cockroach', 'wolf')
	),
	(
		'paper',
		# Beats
		(
			(' ', 'moon', ''),
			(' fans ', 'air', ''),
			(' mache ', 'bowl', ''),
			(' floats on ', 'water', ''),
			(' disproves ', 'alien', ''),
			(' rebukes ', 'dragon', ''),
			(' rebukes ', 'devil', ''),
			(' defines ', 'lightning', ''),
			(' defines ', 'nuke', ''),
			(' encases ', 'dynamite', ''),
			(' outlaws ', 'gun', ''),
			(' covers ', 'rock', '')
		),
		# Loses
		('sun', 'fire', 'scissors', 'axe', 'snake', 'monkey', 'woman', 'man', 'tree', 'cockroach', 'wolf', 'sponge')
	),
	(
		'moon',
		# Beats
		(
			(' has no ', 'air', ''),
			(' shaped like ', 'bowl', ''),
			(' has no ', 'water', ''),
			(' houses ', 'alien', ''),
			(' shines on ', 'dragon', ''),
			(' terrifies ', 'devil', ''),
			(' far above ', 'lightning', ''),
			(' too far for ', 'nuke', ''),
			(' suffocates ', 'dynamite', ''),
			('shine ', 'gun', 'fight'),
			(' shines on ', 'rock', ''),
			(' eclipses ', 'sun', '')
		),
		# Loses
		('fire', 'scissors', 'axe', 'snake', 'monkey', 'woman', 'man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper')
	),
	(
		'air',
		# Beats
		(
			(' tips over ', 'bowl', ''),
			(' evaporates ', 'water', ''),
			(' chokes ', 'alien', ''),
			(' freezes ', 'dragon', ''),
			(' chokes ', 'devil', ''),
			(' creates ', 'lightning', ''),
			(' blows astray ', 'nuke', ''),
			(' blows out ', 'dynamite', ''),
			(' tarnishes ', 'gun', ''),
			(' erodes ', 'rock', ''),
			(' cools heat of ', 'sun', ''),
			(' blows out ', 'fire', '')
		),
		# Loses
		('scissors', 'axe', 'snake', 'monkey', 'woman', ', man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon')
	),
	(
		'bowl',
		# Beats
		(
			(' contains ', 'water', ''),
			(' shapes craft of ', 'alien', ''),
			(' drowns ', 'dragon', ''),
			(' blesses ', 'devil', ''),
			(' focuses ', 'lightning', ''),
			(' encases core of ', 'nuke', ''),
			(' splashes ', 'dynamite', ''),
			(' splashes ', 'gun', ''),
			(' once made of ', 'rock', ''),
			(' focuses ', 'sun', ''),
			(' snuffs out ', 'fire', ''),
			(' covers ', 'scissors', '')
		),
		# Loses
		('axe', 'snake', 'monkey', 'woman', ', man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air')
	),
	(
		'water',
		# Beats
		(
			(' toxic to ', 'alien', ''),
			(' drowns ', 'dragon', ''),
			(' blesses ', 'devil', ''),
			(' conducts ', 'lightning', ''),
			(' shot-circuits ', 'nuke', ''),
			(' douses ', 'dynamite', ''),
			(' rusts ', 'gun', ''),
			(' erodes ', 'rock', ''),
			(' reflects ', 'sun', ''),
			(' puts out ', 'fire', ''),
			(' rusts ', 'scissors', ''),
			(' rusts ', 'axe', '')
		),
		# Loses
		('snake', 'monkey', 'woman', 'man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air', 'bowl')
	),
	(
		'alien',
		# Beats
		(
			(' vaporizes ', 'dragon', ''),
			(' non-believer in ', 'devil', ''),
			(' shoots' , 'lightning', ''),
			(' defuses ', 'nuke', ''),
			(' defuses ', 'dynamite', ''),
			(' force-fields ', 'gun', ''),
			(' vaporizes ', 'rock', ''),
			(' destroys ', 'sun', ''),
			(' fuses ', 'fire', ''),
			(' force-fields ', 'scissors', ''),
			(' force-fields ', 'axe', ''),
			(' mutates ', 'snake', '')
		),
		# Loses
		('monkey', 'woman', 'man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air', 'bowl', 'water')
	),
	(
		'dragon',
		# Beats
		(
			(' commands ', 'devil', ''),
			(' breathes ', 'lightning', ''),
			(' lived before ', 'nukes', ''),
			(' flosses with ', 'dynamite', ''),
			(' is immune to ', 'gun', ''),
			(' blots out ', 'sun', ''),
			(' rests upon ', 'rock', ''),
			(' breathes ', 'fire', ''),
			(' is immune to ', 'scissors', ''),
			(' immunde to ', 'axe', ''),
			(' spawns ', 'snake', ''),
			(' chars ', 'monkey', '')
		),
		# Loses
		('woman', 'man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air', 'bowl', 'water', 'alien')
	),
	(
		'devil',
		# Beats
		(
			(' casts ', 'lightning', ''),
			(' inspires ', 'nuke', ''),
			(' inspires ', 'dynamite', ''),
			(' inspires ', 'gun', ''),
			(' hurls ', 'rock', ''),
			(' curses ', 'sun', ''),
			(' breathes ', 'fire', ''),
			(' is immune to ', 'scissors', ''),
			(' is immune to ', 'axe', ''),
			(' eats ', 'snake', ''),
			(' enrages ', 'monkey', ''),
			(' tempts ', 'woman', '')
		),
		# Loses
		('man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air', 'bowl', 'water', 'alien', 'dragon')
	),
	(
		'lightning',
		# Beats
		(
			(' diffuses ', 'nuke', ''),
			(' ignites ', 'dynamite', ''),
			(' melts ', 'gun', ''),
			(' splits ', 'rock', ''),
			(' storm blocks ', 'sun', ''),
			(' starts ', 'fire', ''),
			(' melts ', 'scissors', ''),
			(' melts ', 'axe', ''),
			(' strikes ', 'snake', ''),
			(' strikes ', 'monkey', ''),
			(' strikes ', 'woman', ''),
			(' strikes ', 'man', '')
		),
		# Loses
		('tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air', 'bowl', 'water', 'alien', 'dragon', 'devil')
	),
	(
		'nuke',
		# Beats
		(
			(' outclasses ', 'dynamite', ''),
			(' outclasses ', 'gun', ''),
			(' incinerates ', 'rock', ''),
			(' has powers of ', 'sun', ''),
			(' starts massive ', 'fire', ''),
			(' incinerates ', 'scissors', ''),
			(' incinerates ', 'axe', ''),
			(' incinerates ', 'snake', ''),
			(' incinerates ', 'monkey', ''),
			(' incinerates ', 'woman', ''),
			(' incinerates ', 'man', ''),
			(' incinerates ', 'tree', '')
		),
		# Loses
		('cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air', 'bowl', 'water', 'alien', 'dragon', 'devil', 'lightning')
	),
	(
		'dynamite',
		# Beats
		(
			(' outclasses ', 'gun', ''),
			(' explodes ', 'rock', ''),
			(' smoke blocks out ', 'sun', ''),
			(' starts ', 'fire', ''),
			(' explodes ', 'scissors', ''),
			(' explodes ', 'axe', ''),
			(' explodes ', 'snake', ''),
			(' explodes ', 'monkey', ''),
			(' explodes ', 'woman', ''),
			(' explodes ', 'man', ''),
			(' explodes ', 'tree', ''),
			(' explodes ', 'cockroach', '')
		),
		# Loses
		('wolf', 'sponge', 'paper', 'moon', 'air', 'bowl', 'water', 'alien', 'dragon', 'devil', 'lightning', 'nuke')
	),
	(
		'gun',
		# Beats
		(
			(' targets ', 'rock', ''),
			(' shoots at ', 'sun', ''),
			('  ', 'fire', 's'),
			(' destroys ', 'scissors', ''),
			(' chips ', 'axe', ''),
			(' shoots ', 'snake', ''),
			(' shoots ',  'monkey', ''),
			(' shoots ', 'woman', ''),
			(' shoots ', 'man', ''),
			(' targets ', 'tree', ''),
			(' shoots ', 'cockroach', ''),
			(' shoots ', 'wolf', '')
		),
		# Loses
		('sponge', 'paper', 'moon', 'air', 'bowl', 'water', 'alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite')
	)
)


def game_loop():
	my_error = 'error'
	while my_error == 'error':
		current_choices = get_choice()
		is_win = check_win(*current_choices)
		my_error = is_win
	print(f'{is_win[0]}\nComputer chose: {choices[current_choices[1]][0]}\nYou chose: {current_choices[0]}\n')
	print_defeat(is_win, choices[current_choices[1]][0], current_choices[0])
	play_again()


def get_choice():
	print('\n\nChoices:')
	print(', '.join(choices[i][0] for i in range(25)))

	computer_choice = random.randint(0, 24)
	my_choice = input('\nWhat do you choose?\n\n	')
	return [my_choice.lower(), computer_choice]

def check_win(my_choice, computer_choice):
	win = my_choice in choices[computer_choice][2]
	lose = any(my_choice in sublist for sublist in choices[computer_choice][1])
	tie = my_choice == choices[computer_choice][0]
	print('\n')
	my_idx = 0
	for i in range(0, 25):
		if my_choice in choices[i]:
			my_idx = i
			break
	if win:
		idx = get_index(my_idx, choices[computer_choice][0])
		return ['Win!', my_choice, choices[my_idx][1][idx]]
	elif lose:
		idx = get_index(computer_choice, my_choice)
		return ['Lose!', choices[computer_choice][0], choices[computer_choice][1][idx]]
	elif tie:
		return ['Tie!']
	else:
		print('Choice not found!\n(Try all lowercase letters)')
		return 'error'
	
def get_index(strt_idx, choice):
	for k in range(0, 12):
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
		print(comp + winner[2][0] + player + winner[2][2], '\n')
	elif winner[1] == player:
		print(player + winner[2][0] + comp + winner[2][2], '\n')
	else:
		print('Some error occurred when printing the defeat statement.')

		
	
game_loop()
