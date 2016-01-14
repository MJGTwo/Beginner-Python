# Loops

What if I had a table of data that we needed to print out in a pattern, like a Sudoku puzzle. Or maybe I wanted scan through the numbers 1 through 100. It would be difficult to do it with just using if statements and functions. Processes like repetition are tough. However we have loops: for loops and while loops.

## While loops

```py
while (condition):
  do task
```

If we were to look at this after our lecture on `if` statements, we would see a bit of a similarity. There is. The two lines above mean the following: `While` this `condition` is `True`, do task. Think about it for a moment.
### True loops
What happens when we do this code:

```py
while(True):
  print "Hello!"
```

Think about it.

This is called an _infinite loop_ or a *forever loop*. It will go on forever until your computer's battery runs out or it dies. If this happens in your Python shell, don't worry. Restart the shell or kill Python. To restart the Python shell if you are using Wing 101, go to the window in Wing 101 that has the Python Shell. In the top right corn there is a tab that has the word "options". Click it and the first option is "restart Python". Click it and it will fix your problem. To kill Python, launch your Operating System's task manager and end the task.

To avoid a infinite loop, you must have an _end condition_. That is to say, a condition that is met that causes the loop to end. A while loop is like an if statement: it does not do the task inside of it if the condition is `False`.
### Examples
The best way of explaining the while loop is to do some examples.

```py
x = 0
while (x <10):
  print x
  x+=1
```
This will print out a number going from 0 to 9, one on each line:
```
0
1
2
3
4
5
6
7
8
9
```
We could make a menu:
```py
from math import pi
user = 0
while (user != '-1'):
  print "Enter a number from below:"
  print "\t1) print \"Hello, world!\""
  print "\t2) print the number 2"
  print "\t3) print pi"
  print "Enter -1 to quit"
  user = raw_input("Enter: ")
  if (user == "1"):
    print "Hello, world!"
  elif (user == "2"):
    print 2
  elif (user == "2"):
    print "%.4f" % pi
  print
print "Bye!"

```

Here is the result with me enter numbers into it. Watch how it handles things that are not options:

```
Enter a number from below:
  1) print "Hello, world!"
  2) print the number 2
  3) print pi
Enter -1 to quit
Enter: 1
Hello, world!

Enter a number from below:
  1) print "Hello, world!"
  2) print the number 2
  3) print pi
Enter -1 to quit
Enter: 2
2

Enter a number from below:
  1) print "Hello, world!"
  2) print the number 2
  3) print pi
Enter -1 to quit
Enter: 3
3.1416

Enter a number from below:
  1) print "Hello, world!"
  2) print the number 2
  3) print pi
Enter -1 to quit
Enter: pineapple

Enter a number from below:
  1) print "Hello, world!"
  2) print the number 2
  3) print pi
Enter -1 to quit
Enter: quit

Enter a number from below:
  1) print "Hello, world!"
  2) print the number 2
  3) print pi
Enter -1 to quit
Enter: -1

Bye!
```

`While` loops are powerful and very useful.

## For loops

There are two types of loops. `While` loops and `for` loops. They are 
