# Strings

As mentioned in the [data](/Users/michaelgardner/MEGA/Programming/teaching/data/data.md) lecture earlier, you can make Python strings like `"this"`, `'this'`, `'t'`, or `"a"`. All of these are valid Python strings. Numbers, symbols and special characters also work.

## Special characters (Escape Character)

Here is a question: how do I make a string with a quotation mark (the symbols `'` or `"`) inside of it? Won't it end the string? If you use the right one at the wrong time, yes you will. However Python has special character combinations to allow programmers to do this: behold the powerful backwards slash:

`\`

It's pretty cool. Let's use it

``` Python    
print "\t \' \" \\ \x21"
```
This bit of code would print out the following line:

`____ ' " \ !`

Note: The line (____) isn't there in programming, I have it there to show you what counts as a `\t`.

Let's break down what is going on.
* \t
 * This tells Python to insert a tab character into the string. Tab characters used for formatting a string (making it look pretty). It's purpose is to add 4 white spaces, however it can add less. Here is an example of "\t1\t2" against "\t\t2"

 `____1___2`

 `________2`

 Notice that the two's position doesn't move. That's what tabs can do.
* \'
 * This tells Python to insert a single quote mark and to not end the string.
* \"
 * This tells Python to insert a double quote mark and to not end the string.
* \\\\
 * This tells Python to insert a backslash into the string. This is needed if you are trying to end a string with a backslash, like "this\", in Python. You need to use \\ or an error will occur.
* \x21
 * This is for a hexadecimal value. These are not used very much in beginner Python but it's good to go over. If I type `print "\x21"` into Python, the terminal will print out `!` because 21 is the hexadecimal value, 00100001 in binary and 33 in decimal, of `!` in ASCII.

Each of these symbols (most notably the sing and double quote marks) have special features by default and you must _escape_ that feature when you want to use it as a _literal_ symbol, so when you use the backslash, you are __escaping__ the character and using it as a __literal__
