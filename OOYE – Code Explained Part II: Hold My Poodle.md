# OOYE – Code Explained Part II: Hold My Poodle

Hey you! Welcome to part II. (That rhymes, haha). Anywho, if you missed Part I or you need a refresher, head on over to [Part I](https://github.com/thisislink/OutOfYourElement/blob/master/OOYE%20%E2%80%93%20Code%20Explained%20Part%20I:%20Game%20Titles%20and%20Secret%20Messages.md) and then come back.

Welcome back, you’re all caught up now I hope. So let’s dive in.

First, let’s refer to the bullet list I created back in Part I:

* Displaying ‘stuff’ on the screen
* Code comments for clarification
* Variable declarations
* Statement controls (if/then)
* User input
* Function declarations

In the first part, you MASTERED the first two bullet items. How do I know that? Just like with many video games, there are final bosses to beat, and since we’re making our first game, I gave you a final boss at the end of the lesson. If you completed it with no problems, I know you MASTERED the first two bullets in the list.

Did you have some troubles? Did the final boss beat you this time? Tell me about about in the comments.

Moving on..

In this lesson, we’re going to learn about variable declarations, or what I’ve so randomly dubbed *Hold My Poodle* for the title of this article.

## Variables, What Are They Good For? Absolutely Everything
The title to this article is a reference from a scene in the movie “White Chicks”, and if you haven’t seen it here are a few clips you can check out:

[Hold My Poodle](https://www.youtube.com/watch?v=mypmNjNyB38)

[Walk How Many Miles?](https://www.youtube.com/watch?v=lBShSkjKiNU)

You might be wondering what does any of this have to do with variable declaration?

You might not think that the scenes from that movie have much to do with this lesson, but think again, because they do… or at least I’m relating them so that it will make sense.

First, in the *Hold My Poodle* clip, what is the Poodle being carried in? Hopefully, you said a bag or purse, etc. and if you didn’t know or check out the clip, [check it out](https://www.youtube.com/watch?v=mypmNjNyB38) and you can skip ahead to about 56 seconds.

Variables are like the purse that the Poodle is inside of; however, variables are also like the Poodle. 

Let me explain by asking you another question. What kind of animal is a Poodle? 

As long as we’re both thinking along the same lines, you should have said a dog. So, in other words, you define variables to do what they’re meant to do, which is hold things.

One more example from the movie and then I’ll tie all this back into games. 

In the second clip that I titled *Walk How Many Miles?*, how many miles are mentioned in the song? 

Or better yet, what is the title of the song? The answer is a thousand (1,000) miles. 

So, with that new information, I just want to state that you not only can create variables to hold words, descriptions, etc., you can also create variables that hold numbers, like money or the 1,000 miles you’re going to walk to see me. Haha, I kid.

## How to Define Variables
First, there are some naming conventions (rules), such as not starting your variable names with numbers or using Python reserved words, and if you’re interested, you can read the full documentation:

[https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

In relation to our movie clips above, to create a variable I’d go with an example like this one:

```python
dog = 'poodle'
miles = 1000
```

So, let’s now swing this all back around to games, shall we?

When you turn on a game and you’re met with the game menu, what’s something that you’re always asked to do? I’ll wait while you think of the answer…

If you guessed press **Continue/Start/Press X**, etc., you’re right, or at least you’re thinking along the same lines that I am. Even if you said something along the lines of pressing a button to play a game or something like that, we’re on the same page. The goal for the player is to play the game, but in order to do that, as the developer/programmer, you have to make that a possibility — you have the power!

Shown you the way I have!

So, let’s think about a couple more things… 

How can you create something that will let the player start playing your game? What needs to happen for the player to start the game and for the game to recognize that the player is ready?

I don’t know about you, but for me, this is where comments can start to come in handy, especially if you don’t want to get out a piece of paper or hurt your brain too much right off the bat before you’ve really gotten started.

Using what I’ve taught you, here’s what I would do:

```python
#Ask player to type S to start playing the game
print "Type S to start the game."
'''The game should be able to tell if the player is ready by the letter S the player typed'''
```

We know two things:

1. The game needs to be able to recognize when the player is ready
2. The player needs to be able to tell the game they’re ready

I’ve already shown you how to make variables — you can pretty much call them whatever you choose, keeping in mind naming conventions and other protected word restrictions that I previously mentioned and linked up for you:

[https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

So, To perform #1, here’s something that I might change the previous code to:

```python
#Ask player to type S to start playing the game
print "Type S to start the game."

#Declare variable that will store default player input to check against
playerReady = 'S'
```

You might have some questions. Such as, how would you know if the player entered the correct letter? Or pressed the right button? How do you get this information from the player?

All valid and important questions that will be answered in the upcoming user input lesson. Until then, it’s up to you to go forth and make sure you master variables!

## Final Boss
Here’s a final boss for you to destroy, in order to prove you’ve mastered Part II.

1. Create a variable that would allow the player to save their game.
2. Create a wallet variable that has $50 inside of it.
3. When creating names (variables), what keyboard character can sometimes help improve readability? Hint: [https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions](https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions)

That’s it, if you have any questions or comments leave them below and I’ll see you in part III.
