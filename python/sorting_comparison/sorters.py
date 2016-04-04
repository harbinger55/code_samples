# Bubble sort
def bubbleSort(sort_list):
  # set the condition to exit the while loop to false
  sortComplete = False

  while not sortComplete:
    # Go into a while loop with index on the list
    for index,item in enumerate(sort_list):
      # Set the initial value to 0, we use the to know if the loop made any changes
      didASort = 0
      # Do stuff in the next 
      #if (index +1) <= len(sort_list) skip to the next iteration
      if (index + 1) < len(sort_list):
        next
        """If itme is greater than the next item in the list, 
           delete item by index and insert item at index + 1"""
        if item >= sort_list[index + 1]:
          del sort_list[index] # Delete the index from list
          sort_list.insert(index + 1,item) # Add the vzlue to index + 1
          didASort += 1 # increment didAsort
    # If we did a sort keep sortComplete to fale so we stay in the while loop
    if didASort >= 1:
      sortComplete = False
   # if we didnt so a sort set sortComplete to True, we are donme here
    else:
      sortComplete = True
# return the sorted list
  return(sort_list)
