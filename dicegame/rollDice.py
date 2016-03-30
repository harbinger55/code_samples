from random import randrange

def rollDice():
  """Generate a random int between 1 and 6 using the random randrange to 
  similate a dice roll """
  roll = randrange(1,7)

  return roll # return the resuilt of the roll
