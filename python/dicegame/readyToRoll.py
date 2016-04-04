def readyToRoll(player):
  """Get inpuit from the user if they are ready to rolls"""
  ready = raw_input("Player " + player + " are you ready to roll? (Y/N)")

  if ready == 'Y' or ready == 'y' or ready == 'yes':
    """ If the answer is one of the expected values for yes print a message and
    return True"""
    print "Player %s is ready to roll !" % player
    return True
  elif ready == 'N' or ready == 'n' or ready == 'no':
    """ If the answer is one of the expected values for no print a message and
    return False"""
    print "Player %s is not ready to roll" % player
    return False
  else:
    """ If the answer is not one of the expected values print a message letting
    the user know and return False"""
    print "I am sorry I don't understand that answer"
    return False
