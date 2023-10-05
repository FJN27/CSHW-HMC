# -*- coding: utf-8 -*-
"""hw2pr1_turtles_notebook

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SxomJd3ybsH0pNFKOXjoXG_PY9XsMAB4

# Notebooks and Recursion and Turtles!


Welcome to Python notebooks! They're ever more ubiquitous:
+ They interleave <i>code cells</i> that have Python and
+ <i>context cells</i> with descriptions and context.
+ This cell is a <i>context cell</i>
+ If you double-click on it, you'll be able to see its source, a mix of markup and markdown...

### Onward!
"""

#
# This is a code cell - here, you're able to run arbitrary Python scripts.
#

# For example, try running this four-fours example:

from math import *

print("Hello from Colab!")
print()
print("The answer is ", factorial(4)+factorial(4)-4-sqrt(4) )

"""### <font color="DodgerBlue"><b>Make your own copy of this notebook</b></font>
+ Under the <i>File</i> menu in the upper left, choose <i><u>Save a copy in Drive</u></i> to create your own copy
+ That copy you'll be able to edit, run, and save
+ <b><i>Later on</i></b>, when you're ready to submit, you should
  + Choose <i><u>File - Download - Download <tt>.ipynb</tt></u></i>, which is near the bottom of the <i>File</i> menu
  + That will save the file to your machine with the extension <tt>.ipynb</tt>
  + Then, you'll submit that file to the usual GradeScope site, at the appropriate spot.

<br>

Onward, to turtle!

# <font color="DodgerBlue"><b>Turtle Scripting </b></font>

Start by running the code boxes below to install our turtle library, named <tt>ColabTurtlePlus</tt>:

<!--
The line `t.initializeTurtle()` creates a turtle graphic terminal? box? if you haven't created one, and erases/refreshes the turtle graphic if you already have one.
-->
"""

!pip install ColabTurtlePlus

import ColabTurtlePlus.Turtle as t

# after installing, run this cell...
# if it works, you may see a message -- and you should be set!

"""### Next, try an example turtle-drawing script:

- <font size = "-1"> Note:   A script usually describes code that's <i>not</i> organized into a function:
"""

import ColabTurtlePlus.Turtle as t

t.clearscreen()      # it's good to start every cell with this
t.setup(500,500)     # setup the drawing area to be 500 pixels x 500 pixels
t.showborder()       # show the border of the drawing area
t.bgcolor("AliceBlue") # sets the background color (could also use "#E0E0FF" on the Mac)

t.shape('turtle2') # Options: ['turtle', 'ring', 'classic', 'arrow', 'square', 'triangle', 'circle', 'turtle2', 'blank']

t.speed(5)         # 10 is fastest, 1 is slowest

# side one
t.color("green")   # a link below shares _all_ the colors
t.width(5)         # number of pixels wide for the turtle's trail
t.forward(100)     # forward 100 pixels
t.left(90)         # left 90 degrees

# side two
t.color("DodgerBlue")    # hometeam?!
t.width(2)
t.forward(100)
t.left(90)

# side three
t.penup()          # "lift" the pen - the turtle will not draw
t.forward(100)
t.left(90)
t.pendown()        # put the pen back "down": drawing will resume

# side four
t.color("purple")
t.forward(100)
t.left(135)        # to aim "northeast"
t.penup()
from math import sqrt
t.forward(50*sqrt(2))   # move to the "middle": 50*sqrt(2)
t.color("green")

"""#### <font color = "blue"> **Turtle Task #1:    *Drawing practice!***

For the first task, play around a bit by copying the
Turtle script above to the cell below.

The, <i>change</i> it so that:
+ You draw a _different_ set of lines -- with at least ***5*** lines, in this case...
+ Don't take overmuch time on this - Turtle-drawing can be addicting!
+ If you want to "teleport" to coordinates `(42,42)` you can do so with `t.goto(42,42)`
+ Also, experiment with different colors:

**Colors**
+ [This page](https://www.w3schools.com/colors/colors_names.asp) shows the colornames available on all browsers.
+ You can change the background with  `bgcolor("darkblue")` or, perhaps, other colors!

Leave your drawing in the notebook (we look forward to seeing _all_ of the drawings!)

Onward to **functioning** with Turtles...


"""

import ColabTurtlePlus.Turtle as t

