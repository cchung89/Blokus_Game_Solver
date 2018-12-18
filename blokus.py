import sys
import math
import random
import copy
import shape

# Blokus Board
class Board:
   # '_' represents empty square
   # board size: (row: nrow, col: ncol)
   def __init__(self, nrow, ncol):
      self.nrow = nrow # total rows
      self.ncol = ncol # total columns
      self.state = [['_'] * ncol for i in range(nrow)] # empty board

   # Takes in a player id and a move as a
   # list of position (x, y) that represent the piece location.
   def update(self, player_id, placement):
      for row in range(self.nrow):
         for col in range(self.ncol):
            if (col, row) in placement:
               self.state[row][col] = player_id

   # Check if the point (y, x) is within the board's bound
   def within_bounds(self, point):
      return 0 <= point[0] < self.ncol and 0 <= point[1] < self.nrow

   # Check if a piece placement overlap another piece on the board
   def overlap(self, placement):
      for x, y in placement:
         if self.state[y][x] != '_':
            return True
      return False

   # check whether a certain player occupies a specific board location
   def occupy_square(self, x, y, player_id):
      return self.within_bounds((x, y)) and self.state[y][x] == player_id

   # Checks if a piece placement is adjacent to any square on
   # the board which are occupied by the player proposing the move.
   def adjacent(self, player_id, placement):
      # Check left, right, up, down for adjacent square
      for x, y in placement:
         if (self.occupy_square(x + 1, y, player_id) 
            or self.occupy_square(x - 1, y, player_id)
            or self.occupy_square(x, y - 1, player_id)
            or self.occupy_square(x, y + 1, player_id)):
            return True
      return False

   # Check if a piece placement is cornering
   # any pieces of the player proposing the move.
   def corner(self, player_id, placement):
      # check the corner square from the placement
      for x, y in placement:
         if (self.occupy_square(x + 1, y + 1, player_id) 
            or self.occupy_square(x - 1, y - 1, player_id)
            or self.occupy_square(x + 1, y - 1, player_id)
            or self.occupy_square(x - 1, y + 1, player_id)):
            return True
      return False
   
   # Print the current board layout
   def print_board(self):
      print("Current Board Layout:")
      for row in range(self.nrow):
         for col in range(self.ncol):
            print(" " + str(self.state[row][col]), end = '')
         print()

# Player Class
class Player:
   def __init__(self, id, strategy):
      self.id = id # player's id
      self.pieces = [] # player's unused game piece, list of Shape
      self.corners = set() # current valid corners on board
      self.strategy = strategy # player's strategy
      self.score = 0 # player's current score

   # Add the player's initial pieces for a game 
   def add_pieces(self, pieces):
      random.shuffle(pieces)
      self.pieces = pieces

   # Remove a player's piece (Shape)   
   def remove_piece(self, piece):
      self.pieces = [p for p in self.pieces if p.id != piece.id]

   # Set the available starting corners for players
   def start_corner(self, p):
      self.corners = set([p])

   # Updates player information after placing a board piece (Shape)
   # like the player's score  
   def update_player(self, piece, board):
      self.score += piece.size # update score
      if len(self.pieces) == 1: # If the current piece is the last unused piece
         self.score += 15 # bonus for putting all pieces
         if piece.id == 'I1':
            self.score += 5 # bonus for putting the smallest piece last
      for c in piece.corners: # Add the player's available corners
         if board.within_bounds(c) and not board.overlap([c]):
            self.corners.add(c)

   # Get a unique list of all possible placements (Shape)
   # on the board
   def possible_moves(self, pieces, game):
      # Updates the corners of the player, in case the
      # corners have been covered by another player's pieces.
      self.corners = set([(x, y) for (x, y) in self.corners
         if game.board.state[y][x] == '_'])

      placements = [] # a list of possible placements (Shape)
      visited = [] # a list placements (a set of points on board)

      # Check every available corners
      for cr in self.corners:
         # Check every available pieces
         for sh in pieces:
            # Check every reference point the piece could have.
            for num in range(sh.size):
               # Check every flip
               for flip in ["h", "v"]:
                  # Check every rotation
                  for rot in [0, 90, 180, 270]:
                     # Create a copy to prevent an overwrite on the original
                     candidate = copy.deepcopy(sh)
                     candidate.create(num, cr)
                     candidate.flip(flip)
                     candidate.rotate(rot)
                     # If the placement is valid and new
                     if game.valid_move(self, candidate.points):
                        if not set(candidate.points) in visited:
                           placements.append(candidate)
                           visited.append(set(candidate.points))
      return placements
    
   # Get the next move based off of the player's strategy
   def next_move(self, game):
      return self.strategy(self, game)

