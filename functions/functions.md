# Functions

Remember when you are in math class and you are told `y = 2x + 4` was the equation for y? You can say that it is a function for `y` in that `y` is given the value of the summation of twice `x` and `4`. Let's write it in a different way: `f(x) = 2x + 4`. There is a function, called `f` that takes in the value `x` and it returns the summation of twice `x` and `4`. Instead of `f`, we could call it `g` or `f1`. Maybe `cat`. It could be anything you want.

## An example

``` python
def add(x,y):
  answer = x + y
  return answer
```

* `def`
 * def is short for *define* and it is used to define a function. You use it whenever you want to make a function.
* `add`
 * This is the name of the function. Try to use names that are meaningful so when you look at them you get an idea of what it does.
* `(x,y)`
 * Every function has twice parenthesis, an open one and a close one, at the end of the function. Anything that goes inside the parenthesis are things that the function uses as input. To go along with our function earlier, `f(x)`, the function `f` has the input `x`.
* `:`
 * This is Python's grammar (also known as syntax) to say that the definition of a function will begin on the next line.
* `answer = x + y`
 * Whenever you have `=` in Python, it does not mean that both sides are equal. They technically are equal but that is not what's going on here. It means that you give the value from the right side of the `=` to the left side of the `=`
 * `answer` gets the value of the summation of `x+y`. This is also known as `answer` is *assigned* the value of the summation of `x+y`.
* `return answer`
 * `return` is another *keyword* (a word that has a special purpose in a language) like `:`. It means that the output of the function `add` is what follows it. In this case, the output is `answer`.