t.clearscreen()      # it's good to start every cell with this
t.setup(500,500)     # setup the drawing area to be 500 pixels x 500 pixels
t.showborder()       # show the border of the drawing area
t.bgcolor("AliceBlue") # sets the background color (could also use "#E0E0FF" on the Mac)

t.shape('turtle2') # Options: ['turtle', 'ring', 'classic', 'arrow', 'square', 'triangle', 'circle', 'turtle2', 'blank']

t.speed(5)         # 10 is fastest, 1 is slowest

# side one
t.color("green")   # a link below shares _all_ the colors
t.width(5)         # number of pixels wide for the turtle's trail
t.forward(100)     # forward 100 pixels
t.left(90)         # left 90 degrees

# side two
t.color("DodgerBlue")    # hometeam?!
t.width(2)
t.forward(100)
t.left(90)

# side three
t.color("brown")          # "lift" the pen - the turtle will not draw
t.forward(100)
t.right(90)
t.pendown()        # put the pen back "down": drawing will resume

# side four
t.color("purple")
t.forward(100)


# side five
t.color("chocolate")
t.left(135)        # to aim "northeast"
# t.penup()
from math import sqrt
t.forward(50*sqrt(2))   # move to the "middle": 50*sqrt(2)
t.color("green")

"""## <font color="#f96d7b"><b>Turtle <i>Functioning</i> </b></font>

Below is the recursive <tt>tri</tt> function from class...

- First, look over the code.
- Then, run it and - we hope - it will draw a triangle.
- Notice the call to `tri(3)` at the bottom. That's the "function call" that runs our function, `tri`
"""

import ColabTurtlePlus.Turtle as t

t.clearscreen()      # it's good to start every cell with this
t.setup(500,500)     # setup the drawing area to be 500 pixels x 500 pixels
t.showborder()       # show the border of the drawing area

t.bgcolor("aliceblue")   # Set the background color
t.shape("turtle2")
t.speed(10)
t.width(10)     # width/thickness of the lines

#
# our tri function
#
def tri(n):
    """Draws n 100-pixel sides of an equilateral triangle.
      Note that n doesn't have to be 3 (!)
    """
    if n == 0:
        return      # No sides to draw, so stop drawing
    else:
        t.forward(100)
        t.left(120)
        tri(n-1)    # Recur to draw the rest of the sides!

#
# here, run tri(3)
#
t.fillcolor('blue')
t.begin_fill()
tri(3)
t.end_fill()

