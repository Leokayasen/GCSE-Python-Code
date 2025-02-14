# Binary Search

def binarysearch (alist, item): # Defines 'binarysearch' function with alist and item parameters
  first = 0 # First number in the array
  last = (len(alist)-1) # Last number in the array
  found = False # Boolean - stops while loop
  while first<=last and not found: # Logical loop
    midpoint = (first+last)//2 # Take midpoint in array and Divide by 2
    if alist[midpoint]==item: # If the midpoint is the item, then found must be True
      found = True # Item has been found
      print("Item Found In List")
      print(" ") # This leaves an empty line for the next search attempt
    else:
      if item < alist[midpoint]: # Last becomes lower than midpoint and below the item
        last = midpoint-1 # New last, midpoint -1 is lower than midpoint
      else:
        first = midpoint+1 # New first, midpoint +1 is higher than midpoint

  if not found: # If the item hasn't been found,
    print("Item Not Found In List") #Notify the user of the failed attempt
    print("Try again") #Tells user to retry the binary search
    print(" ") #This leaves an empty line for the next search attempt
binary = [1,2,3,5,7,9,22,45] # List of items for user to search (change the contents for your own list)
print(binary) #This prints the above list
print(" ")
while True:
  item = int(input("Please enter an item you are looking for: ")) #Input for search query/item
  binarysearch(binary, item)
