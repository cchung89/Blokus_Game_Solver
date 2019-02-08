# Blokus Game Solver - California Polytechnic State University CPE Senior Project
Blokus AI Simulation Program  
Senior Project Report: [Details](https://digitalcommons.calpoly.edu/cpesp/290/)

## Project Goal
* Study the different strategies that can be used in the Blokus using AI simulation.
* For the Senior project, the Blokus version will be based on the Blokus Duo, which have 2 players with 14 by 14 board size.
* For the development of this entire project, it's purpose is to allow gameplay of different Blokus version with different amount of players, like the original 4-players 20 by 20 board game.

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

## Time and Space Complexity
* The more available corners a player has, the more possible moves a player can have overall
* For each turn, each player has to find all the possible board placements from each available piece the player has
* A player can have at most 21 pieces available to choose from
* Each piece has its total amount of reference points based on its size (a piece of size 5 has 5 available reference points)
* Each piece has at most 8 orientations from a single reference point (flip + rotation)
* It is computationally expensive to get all the next possible moves (At least exponential)
* The complete search trees for the piece placements are too large for strategies like Minimax, which involved saving game states, to be effective (At best, probably only 2 or 3 level depth search tree with alpha-beta pruning involved)

## Future Goal
* Develop more complex and effective strategies for the AIs
* Increase the algorithm efficiency to speed up simulation
* Allow the human player to play against an AI player
* Allow human players to player against each other