"""Consider the code's pieces:

+ First, we setup the Turtle's canvas (adjust to suit!)
+ Then we define the `tri` function, and finally
+ we call it at the bottom with `tri(3)`


You'll notice that the internal turtle-drawing calls all begin with "`t.`" i.e., "`t`" followed by a dot. That is because the underlying code creates a variable named `t` known as <i>an object</i> and then it makes changes to that object, and that object makes changes to the drawing canvas.
+ Not worth worrying about! Just a placeholder. Later in the semester, you will use, create, and design <i>objects</i> in much more depth.

When run, the above code should create a graphic that looks similar to this:

<img src = "https://www.cs.hmc.edu/twiki/pub/CS5Fall2022/Lab2Turtle/tri_3.png" height="100px">

Stop for a moment and ask yourself how `tri` actually works:
+ In particular, `tri` only draws one line: `t.forward(100)`
+ How does it draw a complete triangle?
+ Why do we have `tri(n-1)`?

Note that the base case (or empty case) returns - without actually returning any value. This is because the function does not produce a value - instead, it simply changes pixels on the screen!

In this code, we are calling `tri` for its <i>side effects,</i> which are changes to the world that aren't part of any return value. In this case, the side effects are graphics on your screen.

## <font color="#f96d7b"><b>`Tri`-ing fills, options, and colors! </b></font>

Now, change the above `tri`-ing function, using a fill:

To fill any shape, you can wrap it in `t.begin_fill()`, followed by the function that creates the shape, followed by `t.end_fill()`.
+ For the triangle, try altering the bottom part of the cell to read:
```
t.fillcolor('blue')
t.begin_fill()
tri(3)
t.end_fill()
```
+ Then, change the fill color!

<hr>

Next, change your `tri` function and re-running it in order to try at least one out of the many turtle options:

+ (_Line thickness_)   Put the line    `t.width(10)`    as the first overall line of the `tri` <i>function</i>.
   - ***Or*** put the line    `t.width(3*n+1)`    as the first line of the `else` block in the `tri` function!
+ (_Colorfulness_)   Put the line    `t.color('darkgreen')`    as the first line of the function.
   - Or `import random` near the top of the code box and put the two lines:
        ```
        clr = random.choice(['darkgreen', 'red', 'blue'])
        t.color(clr)
        ```
   as the first lines of the function.
+ (_Other Python turtle-drawing commands_)   Put the line `t.dot(10, 'yellow')` as the first line of the `else` block.
   - This should draw a filled circle (a dot) just before it runs the other lines of the `else` block.
   - Note that you can make the dot a different color than the line color by including the color as the second argument to `dot`.

<br>

<font size="-2">Here is [the documentation for the ColabTurtlePlus library.](https://larryriddle.agnesscott.org/ColabTurtlePlus/documentation2.html) and [the documentation for the Python turtle library.](https://docs.python.org/3/library/turtle.html). No need to reference these - here just in case.</font>

## <font color = "blue"> <b>Turtle Task #2:    <i>Spiraling</i></b>

We look forward to seeing your final `tri` !

Does turtle have you <i>spiraling</i> yet? That's next:

## <font color="#f96d7b"><b>The `spiral` function </b> <font size = "-1"> [10 points]</font>

Next, you'll build another <i>single-path</i> recursive function, named `spiral`. It will be similar to `tri`.

First, a picture from the call `spiral(100, 90, 0.9)`:

<img src = "https://www.cs.hmc.edu/twiki/pub/CS5Fall2022/Lab2Turtle/spiral_90.png">

The idea is to write `spiral(initialLength, angle, multiplier)`
+ `initialLength` is the length of the first "spiral leg"
+ `angle` is the amount the turtle turns after each leg
+ `multiplier` is the multiplier used, with each spiral-leg!

Take a look:
+ It won't run as-is...
+ See if you can fill in lines 22-24
+ Then, run it by uncommenting the call to `spiral(100, 90, 0.9)` on line 28
"""

import ColabTurtlePlus.Turtle as t

t.clearscreen()      # it's good to start every cell with this
t.setup(1000,1000)     # setup the drawing area to be 500 pixels x 500 pixels
t.showborder()       # show the border of the drawing area

t.bgcolor("AliceBlue")   # adjust to your preferences!
t.shape("turtle2")
t.speed(10)
t.width(2)

def spiral(initialLength, angle, multiplier):
    """Spiral-drawing function.  Arguments:
       initialLength = the length of the first leg of the spiral
       angle = the angle, in degrees, turned after each spiral's leg
       multiplier = the fraction by which each leg of the spiral changes
    """
    if initialLength <= 1 or initialLength > 1000:
        return      # No more to draw, this base case stops the recursion
    else:
        t.forward(initialLength)  # You will want a call to forward on this line...
        t.left(90) # turn left for 90 degrees
        initialLength = initialLength*multiplier
        spiral(initialLength, 90, multiplier) # You will want to recurse here! That is, make a new call to spiral:
        # spiral(100, 90, 0.9) # use this: spiral( _______________  , ______  , ____ )  # What inputs?!

        pass # delete this empty statement later


spiral(200, 90, 0.9)

