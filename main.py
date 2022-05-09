from move_utils import check_valid_move
from move_utils import computer_move
from update_state import update

playagain = True
POSSIBLE_MOVES = ["c", "b", "f", "w", "gl", "sb"]

# Let's have a section that states the rules
print("======== RULES ========")
print("c is charge")
print("b is block")
print("f is fireball (1 charge)")
print("w is waterball (2 charges)")
print("gl is gain life (2 charges)")
print("sb is spirit bomb (3 charges)")
print("\n")
print("Fireball beats charge and spirit bomb.")
print("Waterball beats fireball and charge and gain life.")
print("Spirit Bomb beats everything except fireball.")
print("\n")

# Section for the player's turn, taking their input
while playagain == True:
  # Player chooses a mode out of the five to set the CPU to.
  mode_select = True
  while mode_select == True:
    selectmode = input("Please enter the number of the game mode you want to play. \n 1. easy \n 2. normal \n 3. aggressive \n 4. defensive \n 5. challenge \n - You play with one life \n")
    
    if selectmode == "1":
      modekey = "easy"
      mode_select = False
    elif selectmode == "2":
      modekey = "normal"
      mode_select = False
    elif selectmode == "3":
      modekey = "aggressive"
      mode_select = False
    elif selectmode == "4":
      modekey = "defensive"
      mode_select = False
    elif selectmode == "5":
      modekey = "challenge"
      mode_select = False
    else:
      print("")
      print("Please enter a valid mode type")
      modekey = "typo"
      mode_select = True

  # Game begins here -- initialize player and CPU state.
  turn_no = 1
  
  player_blocks = 0
  player_lives = 3
  if modekey == "challenge":
    player_lives = 1
  player_charges = 0
  
  cpu_blocks = 0
  cpu_lives = 3
  cpu_charges = 0

  # MAIN LOOP: CPU and player take a turn, state gets updated.
  while cpu_lives > 0 and player_lives > 0:
    print("===== TURN {} =====".format(turn_no))
    move = None
    player_turn = True
    while player_turn:
      move = input("Choose one of moves: c, b, f, w, gl, sb\n")
      if move not in POSSIBLE_MOVES: 
        print("Please enter a valid move.")
        continue
      if check_valid_move(move, player_charges, player_blocks) == True:
        player_turn = False
      
    print("You chose " + move + ".")
    cpu_move = computer_move(cpu_blocks, cpu_lives, cpu_charges, modekey)
    print("Computer chose " + cpu_move + ".")
    player_lives, player_charges, player_blocks, cpu_lives, cpu_charges, cpu_blocks = update(move, player_charges,                                                               player_blocks, player_lives,                                                        cpu_move, cpu_charges,                                                             cpu_blocks, cpu_lives)
    
    print("")
    print("Player Stats:")
    print("BLOCK COUNT =", player_blocks)
    print("LIFE COUNT =", player_lives)
    print("CHARGE COUNT =", player_charges)
    print("")
    print("CPU Stats:")
    print("BLOCK COUNT =", cpu_blocks)
    print("LIFE COUNT =", cpu_lives)
    print("CHARGE COUNT =", cpu_charges)
    print("")
    turn_no += 1

  # Decide the winner.
  if cpu_lives <= 0:
    print("You win!!!! :D")
  elif player_lives <= 0:
    print("You lose!!!! D:")

  # Replay the game if the player decides to.
  pagain = input("Press p to playagain and any other key to quit.")
  if pagain == "p":
    print("")
    print("------------------------")
    print("Restarting Game. . .")
    print("------------------------")
    playagain = True
    print("")    
  else:
    print("Thanks for playing!")
    playagain = False