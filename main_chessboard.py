## This is a chessboard simulation that enforces simple piece movement rules. Checks, pins, castling and other advanced rules are not implemented.

from re import S
from sys import exit
from print_chessboard import *
from move_functions import *
import logging, os, copy
logging.basicConfig(filename='0 - Practice/Chessboard/debug_chessboard.txt', filemode='w', level=logging.INFO, format='%(levelname)s - %(message)s')

# Defining functions
def new_game():
  logging.info('New game started.')
  global turn, chessboard
  turn, chessboard = 'w', STARTING_PIECES.copy()
  os.system('cls')

def quitting():
  logging.info('Game ended by user.')
  print('Thanks for playing!')
  exit()

def get_help():
  # Not fully implemented
  logging.info('Help requested.')

def actions(r, *args):
  logging.debug('Actions function called.')
  {'q': quitting, 'h': get_help, 'n': new_game, 'r': new_game}.get(r.lower(), invalid_input)()

# Initializing varibles
turn = 'w'
chessboard = new_game()
commands = {
  1: actions,
  2: pawn_move,
  3: piece_move,
  4: capture_or_disambiguate,
  5: capture_with_disambiguation
}

# Main game Loop
while True:
  print_chessboard(chessboard)
  response = input('White move: ' if turn == 'w' else "Black move: ").lower()

  # Calling the right function
  try:
    commands.get(len(response),invalid_input)(response, chessboard, turn)
  except:
    raise


  # pawn moves: 2 letters
  # Piece move: 3 letters
  # Capture or disambiguate: 4 letters
  # Capture with disambiguation: 5 letters


# List of thing to do:
# invalid_input function - Raise an exception?
# get_help function - Show help text