"""### <font color = "blue"> **Additional hints/explanation on `spiral`...**

It's helpful to take in `spiral`'s self-similarity. Here's an overview and explanation from the slides:


<img src = "https://www.cs.hmc.edu/twiki/pub/CS5/Lab2Turtle/spiralslide.png" height="400px">



The spiral function should use the turtle drawing functions to create a spiral that
+ Draws its first segment of length `initialLength`
+ then turns `angle` degrees to the left after that segment, then
+ calls `spiral` recursively, using `multiplier` to change its first argument - the second and third arguments won't change!

**Base cases!**

Note that, for your base case, the code checks if the `initialLength` is too big or too small... and then stops.

<hr>

For fun, you might try these calls.
```
spiral(100, 90, 0.9)
spiral(100, 170, 0.95) # More of a "star" than a spiral...
spiral(400, 120, 0.8) # A triangular spiral...
```

Variations welcome!

Below is a picture from our version of the call `spiral(300, 170, 0.99)`:

<img src = "https://www.cs.hmc.edu/twiki/pub/CS5Fall2022/Lab2Turtle/spiral_170.png" height="150px">


Create a spiral you like and leave your favorite spiral in the notebook --

We look forward to seeing all of the <i>spiraling</i> going on...

## <font color = "blue"> <b>Turtle Task #3: <i>Recursive Chai</i></b>  </font>

The `tri` and `spiral` examples demonstrate what's called <i><u>single-path</u></i> recursion:
+ the recursive calls are made a single time, so that
+ there is a single, step-by-step path taken.



But for us, the <i>spiral</i> into the depths of recursion has only begun!

Next up: <i><b>Branching</b></i> recursion!

## <font color="#f96d7b"><b>The `chai` function: branching recursion </b> <font size = "-1"> [10 points]</font>

Now to _branching-recursion_.

Branching is when recursion is at its most "magical."

As a result, _writing_, branching recursion can feel especially mind-bending!

In the end, all of the "magic's" tricks are revealed: it's fully understandable. (It does take some getting used to.)

 Here is a starter code for the `chai` function from class. It's not recursive, yet:
"""

# The chai function

import ColabTurtlePlus.Turtle as t

t.clearscreen()      # it's good to start every cell with this
t.setup(500,500)     # setup the drawing area to be 500 pixels x 500 pixels
t.showborder()       # show the border of the drawing area

t.bgcolor("AliceBlue")   # adjust to your preferences!
t.shape("turtle2")
t.speed(1)
t.width(2)

def chai(size):
    """Our chai function!"""
    if (size < 5):
        return
    else:
        t.forward(size)
        t.left(90)
        t.forward(size/2)
        t.right(90) # turn right for 90 degrees

        # first you'll recurse here

        t.right(90) # turn back for 180 degree (two t.right(90))
        t.forward(size)
        t.left(90)

        # then you'll recurse here, as well!

        t.left(90) # turn back for 180 degree (two t.left(90))
        t.forward(size/2)
        t.right(90)
        # t.backward(size)
        t.backward(size/2)

        size = size/2

        # return
        return chai(size)

#
# This runs the chai function:
#
chai(200)

"""When you run this code with `chai(100)`, you should see a side-view "T"!


Take a moment to digest what `chai` draws:
+ How is the final "T" shape formed? You might act it out, on paper or in person!
+ Notice where in the "T"  the two hash-tagged `# recurse here` comments in the code, at the "T"'s top ends...
+ Next, you'll add one recursive branch, then a second:

To that end, add one branch of recursion to `chai`:

+ First, paste this recursive call: `chai(size/2)` between the two calls to `t.right(90)` (i.e., where the first recursion is called for.

Try it out!

<hr>

<b>Next</b>, add a second branch.

+ That is, place a _second_ recursive call to `chai(size/2)` between the two calls to `t.left(90)`

It's nothing more than a second branch, __but__ because it's called recursively on _all_ of the subbranches, the resulting work - and visual intricacy - is _much more_ than doubled!

Again, try it out!

<hr>

In the end, branching recursion works by creating a smaller version of the overall structure at <b><i>more than one location</i></b> within that structure.


Take a moment again here to analyze the final `chai` function, the branching-recursion one:
+ Why does it draw such a complex figure?
+ Again, it might help to act it out -- or use paper. You'll see that a _lot_ of bookkeeping is going on! The process is keeping track of where in the recursion it is ... <i>at all times</i>.

<br>

<font size = "+1.5">Key idea: <b>Be sure to end where you began</b>

***One key*** to making branching recursion "work" is _making sure that your turtle __ends__ at the same __location__ that it begins, and ends up __facing the same direction__._ That ensures the statements after the recursive calls are moving the turtle as expected -- and that the subsequent drawing is "right on schedule"!

No need to customize `chai` here.

Instead, you'll customize it with `svtree`, our <i>side-view tree</i>, next:

## <font color = "blue"> <b>Turtle Task #4: The `svtree` function</b>  </font> <font size = "-1"> [10 points]</font>


Next, you'll write another branching example: the _side-view_ tree.

"Branching" seems like a particularly appropriate descriptor in this case!

The idea is to create a function that draws the _side view_ of a tree, hence `svtree`. Read over this docstring to get a sense of the two arguments. Then, look over the outline and images below the code:
"""

