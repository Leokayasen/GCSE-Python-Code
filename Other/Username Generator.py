firstInitial = input("Enter your forename initial: ")
surname = input("Enter the first 3 letters of your surname: ")
year = input("Enter the year you where born: ")
age = input("Enter your age in the range 11-19: ")

username = firstInitial + surname + str(age) + str(year[3:4])

print("Your username is: " + username)