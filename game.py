import os
import random

def display_board(board):
	'''
		Function for displaying the board
	'''
	print('\n\n')
	print('\t\t\t\t   |   |')
	print('\t\t\t\t ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
	print('\t\t\t\t   |   |')
	print('\t\t\t\t-----------')
	print('\t\t\t\t   |   |')
	print('\t\t\t\t ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
	print('\t\t\t\t   |   |')
	print('\t\t\t\t-----------')
	print('\t\t\t\t   |   |')
	print('\t\t\t\t ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
	print('\t\t\t\t   |   |')



def player_input():
	'''
		Function for setting markers of user
	'''
	marker1 = ''

	# Repeat until valid input
	while marker1 not in ['X','O']:
		marker1 = input("Player 1 choose your marker (X or O): ")

	if marker1 == 'X':
		marker2 = 'O'
	else:
		marker2 = 'X'

	return (marker1, marker2)



def place_marker(board, marker, position):
	'''
		Function to place marker on given position on board
	'''
	board[position-1] = marker



def win_check(board, mark):
	'''
		Function to check if the mark won or not
	'''	
	return ((board[6] == mark and board[7] == mark and board[8] == mark) or # across the top
    (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle
    (board[0] == mark and board[1] == mark and board[2] == mark) or # across the bottom
    (board[6] == mark and board[3] == mark and board[0] == mark) or # down the middle
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the right side
    (board[6] == mark and board[4] == mark and board[2] == mark) or # diagonal
    (board[8] == mark and board[4] == mark and board[0] == mark)) # diagonal



def choose_first():
	'''
		Function to choose which player will start the game
	'''		
	turn = random.randint(0, 1)
	
	if turn == 0:
		return "Player 1"
	else:
		return "Player 2"



def space_check(board, position):
	'''
		Checks whether board is empty at position
	'''			
	return board[position-1] == ' '



def full_board_check(board):
	'''
		Returns True if board is full
	'''
	for i in range(1,10):
		if space_check(board, i):
		    return False
	return True



def player_choice(board):
	'''
		Return valid input from player
	'''
	choice = int(input('Enter position(1-9):'))

	while choice < 1 or choice > 9 or  space_check(board, choice) == False:
		choice = int(input('Enter position(1-9):'))

	return choice



def replay():
	'''
		returns True if player want to play again or false if not
	'''		
	choice = input('Do you want to play agin(yes/no):')

	if choice.lower() == 'yes':
		return True
	else:
		return False





# Main script begins
os.system('reset')
print('Welcome to Tic Tac Toe!')
print('Written by Abhijeet Gurle')
print('Date Created: 15/08/2018\n\n')

while True:
	# set up the game
	board = [' '] * 9
	(marker1, marker2) = player_input()
	starting_player = choose_first()
	print(starting_player + " will start the game!")

	# Game begins
	while True:

		if starting_player == 'Player 1':
			os.system('clear')
			display_board(board)
			print("Player 1 turn:")
			position = player_choice(board)
			place_marker(board, marker1, position)
			
			if win_check(board, marker1):
				os.system('clear')
				display_board(board)
				print("Player 1 won!!!!")
				break
			starting_player = 'Player 2'	
		else:
			os.system('clear')
			display_board(board)
			print("Player 2 turn:")
			position = player_choice(board)
			place_marker(board, marker2, position)
			
			if win_check(board, marker2):
				os.system('clear')
				display_board(board)
				print("Player 2 won!!!!")
				break
			starting_player = 'Player 1'

		if full_board_check(board):
			os.system('clear')
			display_board(board)
			print("!!!! DRAW !!!!")
			break

	if not replay():
		break
	os.system('reset')				
