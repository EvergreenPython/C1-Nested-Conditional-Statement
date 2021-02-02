'''
02/01/2021

Review:
if/elif/else statement

if (Condition):
  Body Statement1

elif (Condition):
  Body Statement2

.
.
.

else:
  Body Statement3


Nested Conditional Statement
- A conditional statement inside another conditional statement

Indentation
- The header/clause of a nested conditional statement must be indented
from an outter header.

if (Condition):
  Body statement 1
  if (Condition):       <-- Starting a nested statement 
    Body statement 1a   <-- Ending a nested statement

elif (Condition):
  Body Statement2
  if (Condition):       <-- Starting a nested statement 
    Body statement 2a
  
  elif (Condition):
    Body statement 2b   
    
  else:
    Body statment 2c    <-- Ending a nested statement
.
.
.

else:
  Body Statement3


# Example

x = y = 10

if (x < y): # False
  print ("x is less than y")
else:
  if (x > y): # False
    print ("x is greather y")
  else:
    print ("x and y must be equal")

'''
# Exercise: Evaluate if your number is positive/negative/zero and odd/even.
userNum = int(input("Enter a number: "))

# Positive
if (userNum > 0):
  if (userNum % 2 == 0):
    print ("Even Number")
  elif (userNum % 2 == 1):
    print ("Odd Number")
  
  print ("Positive Number")

# Negative
elif (userNum < 0):
  if (userNum % 2 == 0):
    print ("Even Number")
  elif (userNum % 2 == 1):
    print ("Odd Number")
  
  print ("Negative Number")

# Zero
else:
  print ("Zero")