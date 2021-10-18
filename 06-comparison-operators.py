a = 5
b = 5

print("a = ", a)
print("Is a = 5? " , a == 5)

print("Is a != 5? " , a != 5)

print("Is a > 5? " , a > 5)

print("Is a < 5? " , a <5)

print("Is a<= 5? " , a<= 5)

print(a is b) # Warning this does compare actuall space in memory, not value so to var. equal by value may be either true or false

print(a is b -2 +1 +1) # is => identity operator, do not use for comparison. Use == (equality operator) instead

print("Now assign a = 10000 and b = 10000")
a = 10000
b = 10000

print("a is b ? " , a is b)
# interesting fact: when in console in python3 a and b are manually assigned than (a is b) -> false it is interpeter depandant

 
