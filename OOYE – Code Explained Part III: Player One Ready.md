# OOYE – Code Explained Part III: Player One Ready

Hey there!

Welcome to Part III. If you’ve missed the previous lessons, no worries, you can go back and catch up with [Part 1](https://github.com/thisislink/OutOfYourElement/blob/master/OOYE%20%E2%80%93%20Code%20Explained%20Part%20I:%20Game%20Titles%20and%20Secret%20Messages.md) and [Part 2](https://github.com/thisislink/OutOfYourElement/blob/master/OOYE%20%E2%80%93%20Code%20Explained%20Part%20II:%20Hold%20My%20Poodle.md).

So, let’s bring out our trusty list from before and remember what we’ve covered so far:

* ~~Displaying ‘stuff’ on the screen~~
* ~~Code comments for clarification~~
* ~~Variable declarations~~
* Statement controls (if/then)
* User input
* Function declarations

In today’s explanation, we’re going to cover user input, which is why I’ve titled this one *Player One Ready*.

In the last lesson, there were a few questions you probably had that I left unanswered such as how would you know if the player entered the correct letter? Or how would you know if the player pressed the right button? How do you get this information from the player?

We’re going to continue with our code examples from part II, so by setting our *playerReady* variable equal to a default letter, and in this case the capital letter S, the game will be able to check if what the player enters matches.

Of course, we’ll also need some statement controls to get it to fully function properly, but we’ll get to that in Part IV.

Right now, we need to get the input from the player, and we do that by using the following built-in Python statement:

```python
raw_input("Your print statement will now go here instead.")
```

So, my updated code would look something like this:

```python
#Declare variable that will store default player input to check against
playerReady = 'S'

#Ask player to type S to start playing the game
playerReady = raw_input("Type S to start the game.")
```

You might have some questions. One for instance, is why didn’t I just keep the code in the same order of the last part, by asking the player for input and declaring the variable below that? Well, like I like to say, try it! :smile:

You will get an error that you’re using a variable before it’s been declared… that’s not the exact wording, and it probably looks like gibber and doesn’t make any sense if you’re a beginner, but that’s what the error will mean.

## Final Boss
To reinforce what you’ve learned here, here’s a final boss for you to destroy, in order to prove you’ve mastered Part III.

1 .Create a variable that will hold a password to a secret vault
2. Ask the player to enter their password to the secret vault

Now, with this part included, you’ve now mastered 4 of the 6 bullet list items. If you have any questions contact me or leave me a comment, and I’ll see you in Part IV!
