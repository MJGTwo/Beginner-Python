# If statements

If statements are used to have options when something happens. We have if statements everywhere in our lives: if the time is after 10:30 and I am hungry, then I will go eat lunch; if I get 10 points in a game before you, then I win.

In Python, we have three different keywords that allow us to do this: `if`, `elif`, and `else`. `Elif` is a contraction of `else if`.

```py
color = raw_input("What is your favorite color? ")
color = color.lower()
print "Your favorite color is", color

if color == "blue":
  print color, "is my favorite color too!"
print "Thank you for telling me."
```

Here is what the program does:


The program asks the user `"What is your favorite color?"` and takes in the value the user gave it and saves it to the variable `color`. It then uses the function `.lower()` to change all uppercase letters to lowercase letters in the variable `color`. It will print the user's color in the line `"Your favorite color is," color`, to show the user the program saved it. Then the program compares the string to the value `"blue"` in the `if` statement on line 5. If the strings are equal, then it will do the lines that are indented. There is only one line, which is `print color, "is my favorite color too!"`. After this line, the program will print `"Thank you for telling me."`

In this example, the `if` statement only works if the value after the word `if` have the value `True`. If you look at the section about comparisons, we see that the symbol (operator) `==` checks to see if two values are equal. If they are equal, then it returns the value `True`. If they are not equal, then it returns the value `False`.

If you enter any variation of the string `"blue"`, it will compare it to the string `"blue"` on line 5 and return `True` to the `if` statement.

Let's pretend I ran this program, here are the two possible outputs:

`What is your favorite color? RED`

`Your favorite color is red`

`Thank you for telling me.`

And

`What is your favorite color? BlUe`

`Your favorite color is blue`

`blue is my favorite color too!`

`Thank you for telling me.`

Notice that no matter the `if` statement being `True` or `False`, our last line is still the same.
