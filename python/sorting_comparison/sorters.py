import time
def compareSorts(sort_list):
  (btime,blist) = bubbleSort(sort_list)
  (itime,ilist) = insertionSort(sort_list)
  (stime,slist) = selectionSort(sort_list)

  if btime < itime and btime < stime:
   print "Bubble Sort was the fastest with a time of %f seconds (insertion sort: %f, selection sort: %f)" % (btime,itime,stime)
   print blist
  elif itime < btime and itime < stime:
   print "Insertion Sort was the fastest with a time of %f seconds (bubble sort: %f, selection sort: %f)" % (itime,btime,stime)
   print ilist
  elif stime < btime and stime < itime:
   print "Selection Sort was the fastest with a time of %f seconds (bubble sort: %f, insertion sort: %f)" % (stime,btime,itime)
   print slist
  else:
   print "There is no winner today, science has failed us all (bubble sort: %f,insertion sort: %f, selection sort: %f)" % (btime,itime,stime)

# Bubble sort
def bubbleSort(sort_list):
  startTime = time.time() # Get the start time
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
  endTime = time.time() - startTime #Get the time in seconds it took to run
# return the sorted list
  return(endTime,sort_list)

#insertion sort
def insertionSort(sort_list):
  startTime = time.time() # Get the start time
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
  endTime = time.time() - startTime #Get the time in seconds it took to run
  #return the sorted list to the caller
  return(endTime,returnList)
    
#selection sort
def selectionSort(sort_list):
  startTime = time.time() # Get the start time
  indexCounter = len(sort_list) - 1 # Get the list length, minus 1 so it starts at 0

  while indexCounter >= 0: #Do while the counter is less than or equal to 0
    lastValue = sort_list[indexCounter] # store the value of the list at location indexCounter in a variable
    if indexCounter > 0: # Only do this if the index number is greater than 0, max gets mad if there is only one value to compare
      highestValue = max(sort_list[:indexCounter]) #et highestValue to the value of the maximum in the sort_list upto indexCounter
    else:
      highestValue = sort_list[0] # If the index slice it at 0 assign hightestValue to that
    sort_list[sort_list.index(highestValue)] = lastValue # Replace the location in the list corosponding to hightestVale with lastValue
    sort_list[indexCounter] = highestValue #make the highest indice in the current slice equal highest value
    indexCounter = indexCounter - 1 # decremnt the indexCounter
  endTime = time.time() - startTime #Get the time in seconds it took to run
  return(endTime,sort_list) # return the sorted_list
