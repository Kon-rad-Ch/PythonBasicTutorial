print('***  <creating file>  *** \n')
# file = open("file.txt")  # enough to open file

file = open("countries_and_capitals.txt", "w+") # in this mode if the file does not exist in current directory it will be created automatically
# second arg is mode, see further documentation for more details on modes
# also always have in mind the cursor position

countries_and_capitals = {'Poland': 'Warsaw',
                        'Czechia': 'Prague', 'Germany': 'Berlin'}
# sent to a new line with enter and shifted with Tab for a better view in small window

# for country, capital in countries_and_capitals: # would throw error, as by default it would go through keys only
for country, capital in countries_and_capitals.items():  # this way it goes through keyes and values
    file.write(country + "-" + capital + "\n") # .write method is selfexplainatory

file.close() # file closed after the loop overwriting it

print('***  </creating file>  *** \n')



print('***  <opening file>  *** \n')

file = open("countries_and_capitals.txt")

for line in file.readlines(): # line is a temporary var for this loop. readlines does not take input arg.
    print(line)  # print creates new line each time, and new line mark at the end of each line in the file creates empty lines between

file.close()
print()

file = open("countries_and_capitals.txt")
for line in file.readlines():
    print(line.strip()) # .strip method stripes the spaces and the \n as well
file.close()

print('***  </opening file>  *** \n')



