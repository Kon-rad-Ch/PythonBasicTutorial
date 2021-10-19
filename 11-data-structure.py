names_list = []
names_list.append("Sarah") # append adds to the end of the list
names_list.append("Kate")

print("Names added with append function = " , names_list)


names_list_2 = ["Sarah" , "Kate"]

print("Names added while declaring the list = " , names_list_2)

print("Are they equal? -> " , names_list == names_list_2)


for name in names_list: # var name becomes following values of the list till the end of the list
    print(name)


print("Let's reverse the list: ")

names_list.reverse()
print(names_list)


names_list.append("Betty")
names_list.append("Martha")
print("extended list is now: " , names_list)
names_list.sort()
print("Let's sort it alphabetically: " , names_list)

print("Let's call the 2nd on the list: " , names_list[1] , "!")

print()
print("Now adding duplicates")
names_list.append("Betty")
names_list.append("Martha")
names_list.append("Betty")
print("extended list is now: " , names_list)
print("How many Bettys are there? " , names_list.count("Betty"))
print()

print(len(names_list)) # len will tell us how long the list is

print(names_list.pop(0)) #.pop method returns element of the list and erases it from the list
print(len(names_list))
print()

print(names_list)
names_list.remove("Betty") # removes the first appearance of the arg, not all of them
print(names_list)
# names_list.clear()  # erase all positions from the list. The list is now empty
# print(names_list)


print()

names_list_3 = names_list + names_list_2

print(names_list_3)
names_list_3.sort(reverse=True)
print(names_list_3)
print()
print("--- tupple time ---")
names_list_t = ("Anthony" , "Jack" , "Adam") # Tupple can not be changed after it is created
print(names_list_t)
person = ("Marry" , "Black" , "21" , "blond")
print(person , len(person) , person.count("21"))

# list = []  -> OK
# tuple = () -> wrong
print()

names_set = {"green" , "yellow" , "red" , "green"}  # set is like a list, but can not have duplicated elements. Second "green" element is ignored
print(names_set)
# names_set_2 = {} # would not create empty set, but dictionary instead
names_set_2 = set()
names_set.add("Lucas") # adding element ; append is not available for set
names_set.add("Peter")



