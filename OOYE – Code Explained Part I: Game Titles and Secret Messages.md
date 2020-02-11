### OOYE – Code Explained Part I: Game Titles and Secret Messages.md

Alright, so it’s been over a month since I released my first Python game called Out of Your Element (aka OOYE), and as I mentioned in my last update, I said I would talk about the code I wrote to create the current version that was released.

Now, when I originally started writing out this tutorial-of-sorts, it was one looooong lesson that was already 2000+ words and it wasn’t even finished!

I started thinking “Oh man, I’m overwhelmed just writing this!” My next thought was that if I was overwhelmed writing it, how was someone going to feel reading it!? That was the moment I put an end to writing the longest post ever written in post writing history! Ha, I kid of course, but that’s exactly how it felt.

So, this is part I, and each upcoming part is going to be a discussion about the basics of programming in Python with examples. In the final part (part VI), I’ll post the entire code to OOYE and give a quick overview of it, but not too much explanation will be given, because you’ll have gained enough knowledge to understand it and even make your own simple game by that time.

Let’s get down to business!

First, the entire game consists of a few basic concepts:

* Displaying ‘stuff’ on the screen
* Code comments for clarification
* Variable declarations
* Statement controls (if/then)
* User input
* Function declarations

This is part I, so I’m going to talk about the first two bullets on that list, aka Game Titles and Secret Messages (:cough: The title to this post :cough:). You’ll have those two concepts mastered by the end of this, right?! Right!

## Game Titles
If you’re new to programming, picking up a new language in general, or new to Python, the first and most exciting thing you’re going to experience is getting something to show up on the screen.

To do that in Python, you will use the print command. Here’s a line of code that performs that exact function:

```python
print "Welcome to..."
```

You can play around with the text inside the quotation marks, and if you remove one of the quotes, you should get an error if you try to run it. Test those things out for yourself. Really, do it! It’s the best way to learn. :smile:

## Secret Messages
Now that you know how to get text on the screen, let’s talk about comments or what I’ve called secret messages.

### Usefulness of Comments
Comments are really for your eyes only, because when you run your program, they’re not seen by the user/player of the software/game you’ve developed, hence why I’ve called them secret messages.

If you happen to be working with a friend or on a team, comments are also great so that the other people you’re working with can understand what you’re doing or trying to do if you’re stuck trying to figure something out.

I write my own code, and you might be thinking that it’s unnecessary to have comments writing your own code — that’s something I thought when I started programming, especially on really simple or short programs and homework assignments; however, once I started to develop my own projects, and they were longer and more complicated, was the point when I realized how helpful comments can be.

Enough about their usefulness, how do you make a comment in Python?

### How to Write Secret Messages
Simple, use the hashtag/pound/number, etc. symbol. Whatever you want to call it, use that symbol. So, your comment in your code will look something like this:

```python
#I'm a comment
```

So, let’s put together what I’ve taught you so far about game titles and secret messages:

```python
#Game Title
print "Welcome to The Best Game Ever"
```

So, from that code above, we know that the comment tells us that we’re going to be writing the title of the game on the line below the comment. Why on the line below, you might be wondering? Try it out and see!

Did you try it? You should have found that if you started the print statement on the same line after the comment, that it was part of the comment, and nothing displayed on your screen. Now, if you put your statement before the comment, you should notice that it runs normally as our previous code above runs.

Here’s an example of what I’m talking about:

```python
print "Welcome to the Best Game Ever" #Game Title
```

So, now that you know what can and cannot work with comments and actual code statements on the same lines, be careful with your commenting, because it might be tricky at first.

I recommend sticking to putting comments on separate lines from your actual code, for readability, clarity, and easier learning if you’re new to this.

**Note: You can also do multi-line comments using 3-single quotes; this might be even trickier than the single line comments, as a beginner, but it looks something like this, if you're interested in trying them out:**

```python
'''I'm a comment that can go on multiple lines;
However, if you don't close me properly, you might encounter an error.
Make sure I begin and end with 3-single quotes.'''
```

So, that’s going to be it, you know all about how to make magic appear on the screen and write secret messages that only you and your friends/colleagues helping you program can see.

In part II, I’ll discuss variable declarations, and if you don’t know what that means right now, don’t worry, you will and you’ll love it once you know all about them!

## Final Boss Lesson
To reinforce what I’ve shown you, here’s a final boss for you to destroy, in order to prove you’ve mastered part I.

1. Create a new game title of your choosing
2. Write comments that clarify what your code is suppose to do
3. Write a multi-line comment that gives a description of what your game would be about
4. What happens if you don't use any quotes when writing a print statement?

That’s it, see you in part II.
