# number = 1

# while number < 6:  # any expression with bool output will do
#     print(number)
#     number += 1

print("****^^1^^****")
for number in range(1 , 6): # range is closed on the left and open o the right
    print(number)

print("****^^2^^****")

for number in range(1 , 6, 2): # 3rd optional arg is step
    print(number)

print("****^^3^^****")

for number in range(1, 10):
    if number == 5:
        break          # breaks out of the loop
    print(number)

print("****^^4^^****")

for number in range(1 , 10):
    if number== 5:
        continue       # exits current step and goes to the next one
    print(number)