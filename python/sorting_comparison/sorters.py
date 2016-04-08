# Bubble sort
def bubbleSort(sort_list):
  # set the condition to exit the while loop to false
  sortComplete = False

  while not sortComplete:
    # Set the initial value to 0, we use the to know if the loop made any changes
    didASort = 0
    # Go into a while loop with index on the list
    for index,item in enumerate(sort_list):
      #if (index +1) <= len(sort_list) skip to the next iteration
      if not (index + 1) >= len(sort_list):
        """If itme is greater than the next item in the list, 
           delete item by index and insert item at index + 1"""
        if item > sort_list[index + 1]:
          didASort += 1 # increment didAsort
          del sort_list[index] # Delete the index from list
          sort_list.insert(index + 1,item) # Add the vzlue to index + 1
	  next
      # If we did a sort keep sortComplete to fale so we stay in the while loop
      if didASort >= 1:
        sortComplete = False
     # if we didnt so a sort set sortComplete to True, we are donme here
      else:
        sortComplete = True
# return the sorted list
  return(sort_list)

def insertionSort(sort_list):
  returnList = [] # Initialize the return list
  for item in sort_list: # start the loop of the orginal list
    if not returnList: # If the list is empty add the current item to start the list
      returnList.append(item)
    else:
      for index,new_item in enumerate(returnList): # run through a loop to determine where to add the item from sort_list to returnList
        # if the item from sort_list is lower than the itme form returnList and we are not at the end of the list insert item at the current index
        if item <= new_item  and index < len(returnList): 
          returnList.insert(index, item)
          break
        # if item from sort_list is greater than the item from returnList and we are at the end of returnList append the item 
        elif item >= new_item and index + 1 == len(returnList):
          returnList.append(item)
          break
  #return the sorted list to the caller
  return(returnList )
    
