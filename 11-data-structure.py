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
person = ("Marry" , "Garland" , "21" , "blond")
print(person , len(person) , person.count("21"))

# list = []  -> OK
# tuple = () -> wrong
print()

names_set = {"green" , "yellow" , "red" , "green"}  # set is like a list, but can not have duplicated elements. Second "green" element is ignored
print(names_set)
# names_set_2 = {} # would not create empty set, but dictionary instead
names_set_2 = set() # creates empty set
names_set_2.add("Lucas") # adding element ; append is not available for set
names_set_2.add("Peter")
print("names set 2 after adding 2 names" , names_set_2)

names_set_2.remove("Peter")
print("names set 2 after removing Peter" , names_set_2)

names_set_2.discard("Lucas")
print("names set 2 after removing Lucas" , names_set_2)
print()
# method .remove throws error when trying to remove non existing element
# method .discard simply does nothing in such case
print("--- <set discard / remove comparison>---")
names_set_2.discard("bananana")
print("OK")
 # names_set_2.remove("bananana")
print("--- </set discard / remove comparison>---")


# print(names_set[1])  # set structure is not organised, so it is not sobscriptable
print(names_set)

for name in names_set:
    print(name)

print("+++++")
nam_set = set() # empty set declaration
nam_list = [] # empty list declaration
nam_tuple = () # empty tuple declaration

nam_set.add("Doorbell")
nam_set.add("Doorknob")

# nam_set.add(nam_list) # can not add list or any other mutable var
nam_set.add(nam_tuple) # can be added, as tupple is immutable

# set summary:
# 1. Values can not be duplicated inside set
# 2. Elements must be immutable
# 3. Elements are not organised

print("+++++")

print(names_set)
names_set_2.add("Terrakota")
names_set_2.add("Pie")
print(names_set_2)

# names_set_3 = names_set + names_set_2 # can not use '+' operator with set type
names_set_3 = names_set.union(names_set_2) # Use .union method instead
print(names_set_3)
names_set_3 = names_set_2.union(names_set)
print(names_set_3)

for test in names_set_3:
    print(test)

names_set.update(names_set_2) # this method adds ns2 to ns without creating a new var

print()
print("ns = " , names_set)
print("ns2 = " , names_set_2)
print()

names_set_4 = names_set.difference(names_set_2)
print("ns - ns2 = " , names_set_4)
print()

names_set_5 = names_set.intersection(names_set_2)
print("What does ns1 and ns 2 have in comon? " , names_set_5)
print()

names_set_6 = names_set.symmetric_difference(names_set_2)
print("What are elements are in ns1 or ns2 but not in both?  " , names_set_6)
print()

names_set.clear() # this method clears the set. No elements inside right now
print(names_set , " nothing to see here")
print()

#there are more interesting set methods - to explore later!


print()

print("ns2 = " , names_set_2)
names_list_2 = ["Jenny", "Laura"]
print("nl2 = " , names_list_2)
print()
# ls_summary = names_list_2 + names_set_2 # this will not work
ls_summary = names_list_2.extend(names_set_2) 


print("nl2 + ns2 (Methode extend) = " , ls_summary ) #so .extend method retured null
print("nl2 after extend methode = " , names_list_2)
print()

# interesting: is vicarious var. the only logical way to create a new list and not change the initial list? See example below.

names_list_2.remove("Terrakota")
names_list_2.remove("Pie")

print("ns2 = " , names_set_2)
print("nl2 = " , names_list_2)
print()

vicarious_list = names_list_2
vicarious_list.extend(names_set_2)
ls_summary = vicarious_list

# Now I see it:
# ls_summary = names_list_2
# ls_summary.estend(names_set_2)
# no additional vicarious var. needed - resoultind list becomes vicarious only temporarily
# non-existing problem solved. Guess no one will ever read this. Mail me to prove I'm' wrong ;) Unfortunately there is no reward.



print()
print(" ->->-> <Dictionary> <-<-<-")
print()

countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin", "Canada": "Toronto", "Bangladesh": "Dhaka"}
print(countries_and_capitals)
countries_and_capitals['Czechia'] = "Prague"
for country in countries_and_capitals.keys():
    print(country)  # each iteration prints keye one after another

print()
for capitals in countries_and_capitals.values():
    print(capitals) # each iteration prints values one after another
print()

for country, capital in countries_and_capitals.items():
    print(country + "-" + capital) # each iteration prints keye adds string and adds key one after another
print()

print(countries_and_capitals["Poland"])
print(countries_and_capitals.get("Poland"))
print()

# print(countries_and_capitals["USA"]) # received error when key not present in the dictionary
print(countries_and_capitals.get("USA")) # received "None" when key not present
print()
print(countries_and_capitals.setdefault("USA" , "Washington DC")) # setdefaults: if arg1 = key exists -> return value. else add arg 1 as key and arg2 as value
print(countries_and_capitals)
print()
print(countries_and_capitals.setdefault("Poland" , "Washington DC")) # in this case as key Poland exist - it's value is returned, and the dictionary is not changed
print(countries_and_capitals)
print()
countries_and_capitals["Poland"] = "Cracow"  # the value is simply changed
print("trying the capital value to previous one: " , countries_and_capitals)
print(countries_and_capitals)
print()
print("this can not be, need to erase this key ")
print(countries_and_capitals.pop("Poland")) # method .pop removes the key and it's value, but also returns the value that used to be assigned to this key
print(countries_and_capitals)
print()
# print(countries_and_capitals.pop("Swizerland")) # .pop returns error when there is no such key value
print(countries_and_capitals.pop("Switzerland" , "Zurich")) # when using the default value for .pop (2nd arg) .pop returns this value when trying to delete no-existing key value
print(countries_and_capitals)
print()
print("Let me .popitem : " , countries_and_capitals.popitem()) #.popitem does not take arg. it removes the last added key and it's value. Key and it's value is returned as tuple
print(countries_and_capitals)
print()
# to check if there is a particular key in the dictionary we'll need a conditional:

if "Canada" in countries_and_capitals.keys():
    print("Key present in the dictionary!")
else:
    print("Key not found")

print()
print("Berlin" in countries_and_capitals)
print("Germany" in countries_and_capitals)
# can be used without specyfying ,key -> will search key values ony anyway

print("Enough, erase this dictionary! " , countries_and_capitals.clear())
print(countries_and_capitals)
print()
print(" ->->-> </Dictionary> <-<-<-")
print()








