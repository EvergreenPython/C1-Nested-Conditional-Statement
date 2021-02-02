##  Nested Conditional Statement

A conditional statement inside another conditional statement

### Indentation
The header/clause of a nested conditional statement must be indented from an outter header.

### Formula: 
```python
if (Condition): 
  if (Condition):     <-- Starting a nested statement
    Body Statement
  
  elif (Condition):
    Body Statement
  
  else:
    Body Statement    <-- Ending a nested statement

elif (Condition): 
  Body Statement 

else: 
Body Statement 
```

*Ex. * 
```python
x = 10
y = 10

if (x < y):
    print("x is less than y")
else:
    if (x > y):
        print("x is greater than y")
    else:
        print("x and y must be equal")
```
> x and y must be equal
  