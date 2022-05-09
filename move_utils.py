'''
move_utils.py
File containing all the functions that have to do with player moves or computer moves:
  1) check_valid_move
  2) renormalize
  3) computer_move
'''
import numpy as np
from numpy.random import choice

'''
check_valid_move
Checks if a player move is valid, depending on the rules of the game (costs for charges and blocks).
'''
def check_valid_move(player_move, player_charges, player_blocks):
  if player_charges == 0 and player_move == "f":
    print("You don't have enough charges for fireball! (You need" , str(1 - player_charges) , "more charges!)")
    return False
  if player_charges < 2 and player_move == "w":
    print("You don't have enough charges for waterball! (You need" , str(2 - player_charges) , "more charges!)")
    return False   
  if player_charges < 2 and player_move == "gl":
    print("You don't have enough charges for gain life! (You need" , str(2 - player_charges) , "more charges!)")
    return False 
  if player_charges < 3 and player_move == "sb":
    print("You don't have enough charges for Spirit Bomb! (You need" , str(3 - player_charges) , "more charges!)")
    return False  
  if player_blocks == 3 and player_move == "b": 
    print("Oops! You can only use three shields in a row!")
    return False
  return True

'''
renormalize
Used as a utility inside computer_move for renormalizing probabilities.
'''
def renormalize(p_list):
  p_list_arr = np.array(p_list)
  sum = np.sum(p_list)
  p_list_renorm = np.divide(p_list_arr, sum)
  return p_list_renorm

'''
computer_move
Used to decide what move the CPU does. This decides based on a probability distribution over the states. Player can choose what mode computer they want to play against.
'''
def computer_move(blocks, lives, charges, mode):
  POSSIBLE_MOVES = ["c", "b", "f", "w", "gl", "sb"]
  MODES = {
    "easy": [
      [1.0, 0, 0, 0, 0, 0],
      [0.4, 0.1, 0.5, 0, 0, 0],
      [0.1, 0.1, 0.2, 0.5, 0.1, 0],
      [0.1, 0, 0.1, 0.1, 0.1, 0.6], 
      [0.1, 0.2, 0.1, 0.1, 0, 0.5]
    ],
    "normal": [
      [1.0, 0, 0, 0, 0, 0],
      [0.45, 0.25, 0.3, 0, 0, 0],
      [0.3, 0.2, 0.15, 0.25, 0.1, 0],
      [0.15, 0.25, 0.1, 0.1, 0, 0.4],
      [0, 0, 0, 0, 0.8, 0.2],
    ],
    "aggressive": [
      [1.0, 0, 0, 0, 0, 0],
      [0.25, 0, 0.75, 0, 0, 0],
      [0.2, 0.05, 0.15, 0.6, 0, 0],
      [0.15, 0, 0.15, 0.15, 0.1, 0.45],
      [0.05, 0.05, 0.1, 0.15, 0.15, 0.5],
    ],
    "defensive": [
      [1.0, 0, 0, 0, 0, 0],
      [0.25, 0.5, 0.25, 0, 0, 0],
      [0.35, 0.4, 0.1, 0.15, 0, 0],
      [0.25, 0.5, 0, 0, 0, 0.25],
      [0.15, 0.6, 0.05, 0.05, 0.1, 0.05],
    ],
    "challenge": [
      [1.0, 0, 0, 0, 0, 0],
      [0.5, 0.3, 0.2, 0, 0, 0],
      [0.25, 0.3, 0.2, 0.25, 0, 0],
      [0.2, 0.1, 0.1, 0.1, 0.2, 0.3],
      [0.1, 0.2, 0.5, 0.1, 0, 0.1],
    ]
  }

  if charges == 0 and blocks < 3:
    return choice(POSSIBLE_MOVES, p=MODES[mode][0])
  elif charges == 0 and blocks >= 3:
    return choice(POSSIBLE_MOVES, p=renormalize(MODES[mode][0]))
  elif charges == 1 and blocks < 3:
    return choice(POSSIBLE_MOVES, p=MODES[mode][1])
  elif charges == 1 and blocks >= 3:
    return choice(POSSIBLE_MOVES, p=renormalize(MODES[mode][1]))

  elif charges == 2 and blocks < 3:
    return choice(POSSIBLE_MOVES, p=MODES[mode][2])
  elif charges == 2 and blocks >= 3:
    return choice(POSSIBLE_MOVES, p=renormalize(MODES[mode][2]))
    
  elif charges == 3 and blocks < 3:
    return choice(POSSIBLE_MOVES, p=MODES[mode][3])
  elif charges == 3 and blocks >= 3:
    return choice(POSSIBLE_MOVES, p=renormalize(MODES[mode][3]))
  
  elif charges > 3 and blocks < 3:
    return choice(POSSIBLE_MOVES, p=MODES[mode][4])
  elif charges == 3 and blocks >= 3:
    return choice(POSSIBLE_MOVES, p=renormalize(MODES[mode][4]))