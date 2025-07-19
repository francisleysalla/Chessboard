import logging
logging.basicConfig(filename='0 - Practice/Chessboard/debug_chessboard.txt', filemode='a', level=logging.DEBUG, format='%(levelname)s - %(message)s')

def invalid_input(*args):
  logging.error('Invalid input received.')
  pass

def valid_notation(entry):
  notation = entry.replace('x','')
  if len(notation) == 4 and (notation[0] not in 'KQRBN' or notation[1] not in 'abcdefgh12345678'):
      logging.debug(f'Invalid chess notation: {entry}')
      return False
  if len(notation) == 3 and notation[0] not in 'KQBNRabcdefgh':
    logging.debug(f'Invalid chess notation: {entry}')
    return False
  if notation[-1] not in '12345678' or notation[-2] not in 'abcdefgh':
    logging.debug(f'Invalid chess notation: {entry}')
    return False
  return True

def pawn_move(resp, board, turn):
  logging.info('Pawn move function called.')
  # check if it is a valid chess notation and a valid pawn move
  if valid_notation(resp):
    pass
  else:
    invalid_input()


def piece_move(resp, board, turn):
  logging.info('Piece move function called.')
  if valid_notation(resp.captalize()):
    pass
  else:
    invalid_input()

def capture_or_disambiguate(resp, board, turn):
  logging.info('Capture or disambiguate function called.')
  if valid_notation(resp.captalize()):
    pass
  else:
    invalid_input()

def capture_with_disambiguation(resp, board, turn):
  logging.info('Capture with disambiguation function called.')
  if valid_notation(resp.captalize()):
    pass
  else:
    invalid_input()