'''
update
This huge function implements all the rules of the game and resolves a turn for both the CPU and the player.
'''
def update(move, player_charges, player_blocks, player_lives, 
           cpu_move, cpu_charges, cpu_blocks, cpu_lives):
  # First, we need to update the block counts
  if move == "b":
    player_blocks += 1
  else:
    player_blocks = 0
    
  if cpu_move == "b":
    cpu_blocks += 1
  else:
    cpu_blocks = 0

  # Resolve everything else (not about blocks)
  if move == "c" and cpu_move == "c":
    player_charges += 1
    cpu_charges += 1
  elif move == "c" and cpu_move == "b": 
    player_charges += 1
  elif move == "c" and cpu_move == "f":
    player_lives -= 1
    player_charges += 1
    cpu_charges -= 1
  elif move == "c" and cpu_move == "w":
    player_lives -= 1
    player_charges += 1
    cpu_charges -= 2
  elif move == "c" and cpu_move == "gl":
    player_charges += 1
    cpu_charges -= 2
    cpu_lives += 1
  elif move == "c" and cpu_move == "sb":
    player_lives -= 2
    player_charges += 1
    cpu_charges -= 3
  elif move == "b" and cpu_move == "c":
    cpu_charges += 1
  elif move == "b" and cpu_move == "b":
    return player_lives, player_charges, player_blocks, cpu_lives, cpu_charges, cpu_blocks
  elif move == "b" and cpu_move == "f":
    cpu_charges -= 1
  elif move == "b" and cpu_move == "w":
    cpu_charges -= 2
  elif move == "b" and cpu_move == "gl":
    cpu_lives += 1
    cpu_charges -= 2
  elif move == "b" and cpu_move == "sb":
    player_lives -= 2
    cpu_charges -= 3
  elif move == "f" and cpu_move == "c":
    cpu_lives -= 1
    cpu_charges += 1
    player_charges -= 1
  elif move == "f" and cpu_move == "b":
    player_charges -= 1
  elif move == "f" and cpu_move == "f":
    cpu_charges -= 1
    player_charges -= 1
  elif move == "f" and cpu_move == "w":
    player_lives -= 1
    cpu_charges -= 2
    player_charges -= 1
  elif move == "f" and cpu_move == "gl":
    cpu_lives -= 1
    cpu_charges -= 2
    player_charges -= 1
  elif move == "f" and cpu_move == "sb":
    cpu_lives -= 1
    cpu_charges -= 3
    player_charges -= 1
  elif move == "w" and cpu_move == "c":
    cpu_lives -= 1
    cpu_charges += 1
    player_charges -= 2
  elif move == "w" and cpu_move == "b":
    player_charges -= 2
  elif move == "w" and cpu_move == "f":
    cpu_lives -= 1
    cpu_charges -= 1
    player_charges -= 2
  elif move == "w" and cpu_move == "w":
    cpu_charges -= 2
    player_charges -= 2
  elif move == "w" and cpu_move == "gl":
    cpu_lives -= 1
    cpu_charges -= 2
    player_charges -= 2
  elif move == "w" and cpu_move == "sb":
    player_lives -= 2
    cpu_charges -= 3
    player_charges -= 2
  elif move == "gl" and cpu_move == "c":
    player_lives += 1
    cpu_charges += 1
    player_charges -= 2
  elif move == "gl" and cpu_move == "b":
    player_lives += 1
    player_charges -= 2
  elif move == "gl" and cpu_move == "f":
    player_lives -= 1
    cpu_charges -= 1
    player_charges -= 2
  elif move == "gl" and cpu_move == "w":
    player_lives -= 1
    cpu_charges -= 2
    player_charges -= 2
  elif move == "gl" and cpu_move == "gl":
    player_lives += 1
    cpu_lives += 1
    cpu_charges -= 2
    player_charges -= 2
  elif move == "gl" and cpu_move == "sb":
    player_lives -= 2
    cpu_charges -= 3
    player_charges -= 2
  elif move == "sb" and cpu_move == "c":
    cpu_lives -= 2
    cpu_charges += 1
    player_charges -= 3
  elif move == "sb" and cpu_move == "b":
    cpu_lives -= 2
    player_charges -= 3
  elif move == "sb" and cpu_move == "f":
    player_lives -= 1
    cpu_charges -= 1
    player_charges -= 3
  elif move == "sb" and cpu_move == "w":
    cpu_lives -= 2
    cpu_charges -= 2
    player_charges -= 3
  elif move == "sb" and cpu_move == "gl":
    cpu_lives -= 2
    cpu_charges -= 2
    player_charges -= 3
  elif move == "sb" and cpu_move == "sb":
    cpu_charges -= 3
    player_charges -= 3
  return player_lives, player_charges, player_blocks, cpu_lives, cpu_charges, cpu_blocks