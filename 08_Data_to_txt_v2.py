# Source:

# Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, cant be blank / invalid
#assume valid data for now
filename = input("Enter a Filename(leave off the extension): ")

# add .txt sufix!
filename = filename + ".txt"

# create file to hold data
f - open(filename, "w+")

# add new line at end of each line
for item in data:
    f.write(item + "\n")

# close file
f.close()