# Blokus Game class
class Blokus:
   def __init__(self, players, board, all_pieces):
      self.players = players # list of players in the game
      self.rounds = 0 # current round in the game
      self.board = board # the game's board
      self.all_pieces = all_pieces # all the initial pieces in the game
      self.previous = 0  # previous total available moves from all players
      self.repeat = 0 # counter for how many times the total available moves are
                      # the same by checking previous round
      self.win_player = 0 # winner's id, 0 = a tied between players

   # Check for the winner (or tied) in the game and return the winner's id.
   # Or return nothing if the game can still progress
   def winner(self):
      # get all possible moves for all players
      moves = [p.possible_moves(p.pieces, self) for p in self.players]

      # check how many rounds the total available moves from all players
      # are the same and increment the counter if so
      if self.previous == sum([len(mv) for mv in moves]):
         self.repeat += 1
      else:
         self.repeat = 0

      # if there is still moves possible or total available moves remain
      # static for too many rounds (repeat reaches over a certain threshold)
      if False in [len(mv) == 0 for mv in moves] and self.repeat < 4:
         self.previous = sum([len(mv) for mv in moves])
         return None # Nothing to return to continue the game
      else: # No more move available, the game ends
         # order the players by highest score first
         candidates = [(p.score, p.id) for p in self.players]
         candidates.sort(key = lambda x: x[0], reverse = True)
         highest = candidates[0][0]
         result = [candidates[0][1]]
         for candidate in candidates[1:]: # check for tied score
            if highest == candidate[0]:
               result += [candidate[1]]
         return result # get all the highest score players

   # Check if a player's move is valid, including board bounds, pieces' overlap,
   # adjacency, and corners.
   def valid_move(self, player, placement):
      if self.rounds < len(self.players): # Check for starting corner
         return not ((False in [self.board.within_bounds(pt) for pt in placement])
            or self.board.overlap(placement)
            or not (True in [(pt in player.corners) for pt in placement]))
      return not ((False in [self.board.within_bounds(pt) for pt in placement])
         or self.board.overlap(placement)
         or self.board.adjacent(player.id, placement)
         or not self.board.corner(player.id, placement))

   # Play the game with the list of player sequentially until the
   # game ended (no more pieces can be placed for any player)
   def play(self):
      # At the beginning of the game, it should
      # give the players their pieces and a corner to start.
      if self.rounds == 0: # set up starting corners and players' initial pieces
         max_x = self.board.ncol - 1
         max_y = self.board.nrow - 1
         starts = [(0, 0), (max_x, max_y), (0, max_y), (max_x, 0)]

         for i in range(len(self.players)):
            self.players[i].add_pieces(list(self.all_pieces))
            self.players[i].start_corner(starts[i])

      winner = self.winner() # get game status
      if winner is None: # no winner, the game continues
         current = self.players[0] # get current player
         proposal = current.next_move(self) # get the next move based on
                                            # the player's strategy
         if proposal is not None: # if there a possible proposed move
            # check if the move is valid
            if self.valid_move(current, proposal.points):
               # update the board and the player status
               self.board.update(current.id, proposal.points)
               current.update_player(proposal, self.board)
               current.remove_piece(proposal) # remove used piece
            else: # end the game if an invalid move is proposed
               raise Exception("Invalid move by player " + str(current.id))
         # put the current player to the back of the queue
         self.players = self.players[1:] + self.players[:1]
         self.rounds += 1 # update game round
      else: # a winner (or tied) is found
         if len(winner) == 1: # if the game results in a winner
            self.win_player = winner[0]
            print('Game over! The winner is: ' + str(winner[0]))
         else: # if the game results in a tie
            print('Game over! Tied between players: '
               + ', '.join(map(str, winner)))

# Random Strategy: choose an available piece randomly
def Random_Player(player, game):
   options = [p for p in player.pieces] # get all player's available pieces
   while len(options) > 0: # if there are still options to find possible moves
      piece = random.choice(options) # get a random piece
      # get a list of all possible moves from that piece
      possibles = player.possible_moves([piece], game)

      if len(possibles) != 0: # if there is possible moves
         return random.choice(possibles) # choose a random placements to use
      else: # no possible move for that piece
         options.remove(piece) # remove it from the options
   return None # no possible move left

# Basic Greedy Strategy: chooses an available piece with the highest size
def Greedy_Player(player, game):
   options = [p for p in player.pieces]
   # order the piece based on highest size first
   options.sort(reverse = True, key = lambda x: x.size)

   while len(options) > 0:
      piece = options[0] # get the largest piece
      possibles = player.possible_moves([piece], game)

      if len(possibles) != 0:
         return random.choice(possibles)
      else:
         options.remove(piece)
   return None

