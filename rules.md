# Rules of Fireball 2.0
## Win Condition
- Both players have three lives.
- What beats what:
  - **Fireball** beats **charge**.
  - **Waterball** beats **fireball**.
  - **Waterball** beats **charge**.
  - **Fireball** or **waterball** beats **gain a life** (and no life is gained, it just acts as a **charge**.)
  

## Possible Actions 
1. **Fireball:** Costs 1 charge. Takes 1 life.
2. **Waterball:** Costs 2 charges. Takes 1 life.
3. **Gain a life:** Costs 2 charges, gives you 1 life.
4. **Spirit Bomb:** Costs 3 charges. Takes 2 lives, but can be countered by fireball. If countered, lose 1 lives. 
5. **Charge:** Gives you 1 charge to use on waterball or fireball.
6. **Shield:** Blocks fireball or waterball. Cannot be done more than three times in a row.

## Computer Strategy
The computer can be in five possible states:

1. 0 charges. 
2. 1 charge.
3. 2 charge.
4. 3 charge.
5. 4+ charges.

There is a "sub-state" for each of these -- when the computer has shielded more than 3 times.

For each of the modes, we'll have to decide what the comptuter does in all of the states. That'll decide the complete strategy of the computer.

### Easy Mode
- 0 charge.
  - Charge (100%).
  - Block (0%).
- 1 charge.
  - Fireball (50%).
  - Charge (40%).
  - Block (10%).
- 2 charge.
  - Fireball (20%).
  - Charge (10%).
  - Block (10%).
  - Waterball (50%).
  - Gain life (10%).
- 3 charge.
  - Fireball (10%).
  - Charge (10%).
  - Block (0%).
  - Waterball (10%).
  - Gain life (10%).
  - Spirit Bomb (60%).
- 4+ charge.
  - Fireball (10%).
  - Charge (10%).
  - Block (20%).
  - Waterball (10%).
  - Gain life (0%).
  - Spirit Bomb (50%).
- 3 block strategy:
  - Block is 0% but reweight the other stuff.

### Normal Mode
- 0 charge.
  - Charge (100%).
  - Block (0%).
- 1 charge.
  - Fireball (30%).
  - Charge (45%).
  - Block (25%).
- 2 charge.
  - Fireball (15%).
  - Charge (30%).
  - Block (20%).
  - Waterball (25%).
  - Gain life (10%).
- 3 charge.
  - Fireball (10%).
  - Charge (15%).
  - Block (25%).
  - Waterball (10%).
  - Gain life (0%).
  - Spirit Bomb (40%).
- 4+ charge.
  - Fireball (0%).
  - Charge (0%).
  - Block (0%).
  - Waterball (0%).
  - Gain life (80%).
  - Spirit Bomb (20%).
- 3 block strategy:
  - Block is 0% but reweight the other stuff.

### Aggressive Mode
- 0 charge.
  - Charge (100%).
  - Block (0%).
- 1 charge.
  - Fireball (75%).
  - Charge (25%).
  - Block (0%).
- 2 charge.
  - Fireball (15%).
  - Charge (20%).
  - Block (5%).
  - Waterball (60%).
  - Gain life (0%).
- 3 charge.
  - Fireball (15%).
  - Charge (15%).
  - Block (0%).
  - Waterball (15%).
  - Gain life (10%).
  - Spirit Bomb (45%).
- 4+ charge.
  - Fireball (10%).
  - Charge (5%).
  - Block (5%).
  - Waterball (15%).
  - Gain life (15%).
  - Spirit Bomb (50%).
- 3 block strategy:
  - Block is 0% but reweight the other stuff.

### Defensive Mode
- 0 charge.
  - Charge (100%).
  - Block (0%).
- 1 charge.
  - Fireball (25%).
  - Charge (25%).
  - Block (50%).
- 2 charge.
  - Fireball (10%).
  - Charge (35%).
  - Block (40%).
  - Waterball (15%).
  - Gain life (0%).
- 3 charge.
  - Fireball (0%).
  - Charge (25%).
  - Block (50%).
  - Waterball (0%).
  - Gain life (0%).
  - Spirit Bomb (25%).
- 4+ charge.
  - Fireball (5%).
  - Charge (15%).
  - Block (60%).
  - Waterball (5%).
  - Gain life (10%).
  - Spirit Bomb (5%).
- 3 block strategy:
  - Block is 0% but reweight the other stuff.

### Challenge Mode
Gives the player 1 life, while computer still has 3 lives. 

- 0 charge.
  - Charge (100%).
  - Block (0%).
- 1 charge.
  - Fireball (20%).
  - Charge (50%).
  - Block (30%).
- 2 charge.
  - Fireball (20%).
  - Charge (25%).
  - Block (30%).
  - Waterball (25%).
  - Gain life (0%).
- 3 charge.
  - Fireball (10%).
  - Charge (20%).
  - Block (10%).
  - Waterball (10%).
  - Gain life (20%).
  - Spirit Bomb (30%).
- 4+ charge.
  - Fireball (50%).
  - Charge (10%).
  - Block (20%).
  - Waterball (10%).
  - Gain life (0%).
  - Spirit Bomb (10%).
- 3 block strategy:
  - Block is 0% but reweight the other stuff.
  
## Programming/Game Details
What programming concepts will we need to design this game?

1. **Lists:** We need this to store all the possible moves.
2. **Input:** Takes the user input, and stores it in a variable depending on what the user types in the keyboard.
3. **While Loop:** We want the game to keep on going until somebody loses.
4. **If/Else Statements:** To check what moves beat what moves.
5. **Functions:** Didn't go over this yet, but these allow us to package multiple lines of code into one line.

What will the overall program look like/what's the plan?

1. Figure out how to program a single turn. 
2. Figure out how to store/memorize states over multiple turns. Two things we need to keep track of:
    1. Charges
    2. Blocks
    3. Lives
3. Extend the game to keep going over multiple turns (using loops).
4. Add the computer player's different strategies. 
5. Allow for randomization.
