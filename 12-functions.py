countries_info = {}
countries_info["Poland"] = ("Warsaw", 37.97) # country name as a key, and 2 element tuple as value. 
countries_info["Germany"] = ("Berlin", 83.02)
countries_info["Slovakia"] = ("Bratislava", 5.45)

def show_country_info(country):  # defining function called show_country_info
    country_info = countries_info.get(country)

    print()
    print(country)
    print()
    print("Capital city: " , country_info[0])
    print("Population(mln): " , country_info[1])
    print()   # no argument is returned by this function. Only operations are performed


for country in countries_info.keys():
    print(country)

country = input("Which country to display it's data? ")
show_country_info(country)


def calculate_sum(a , b):
    # return (a + b)  
    return a + b   # to return arguments boath this and the notation above works

print(calculate_sum(2 , 3))


def print_message():  # function without input arguments can also be used
    print("This function has been sucessfully activated")

print_message() 
