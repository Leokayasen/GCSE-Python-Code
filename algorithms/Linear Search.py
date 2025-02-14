# Linear Search

def linear(namelist,item): # Defines the type of search, LinearSearch
    position = 0 # Start position for search
    found = False # Starting status for finding search query/item
    while position < len(namelist) and not found:
        if str(namelist[position]) == item:
            print('Item found in position: ',position + 1) # Item has been found, tells position in list of item
            found = True # Search query has been found
        position = position + 1

    if not found:
        print('Item not found') # Prints alert for not finding search query
while True:
    #nameList = [1, 2, 8, 13, 17, 19, 32, 42, 56, 47]
    namelist = ['Adam', 'Balint', 'Cindy', 'David', 'Ellie', 'Fred', 'Hugo'] # List for search query
    print(namelist) # Prints search list
    item = input('Enter an item: ') # Input for search query
    linear(namelist,item.title())