import ColabTurtlePlus.Turtle as t

t.clearscreen()      # it's good to start every cell with this
t.setup(500,500)     # setup the drawing area to be 500 pixels x 500 pixels
t.showborder()       # show the border of the drawing area

t.bgcolor("AliceBlue")   # adjust to your preferences!
t.shape("turtle2")
t.speed(1)
t.width(2)
# t.left(90)

def svtree(trunklength, levels, angle):
    """svtree: draws a side-view tree
       trunklength = the length of the first line drawn ("the trunk")
       levels = the depth of recursion to which it continues branching
    """
    if levels == 0:
        return
    else:
      t.forward(trunklength) # draw the branch
      t.right(angle) # turn right
      svtree(trunklength*0.8, levels-1, angle) # recursion to turn left

      t.left(2*angle) # the head turns left

      svtree(trunklength*0.8, levels-1, angle) # recurison to move right

      t.right(angle) # the head goes back to the middle


      t.backward(trunklength) # draw back the branch

      pass # delete this empty statement later

#
# setup - move the turtle backward a bit:
#
t.penup()
t.backward(150)
t.pendown()

# Go!  One example:
svtree(100, 6, 30)

# try svtree(100,5)

"""#### **Try more branches!**

Once you have the `svtree` function working, alter it so that it has three or more branches, instead of only two...

- You can get some very dense "foliage" very quickly.
- Even more "life-like" results are possible if you use non-identical branching angles and size multipliers.
- Also, you could have the `pensize` or `pencolor` depend on the value of `levels`.
- If you make the final "level" red, you can create an apple tree.
   - See the `dot` example from `tri` for other ways to add fruit to a tree...
- Or, if you make that final "level" a random color, you can produce fall-foliage-type effects...

### <font color = "blue"> **More on `svtree`...**

Before diving in, take a look at two examples and some analysis. First, here is an example of the possible output when `svtree(50, 2)` is run:


<img src = "https://www.cs.hmc.edu/twiki/pub/CS5Fall2022/Lab2Turtle/svtree_2.png" height="142px">

Caution: because the function draws a sideways tree, it can go off the screen really fast. The lines of code at the bottom (`t.penup()` through `t.pendown()`) ensure that that doesn't happen, so make sure that you call svtree _after_ them.

Here is an example of the output from our function when `svtree(128, 6)` is run:

<img src = "https://www.cs.hmc.edu/twiki/pub/CS5Fall2022/Lab2Turtle/svtree_6.png" height="200px">


Note that this __really__ is side-view!

Also, if `svtree(50, 0)` is run, the result should be no drawing at all. _The base case occurs when `levels` equals 0._

<br>

<font size = "+1.5"> <b> Strategy and analysis </font></b>

**Base case:**   for `svtree`, you want to draw nothing (and `return` from `svtree`) when `levels == 0`.

**Recursive case:**   We tackle it conceptually.

Here is a picture showing the self-similar breakdown of `svtree` (from the Gold slides). This is, in fact, an almost complete map of the svtree code!


<img src = "https://www.cs.hmc.edu/twiki/pub/CS5/Lab2Turtle/svtree.png" height="442px">


The key to happiness with recursive drawing is this: ___the pen must be back at the start (root) of the tree at the end of the function call, and the turtle must be facing in the original direction!___ That way, each portion of the recursion "takes care of itself" relative to the other parts of the image. Here are the steps:

- Go forward the `trunklength`.
- Turn left some amount.
- Recur! (call `svtree` with a fraction of the `trunklength` and 1 fewer levels).
- Turn right some amount (if you want to be symmetric, turn right by double the amount you turned left).
- Recur again! (make the same call to `svtree` with a fraction of the `trunklength` and 1 fewer levels).
- _Finish up, part 1_: Turn left so that the turtle is facing its original direction (if your tree is symmetric, the same as the original left turn).
- _finish up, part 2_: Go __backward__ the original `trunklength`.

<br>

**Notes and Hints**

- Don't worry about the exact angle of branching...
- Don't worry about the exact amount of reduction of the trunklength in sub-branches, etc.
- Design your own tree by making aesthetic choices for each of these!

Also, calling `t.left(90)` before the code at the bottom will yield a more traditional, skyward, tree pose!

For the fourth task, as with the previous ones,
+ leave in the notebook your final/favorite tree, one that's different from this page's provided examples.

### _What - only two branches?!_    

 As the branching factor increases, things can get __icy__... or, perhaps, numbing:

## <font color = "blue"> <b>Turtle Task #5: The `flakeside` function </b> <font size = "-1"> [10 points]</font>

A challenge! The Koch Snowflake is an example of _deeply_ branching recursion.

The Koch snowflake is a fractal with three identical sides—it's the sides themselves that are defined recursively, not the set of three of them.

Because of this, we provide the overall `snowflake` function for you to use—it's here.

<b>Note</b> - you won't be able to use the <tt>snowflake</tt> function until you define `flakeside` below.
"""