# Advanced Greedy Strategy: chooses an available piece based on a hueristic
# It is based on the piece's size and the total corner difference from
# its placement
def Greedy_Player_Two(player, game):
   shape_options = [p for p in player.pieces]
   board = game.board
   weights = [] # array of tuples, (piece's placement, weight)

   for piece in shape_options:
      possibles = player.possible_moves([piece], game)
      if len(possibles) != 0:
         for possible in possibles:
            # set a test player and board to simulate a future move,
            # then determine the average total available corners difference
            # between the player and its opponents
            test_players = copy.deepcopy(game.players)
            opponents = [p for p in test_players if p.id != player.id]
            test_board = copy.deepcopy(board)
            test_board.update(player.id, possible.points)
            test_player = copy.deepcopy(player)
            test_player.update_player(possible, test_board)
            my_corners = len(test_player.corners)
            total = 0 # total corner difference between player and each opponent
            for opponent in opponents:
               opponent.corners = set([(x, y) for (x, y) in opponent.corners
                  if test_board.state[y][x] == '_'])
               total += (my_corners - len(opponent.corners))
            average = total / len(opponents) # average corner difference
            weights += [(possible, 2 * piece.size + average)]
   weights.sort(key = lambda x: x[1], reverse = True) # sort by highest weight
   # get the highest weighted placement if there are possible moves left
   return None if len(weights) == 0 else weights[0][0]

# Play a game of blokus without showing the board
def test_blokus(blokus):
   blokus.play()
   # game continues until a winner (or tied) is decided
   while blokus.winner() is None:
      blokus.play()

# play a round of blokus including printing the board
def play_blokus(blokus):
   print("Round: " + str(blokus.rounds))
   blokus.board.print_board()
   print('=================================================================')
   blokus.play()
   print("Round: " + str(blokus.rounds))
   blokus.board.print_board()
   for player in blokus.players:
      print("Player " + str(player.id) + " score " + str(player.score) + ": "
         + str([sh.id for sh in player.pieces]))
   print('=================================================================')

   while blokus.winner() is None:
      blokus.play()
      print("Round: " + str(blokus.rounds))
      blokus.board.print_board()
      for player in blokus.players:
         print("Player " + str(player.id) + " score " + str(player.score) + ": "
            + str([sh.id for sh in player.pieces]))
      print('=================================================================')

# run multiple blokus games with a strategy for each player
# default configuration: 14 by 14 board with 100 matches in a game
#                        no print out of board every round
#                        two players with random strategies
def simulate(row = 14, col = 14, repeat = 100, printout = False,
   *players):
   if not (1 < len(players) < 5):
      print('Total players need to be between 2 to 4!')
      return

   winner = {} # players' total win counts
   for i in range(len(players)):
      winner[i + 1] = 0
   for i in range(repeat): # Play multiple times
      print("New Game " + str(i))
      order = []
      for index, strategy in enumerate(players, 1):
         order += [Player(index, strategy)] # total players in order
      all_pieces = [shape.I1(), shape.I2(), shape.I3(), shape.I4(), shape.I5(),
                  shape.V3(), shape.L4(), shape.Z4(), shape.O4(), shape.L5(),
                  shape.T5(), shape.V5(), shape.N(), shape.Z5(), shape.T4(),
                  shape.P(), shape.W(), shape.U(), shape.F(), shape.X(),
                  shape.Y()] # set up all the initial game pieces
      board = Board(row, col) # 14 by 14 board
      blokus = Blokus(order, board, all_pieces)

      # print the board every round if desired
      play_blokus(blokus) if printout else test_blokus(blokus)

      blokus.board.print_board() # print the final board
      blokus.play()
      print('Final Score:')
      plist = sorted(blokus.players, key = lambda p: p.id)

      for player in plist:
         print('Player ' + str(player.id) + ': ' + str(player.score))
      if blokus.win_player > 0: # if there is a winner, not a tie
         winner[blokus.win_player] += 1 # update the winner's win count
      # print players' win count
      for player_id in winner:
         print('Player ' + str(player_id) + ' win count: '
            + str(winner[player_id]))
      print()


def main():
   printout = False
   if len(sys.argv[1:]) > 0 and sys.argv[1] == 'print':
      printout = True
   print("Senior Project Blokus Game")

   # Simulation setup
   # - board size: # of rows (row), # of cols (col)
   # - total matches: repeat
   # - print board status every round: printout
   # - total players + their strategies: *players
   # - method signature: simulate(row, col, repeat, printout, *players)
   simulate(20, 20, 1, printout,
      Random_Player, Greedy_Player_Two, Greedy_Player, Random_Player)


if __name__ == '__main__':
   main()