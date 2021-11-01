
countries_info = {}
countries_info["Poland"] = ("Warsaw", 37.97) # country name as a key, and 2 element tuple as value. 
countries_info["Germany"] = ("Berlin", 83.02)
countries_info["Slovakia"] = ("Bratislava", 5.45)


# print(countries_info['USA']) # key 'USA not defined, so error would be triggered at this point


# try:
#     print(countries_info['USA'])
# except:  #execute the code below - not for precise excetion thrown, but general one. like in catch(...)
#     print("Key not found!")

try:
    print(countries_info['USA'])
except KeyError:  # catches only the KeyError errors type
    print("Key not found!")

print()
print("more complex exception below: \n")

try:
    print(2 / 0)
    print(countries_info['USA'])
except KeyError:  # catches only the KeyError errors type, will still crash on division by zero
    print("Key not found!")   # will not be displayed, because first error was ZeroDivisionError and further lines in try section were not executed
except ZeroDivisionError:
    print("Unable to divide by 0")
finally:
    print("We can proceed") # code in finally section will be executed always no matter if there were exceptions or not
    # commonly used to close file or the connection to the database

# one shall always try to catch particular exeptions thrown, rather than relying on overly general exception support


print("succesfully proceeded with the code")

