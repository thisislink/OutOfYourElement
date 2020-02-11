# OOYE – Code Explained Part V: Let’s Get Functional

Welcome to Part V. If you’ve missed the previous lessons, be sure to check them out here:

[Part I – Game Titles & Secret Messages](https://github.com/thisislink/OutOfYourElement/blob/master/OOYE%20%E2%80%93%20Code%20Explained%20Part%20I:%20Game%20Titles%20and%20Secret%20Messages.md)

[Part II – Hold My Poodle](https://github.com/thisislink/OutOfYourElement/blob/master/OOYE%20%E2%80%93%20Code%20Explained%20Part%20II:%20Hold%20My%20Poodle.md)

[Part III – Player One Ready](https://github.com/thisislink/OutOfYourElement/blob/master/OOYE%20%E2%80%93%20Code%20Explained%20Part%20III:%20Player%20One%20Ready.md)

[Part IV – Taking Control](https://github.com/thisislink/OutOfYourElement/blob/master/OOYE%20%E2%80%93%20Code%20Explained%20Part%20IV:%20Taking%20Control.md)

Now, let’s see everything we’ve covered so far:

* ~~Displaying ‘stuff’ on the screen~~
* ~~Code comments for clarification~~
* ~~Variable declarations~~
* ~~User Input~~
* ~~Statement controls (if/then or if-else)~~
* Function declarations

This is the final part until Part VI, which will just be all of the code I wrote to create Out Of Your Element. So, in this final part to explain simple Python programming, I’m going to teach you about functions.

In Part IV, we left off with the following code:

```python
#Declare variable that will store default player input to check against
playerReady = 'S'

#Ask player to type S to start playing the game
playerInput = raw_input("Type S to start the game.")

#Check that the player enters the correct letter to start the game
while playerInput != playerReady:
    playerInput = raw_input("Type the letter S to start the game: ")
if playerInput == playerReady:
    startgame()
```

The startgame() is a function. 

You can think of a function as basically a way to group a bunch of statements together to perform one thing, instead of having a bunch of individual statement performing each task separately.

I’ve always thought of functions as a way to improve readability of code, which is especially useful when you have hundred of lines of code to go through. 

Instead of searching for one or two lines of code that you might need to fix or improve, you know exactly where the problem lies if you use functions, because the lines of code will be in the function you create.

An example that might help you understand functions better, is to think of functions like a soda/vending machine. The soda/vending machine has to be able to do several things in order for you to get your soda or snack. It has to be able to accept money, count the money to properly pay for your soda/snack, give you change back if too much money is put into it, check if the snack/soda is out, and ultimately it has to be able to give you your soda/snack.

You could do all of those things in single statements based on what I’ve shown you in the previous parts; however, you can instead create an entire soda/snack machine function.

Just like with variables and still keeping in mind naming conventions ([Part II](https://github.com/thisislink/OutOfYourElement/blob/master/OOYE%20%E2%80%93%20Code%20Explained%20Part%20II:%20Hold%20My%20Poodle.md)), you can name functions anything you’d like. 

So, with the startgame() function, it will do exactly what I’ve named it to do, it will start the game; however, this is only after the previous check was in place that the player entered the correct letter ‘S’ to start the game (which we covered – [Part IV](https://github.com/thisislink/OutOfYourElement/blob/master/OOYE%20%E2%80%93%20Code%20Explained%20Part%20IV:%20Taking%20Control.md)).

Now, there are basically two types of functions. Functions that take arguments and functions that don’t. What that means is that when a function takes an argument, it needs something before it can actually work, just like a soda/vending machine needs money before it can give you anything back (unless it’s broken which is a different story).

Let me show you some examples how this would look writing it in Python:

```python
startgame() #function call that takes no arguments
startGame(playerInput) #function call that takes one argument
sodamachine(takesBills, takesChange) #function call that takes arguments
sodaMachine() '''function call that takes no arguments 
and gives free soda apparently'''
```

So, as you can see, you can create a function that takes no arguments or takes several. You might be wondering if there is a maximum number of arguments a function can take, and there isn’t; however, if you want to keep clean, readable/understandable code, it’s best to keep the function parameters/arguments to a minimum. I recommend between 0 and 4 maximum.

You might have noticed in my comments in the examples for functions, I wrote *function call*, which is important, because creating a function is slightly different from calling a function.

Look at this example and see if you can spot the difference between which one is a function call and which one is how you’d create a function:

```python
gameMap()
gameMap():
    print "\n-------x-"
```

Hopefully, you noticed that the function call has no colon after the parenthesis, and the creation of a function has a colon, followed by statements to do things (all the things you learned in the previous parts).

That’s going to conclude these lessons. You should have a mastered the basics of being able to not just program using the Python language, but you should be able to create your own basic game because everything I’ve shown you is everything I used to create my simple game.

In Part VI, you’ll get a look at the entire code to “*Out Of Your Element*” and more importantly, you’ll understand what’s going on behind the scenes since I’ve taught you everything you need to know to understand it.

However, before I let you go, let me make sure you’ve mastered functions….

## Final Boss
1. Create a function that tells you how many health points you have
2. Create a function that tells you if you’re alive or dead based on how many health points you have, and make this function take at least one parameter.

That’s it! I’ll see you in Part VI!
