#!/usr/bin/python
import rollDice
import readyToRoll

"""Set begining values for variables """
playerIndex = 0
playerScore = {'One':0,'Two':0}

""" Stay in the loop while both players score is less than 100 """
while playerScore['One'] < 100 and playerScore['Two'] < 100:
  if playerIndex%2 == 0: # If the player index is even set player to 1 
    player = 'One'
  else: # If player index is not even set play to 2
    player = 'Two'
  
  """Loop until the results of readytoroll return True then break """
  while True:
   if readyToRoll.readyToRoll(player):
     break

  roll = rollDice.rollDice() #The player answered yes so roll the dice
  if roll == 1: # Your turn ends when you role a 1
    print "You have rolled a 1, your turn is over"
    playerIndex += 1 # Increment the player index by 1
  else:
    playerScore[player] += roll # Add the new dice roll to the players total
    if playerScore[player] >= 100: # First to 100 or more wins
      print "Player %s has WON the game with a score of %d" % (player, playerScore[player])
    else:
      """ You havent won yet, keep going """
      print "Player %s has rolled %d for a new score of %d, you get to go again" % (player, roll, playerScore[player])
