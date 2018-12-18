# Blokus Game Solver - California Polytechnic State University CPE Senior Project
Blokus AI Simulation Program  
Setup and Idea are based on this Final Project: https://github.com/mknapper1/Machine-Learning-Blokus  
**NOTE: This version is the code submitted for the Senior Project, the master branch has the most up-to-date version.**

## Project Goal
Study the different strategies that can be used in the Blokus using AI simulation.  
For this project, the Blokus version will be based on the Blokus Duo, which have 2 players with 14 by 14 board size.

## Functionality
* Board size can be changed (14 by 14 for the project, 20 by 20 for the standard Blokus 4 player game)
* Each AI can use a strategy that is implemented in the program
* The game allows 2 to 4 players (2 players for the project)
* Allow multiple matches in a game (100 matches for the project)

## Game Strategies
* **Random** - Randomly chooses a piece and its placement
* **Simple Greedy** - Based on the pieces' size only and placement is random
* **Advanced Greedy** - Based on both the size and average available corner difference between the player and the opponents for a piece placement
* **First Turn Advantage** will be considered and studied as well

## Simulation Performed
* Random vs. Random
* Greedy (Basic) vs. Random
* Random vs. Greedy (Basic)
* Greedy (Basic) vs. Greedy (Basic)
* Greedy (Advanced) vs. Random
* Random vs. Greedy (Advanced)
* Greedy (Advanced) vs. Greedy (Advanced)
* Greedy (Advanced) vs. Greedy (Basic)
* Greedy (Basic) vs. Greedy (Advanced)

## Game Result
* The statistic is in the form of:  
     *first player win, second player win, tie* - Based on total of 100 matches in a game
* Random vs. Random - **61, 35, 4**
* Greedy (Basic) vs. Random - **95, 4, 1**
* Random vs. Greedy (Basic) - **92, 6, 2**
* Greedy (Basic) vs. Greedy (Basic) - **59, 28, 3**
* Greedy (Advanced) vs. Random - **86, 13, 1**
* Random vs. Greedy (Advanced) - **78, 19, 3**
* Greedy (Advanced) vs. Greedy (Advanced) - **51, 39, 10**
* Greedy (Advanced) vs. Greedy (Basic) - **42, 58, 0**
* Greedy (Basic) vs. Greedy (Advanced) - **64, 32, 4**

## Analysis
* **First Turn Advantage** is noticeable in any first turn player
* For two players using the same strategy, the first player will have higher winning ratio
* **Greedy** strategy is generally more effective than **Random**
* **Simple Greedy** strategy is more effective than **Advanced Greedy** strategy