import ColabTurtlePlus.Turtle as t

t.clearscreen()      # it's good to start every cell with this
t.setup(500,500)     # setup the drawing area to be 500 pixels x 500 pixels
t.showborder()       # show the border of the drawing area

t.bgcolor("AliceBlue")   # adjust to your preferences!
t.shape("turtle2")
t.speed(10)
t.width(2)

def snowflake(sidelength, levels):
    """Fractal snowflake function, complete.
       sidelength: pixels in the largest-scale triangle side
       levels: the number of recursive levels in each side
    """
    flakeside(sidelength, levels)     # needs to be implemented - see below
    t.left(120)
    flakeside(sidelength, levels)
    t.left(120)
    flakeside(sidelength, levels)
    t.left(120)

"""### <font color = "blue"> **Writing the `flakeside` function!**

Your task is to implement `flakeside(sidelength, levels)`, which will draw one snowflake side:

There is a starter code below. First, here is a graphical summary of a snowflake-side's structure:

<img src = "https://www.cs.hmc.edu/twiki/pub/CS5/Lab2Turtle/flakeside.png" height="542px">
"""

import ColabTurtlePlus.Turtle as t

t.clearscreen()      # it's good to start every cell with this
t.setup(500,500)     # setup the drawing area to be 500 pixels x 500 pixels
t.showborder()       # show the border of the drawing area

t.bgcolor("AliceBlue")   # adjust to your preferences!
t.shape("turtle2")
t.speed(10)
t.width(2)

def flakeside(sidelength, levels):
    """ flakeside draws _one side_ of the fractal Koch snowflake
    """

    # see hints below! This function is _deeply_ recursive!
    if levels == 0:
      t.forward(sidelength/3)
      return
    else:
      flakeside(sidelength/3, levels - 1)
      t.right(60)

      flakeside(sidelength/3, levels - 1)
      t.left(120)

      flakeside(sidelength/3, levels -1)

      t.right(60)
      flakeside(sidelength/3, levels - 1)

      pass

def snowflake(sidelength, levels):
  """
  """
  if levels == 0:
    t.forward(sidelength)
    return
  else:
    flakeside(sidelength, levels)

    t.left(120)
    flakeside(sidelength, levels)

    t.left(120)
    flakeside(sidelength, levels)

    pass # remove this empty statement later




#
# try it!
#
t.penup()
t.goto(-200,0)  # move the pen to a "southwest" corner...
t.pendown()


snowflake(500,2)
# last(100, 2)

