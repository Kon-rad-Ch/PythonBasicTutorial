name = "konrad"

print("name : " , name)
print("name lenght : " , len(name)) 
print("Type capitalized name, but not change the var. name! Name = " , name.capitalize())
print("var. name = " , name)


sentence = "Marry had a little Lamb"
print("Sentence : " , sentence)
print("sentence.lower : " , sentence.lower())
print("sentence.capitalize : " , sentence.capitalize())
print("sentence.upper" , sentence.upper())

print("first letter of name : " , name[0]) # index counting starts at 0
print("first 3 letters of nam : " , name[0:3]) # 0 as starting index and 3 as nuber of following letters to be taken
print("all letters from the 2nd till the end : " , name[1:])
print("all letters starting from 3rd till the end" , name[-3:]) # -0 is not used, so while calculating backwards -1 is the firs letter

print("List the words from the sentence :" , sentence.split(" ")) # space used as separator

join_string = " "
#join_string = "-"

print(join_string.join(['Who', 'let', 'the', 'dogs', 'out?']
))

print("Does name start with K ? " , name.startswith("K"))
print("Does name start with k ? " , name.startswith("k"))


print("does name end with d? " , name.endswith("d"))
print("does name end with K? " , name.endswith("K"))

#---------strip---------

print("**********<strip>**********")

print(name.rstrip("d")) # if the last / most right letter is "d" it is erased and the rest is displayed
print(name.rstrip("r")) 

print(name.lstrip("K"))
print(name.lstrip("k"))

palindrom = "kayak"
print(palindrom.strip("k"))  # stripes boath left and right side if letter correlate
trash = "    rubbish "
print(trash)
print(trash.strip()) # stripping all the spaces  right and left side


print("**********</strip>**********")


print("broken boat:" + " " + trash.strip() + " " + palindrom) # adding of strings

join_string = " "
print(join_string.join([trash , palindrom]))
print(join_string.join([trash.strip() , palindrom]))

james_bond = 7
print(str(james_bond).zfill(3)) # int to str conversion, zfill method adds 0 at the beaginning to reach the number of digits as in arg

james_bond = 77777
print(str(james_bond).zfill(3)) # no 0 will be added, but all the initial digits will be present
