#!/usr/bin/python

import board

boardPositions = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
totalPositions = 9
victoryAchieved = False
player = "X"
while not victoryAchieved and totalPositions > 0:
  board.printBoard(boardPositions) # Show the player the current board
  positionAvailable = True
  while positionAvailable:
    positionToOccupy = raw_input("Player " + player + " where do you want put your mark? ") # Get the position where the player want to go
    if boardPositions[positionToOccupy] == 'X' or boardPositions[positionToOccupy] == 'O': # If the position is already taken let the player know
      print "That position is occupied please select another"
    else: #If it isnt taken assign it
      boardPositions[positionToOccupy] = player # Set that position to the players mark
      totalPositions = totalPositions - 1

	# cycle thru all the possible winning combos and le the user know if they win
      if boardPositions['1'] == player and boardPositions['2'] == player and boardPositions['3'] == player:
        board.printBoard(boardPositions) # Show the player the current board
        print "Congratulations player %s Wins!" % player
        victoryAchieved = True
        break
      elif boardPositions['4'] == player and boardPositions['5'] == player and boardPositions['6'] == player:
        board.printBoard(boardPositions) # Show the player the current board
        print "Congratulations player %s Wins!" % player
        victoryAchieved = True
        break
      elif boardPositions['7'] == player and boardPositions['8'] == player and boardPositions['9'] == player:
        board.printBoard(boardPositions) # Show the player the current board
        print "Congratulations player %s Wins!" % player
        victoryAchieved = True
        break
      elif boardPositions['1'] == player and boardPositions['4'] == player and boardPositions['7'] == player:
        board.printBoard(boardPositions) # Show the player the current board
        print "Congratulations player %s Wins!" % player
        victoryAchieved = True
        break
      elif boardPositions['2'] == player and boardPositions['5'] == player and boardPositions['8'] == player:
        board.printBoard(boardPositions) # Show the player the current board
        print "Congratulations player %s Wins!" % player
        victoryAchieved = True
        break
      elif boardPositions['4'] == player and boardPositions['5'] == player and boardPositions['6'] == player:
        board.printBoard(boardPositions) # Show the player the current board
        print "Congratulations player %s Wins!" % player
        victoryAchieved = True
        break
      elif boardPositions['3'] == player and boardPositions['6'] == player and boardPositions['9'] == player:
        board.printBoard(boardPositions) # Show the player the current board
        print "Congratulations player %s Wins!" % player
        victoryAchieved = True
        break
      elif boardPositions['1'] == player and boardPositions['5'] == player and boardPositions['9'] == player:
        board.printBoard(boardPositions) # Show the player the current board
        print "Congratulations player %s Wins!" % player
        victoryAchieved = True
        break
      elif boardPositions['3'] == player and boardPositions['5'] == player and boardPositions['7'] == player:
        board.printBoard(boardPositions) # Show the player the current board
        print "Congratulations player %s Wins!" % player
        victoryAchieved = True
        break
      elif totalPositions <= 0:
        print "The Game is a tie, No winner today!"

      if player == 'X': #Set the player for the next turn
        player = 'O'
      else:  
        player = 'X'
      positionAvailable = False