"""### <font color= "salmon"> Hints for  flakeside



- A base-case Koch snowflake side is simply a straight line of length `sidelength`!
- Other than the base case, you should never draw a line directly. Instead, use a recursive call to `flakeside`.
- Each recursive level replaces the _middle third_ of the snowflake's side with a "bump," i.e., two sides that would be part of a one-third-scale equilateral triangle.
- Notice there are four _sub-sides_ to each flake side. This means that `flakeside` will call itself recursively ___four times___!
- At the three spots _between_ those four calls, there will be an appropriate turn...
- Thus, the recursive case will include seven total lines (4 recursions and three turns).

#### **Calls to try...**

- Try `flakeside(300, 0)`—make sure you get a straight line
- Try `flakeside(300, 1)`—make sure you get a four-segment contour
- Try `flakeside(300, 2)`—make sure you get four "level-1" flakesides
- Try `flakeside(300, 3)`—pretty! and pretty cool! Olaf approves.


Remember that `flakeside` is creating ___only one___ of the three sides of the snowflake!

- Because of this, it does __not__ have to end in the same location as it begins.
- After all, if it did, all three sides of the overall snowflake would be on top of one another.

### From `flakeside` to `snowflake`

Once your `flakeside` function works, try out `snowflake`!

- The `snowflake` function simply calls `flakeside` three times.
- Depending on the directions that `flakeside` uses, you may need to change the `left`s in `snowflake` to `right`s.
- Examples to try might include `snowflake(300, 2)` and `snowflake(300, 3)`

Like `svtree`, if you are having trouble seeing everything you may need to move the turtle at the beginning. Try:
```
t.penup()
t.setposition(x, y)
t.pendown()
```
Put the coordinates you want into `setposition`. Note that `(0, 0)` is the upper left corner.

Here are images of four different values of `levels` for a snowflake, `0`, `1`, `2`, and `3`:


<img src = "http://www.cs.hmc.edu/~cs5grad/cs5/koch.png" height="442px">


Consider the following script:
```
t.penup()
t.goto(-200,-100)  # move the pen to a "southwest" corner...
t.pendown()
snowflake(300,2)   # two recursive levels deep!
```
Here's an in-progress run from this script:

<img src = "https://www.cs.hmc.edu/twiki/pub/CS5Fall2022/Lab2Turtle/snowflake_partial.png" height="442px">

Try it here:
"""

#
# Drawing the Koch snowflake
#

t.clearscreen()      # it's good to start every cell with this
t.setup(500,500)     # setup the drawing area to be 500 pixels x 500 pixels
t.showborder()       # show the border of the drawing area

t.bgcolor("AliceBlue")   # adjust to your preferences!
t.shape("turtle2")
t.speed(10)
t.width(2)



# You'll need both the snowflake function (provided) and flakeside, which you will have written:

t.penup()
t.goto(-200,-100)  # move the pen to a "southwest" corner...
t.pendown()

snowflake(300,2)   # two recursive levels deep!

#
# Try three - or four - levels, as well.

"""#### More snow!

There is lots more about the Koch snowflake and its kin...   

Google around and you'll find that branching recursion and fractals are one and the same thing:

- [the Koch Snowflake](https://en.wikipedia.org/wiki/Koch_snowflake)
- [the Menger Sponge](https://en.wikipedia.org/wiki/Menger_sponge)
- [Julia Sets](https://en.wikipedia.org/wiki/Julia_set#/media/File:Julia_set,_plotted_with_Matplotlib.svg)
- [space-filling curves](https://en.wikipedia.org/wiki/Space-filling_curve)


<br>

# <font color = "dodgerblue"> **Submitting...**

To submit,
+ first, download your <tt>.ipynb</tt> notebook - with your turtle images present
+ then upload the resulting file to GradeScope

You're set!

<br>

If you're in the mood for more turtle (or have homework in other courses to procrastinate...), read on!

### More turtle?

<b>Extra credit options</b>

If you enjoy creating turtle graphics, whether recursive or not, you're invited to try more!

+ For extra-credit of up to +8.42 points, include additional cell(s) with your own custom-designed turtle creations...  (and the code used to create them)
  + This is your "turtle-graphics portfolio"!
+ In fact, you may already have a portfolio! If you've already created a work you like, you can always copy the code to a new cell and then continue working/developing from there. It's completely OK if it was accidental!
+ Feel free to build something new, whether by designed or <i>unencumbered by strategic assembly</i> ...
+ Since lab does usually have as much e.c., if you do create additional turtle-artwork, please submit you under this week's e.c. problem, <tt>hw2pr5</tt>


The grutors - and we - look forward to your turtle-visions!

<br>

<i>Happy turtling!</i>
"""

# run this cell to create a good-job-for-finishing star 🤩

t.clearscreen()      # it's good to start every cell with this
t.setup(500,500)     # setup the drawing area to be 500 pixels x 500 pixels
t.showborder()       # show the border of the drawing area

t.bgcolor("AliceBlue")   # adjust to your preferences!
t.shape("turtle2")
t.speed(10)
t.width(2)

def star(n):
    """ draws a star!
        call with star(5)
    """
    if n == 0:
        return
    else:
        t.forward(100)
        t.right(144)
        star(n-1)

t.fillcolor("gold")
t.begin_fill()
star(5)
t.end_fill()

t.penup()
t.backward(100)
t.pendown()