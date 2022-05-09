# Fireball-2.0
My introductory Python project with Path Mentors. 

## Goal
My goal with this project was to learn introductory Python through implementing a game I've known since I was very small that I learned from my friends. The main finished product is a game that can be played on command line using just Python 3. The game allows the player to pick from five different modes and difficulties against a nondeterministic computer player. As a result, I learned basic Python programming and fundamentals.

The project was created on **replit.com**, a website that allows interactive pair programming with my mentor, Sam.

## Learning Outcomes
During this project, the main learning goal was to **get working understanding of the basics of Python 3 and programming in general.** We covered these topics:

1. **If/Else and Control Flow:** Learned how to use if/else statements to direct the flow of a program based on variables.
2. **Variables** Learned what a variable is, why it's necessary to store data in variables.
3. **Data Types:** Learned basic datatypes of Python: `string` is for words and characters, `int` is for numbers, and `boolean` for True/False.
4. **Logical Evaluation:** Learned how to use logical operators for True/False values when we needed to evaluate truth values.
5. **Loops:** Learned how to use *loops* to repeat program behavior; this allowed functionality like playing again and multiple turns.
6. **Functions:** Learned the basics of what a function is, why it's important in programming and in Python, and how to call functions.
7. **Lists:** Learne the basic data structure of lists, and why it's important to use lists to store data that should be collected together.
8. **User Input:** Learned how to take user input in a program; this was crucial because we were designing a game.
9. **External Libraries:** Learned how to import an external library's functions to use in our own program; we used `numpy` for some basic probability functionality.
10. **General Programming Practice:** Learned how to write good programs that people can read and interpret after their making.

## My Plan
Here was the rough plan we followed for implementing this game. 

1. **Made `rules.md`.** We created a file, `rules.md` that indicated the outline of how to play the game itself and what all the rules were. We needed this to be well-defined because that makes it much easier to program.
2. **Define computer strategies.** We wanted to make a game with *multiple* strategies for the computer, and we also didn't want the computer to be deterministic (completely predictable). Due to this, we made a probability distribution for each of the computer's moves at each turn based on a difficulty level. We made 5 difficulty levels.
3. **Setup the repl and `main.py`.** Did basic setup for the game by adding print statements, comments, and a plan in the comments for what we would be programming.
4. **Program a single turn.** Laid out the code for making sure a *single turn* of the game works, taking user input against a CPU that always does the same thing.
5. **Basic rules implemented.** Made a function `check_valid_move` that made sure that the rules were properly enforced in the game.
6. **Implemented update state function.** Implemented the (huge) function `update` that contains *all* the code for updating the state of the game after a turn from the CPU and the player. This contained every single possible combination of moves.
7. **Implemented the CPU move.** Allowed the CPU to move using randomness, introducing `numpy` and the `random.choice` external function so the CPU moves based on a probability distribution over its choices. Did this only for the EASY mode CPU first, then added the probabilities for the other 4 modes of difficulty.
8. **Loop so multiple turns could be played.** Made a `while` loop for the entire program and kept track of game state so the game keeps being played until either player loses. Multiple turns work now.
9. **Implemented win/lose logic and main menu.** We added a main menu that let the player choose which difficulty of CPU they wanted to play and finally added a section that decides the winner and loser. We also let the player choose to play again at the end of the game.
10. **Cleaned up the code, uploaded to GitHub.** Up until this point, we just used **replit.com** to do coding because it allows for interactive programming. At the end, we cleaned the code, splitting the functions into different files for cleaner code style, and uploaded it to GitHub.

## How to Play
To play, simply download the repository and use command line to run the `main.py` file. This is typically done with:

```
python3 main.py
```

Then, just follow the instructions onscreen and enjoy!

## Future Steps
**Sam:** For future steps, Lucas is qualified to move on to learn more advanced Python topics. He has a good grasp of basic control flow, while loops, functions, and basic coding practice. I think it would be good for Lucas to start learning object oriented programming through Python through another project as a next step, delving deeper into functions, classes (which we didn't cover), and drilling the basic fundamentals deeper. Lucas does a good job trying to figure out basic programming problems by himself, and is motivated to learn Python through projects and example. 
