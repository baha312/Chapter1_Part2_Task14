# Given a list of numbers, print all it’s even elements. 
# Use a for-loop that iterates over the list itself and not over its indices. 
# That is, don't use range()

# make an empty list
numbers = []
# create a loop to add to list
ans = 'y'
while ans == "y":
  add = int(input('Enter the number that you want to add to the list:\n'))
  numbers.append(add)
  ans = input('Do you want to add a number? ENTER y for yes or n for no:')
print (numbers)
for x in numbers:
  if x % 2 == 0:   #determine if number is even
    print(x)
    