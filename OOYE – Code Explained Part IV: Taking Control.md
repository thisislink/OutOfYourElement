# OOYE – Code Explained Part IV: Taking Control

Welcome to Part IV. If you’ve missed the previous lessons, be sure to check them out here:

[Part I – Game Titles & Secret Messages](https://github.com/thisislink/OutOfYourElement/blob/master/OOYE%20%E2%80%93%20Code%20Explained%20Part%20I:%20Game%20Titles%20and%20Secret%20Messages.md)

[Part II – Hold My Poodle](https://github.com/thisislink/OutOfYourElement/blob/master/OOYE%20%E2%80%93%20Code%20Explained%20Part%20II:%20Hold%20My%20Poodle.md)

[Part III – Player One Ready](https://github.com/thisislink/OutOfYourElement/blob/master/OOYE%20%E2%80%93%20Code%20Explained%20Part%20III:%20Player%20One%20Ready.md)

Now, let’s see what we’ve covered so far:

* ~~Displaying ‘stuff’ on the screen~~
* ~~Code comments for clarification~~
* ~~Variable declarations~~
* ~~User Input~~
* Statement controls (if/then or if-else)
* Function declarations

In this part, I’m going to teach you about control statements, hence why I’ve used *Taking Control* in the title.

**Note: Programming in Python is not the first language I ever learned to program in, and due to that, you'll see me talk about if-then or if-else interchangeably; however, when it comes to the actual code part, that is the importance. I just wanted to note, not to get confused by me saying if-then or if-else, because they are the same for the context of me teaching you how to make games in Python and the ideas/examples I give.**

Following suit from our previous lessons, we need to update our code. This time, we need to update it using control statements, which are basically some of the most crucial ways to get your game to function how it should.

Let me explain further using some simple examples outside of games. 

If you’re hungry, then you’ll eat. If you’re tired, then you’ll sleep, and if you’re not tired, then you won’t sleep, and sometimes while you’re asleep you’ll have dreams.

Those examples can be turned into what is called if-else statements, and while statements. If you go back and read them again, you can pick out the if-then parts, the while, as well as the actions that would be performed during each.

Example:

**IF** you're hungry, then you'll eat.

**IF** you're tired, then you'll sleep, **ELSE IF** you're not tired, then you won't sleep.

**WHILE** you're asleep, you'll have dreams.

**IMPORTANT: You'll need to know/memorize logic symbols, which really won't be too hard in the long run, because you'll use them often so memorization should come naturally. Logic symbols/words/statements are part of IF-ELSE and WHILE statements. In the examples, they consist of the and's, the not's and the connections that need to be made between the control words (IF) and the actual actions (hungry).**

Here's a list you can quickly reference:

* = (equal) Sets equal to something i.e. playerOne = “James”
* == (equal to) compares that it’s the same as something else i.e. 4 == 4
* <= (less than or equal to)
* ```>= (greater than or equal to)```
* != (not equal) Yes the exclamation point means NOT
* and
* or
* not
* True
* False


Alright, I think that’s enough of our eat, sleep, dream sequence non-code examples, let me show you how you’d actually do those control statements in Python.

Continuing with our previous game code from the last part:

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
That’s going to be it! Fairly simple right?!

Oh, you have a question…What’s the startgame() at the end? That’s a function, and what I’ll be covering in the next lesson! :smile:

You should have a good grasp on control statements, and I’m going to give you a final boss to defeat just to make sure! 

Remember, control statements can really be applied to everything in life that we do such as eating, sleeping, driving, talking, etc., because they’re that simple to understand. Also, don’t be surprised if you start thinking about them more often in your everyday life as you do things.

## Final Boss
To reinforce what you’ve learned here, here’s a final boss for you to destroy, in order to prove you’ve mastered Part IV.

1. Create a variable that stores your name (or your gamertag if you prefer).
2. Properly create check system using a while statement that checks the name the player enters is the correct name.

You’ve now mastered 5 of the 6 bullet list items. If you have any questions contact me/leave me a comment.

That’s it! See you in Part V.
