# Bullet-Point-Adder
It's a practice program for python beginners.

Project: Adding Bullets to Wiki Markup

When editing a Wikipedia article, you can create a bulleted list by putting 

each list item on its own line and placing a star in front. But say you have 

a really large list that you want to add bullet points to. You could just type 

those stars at the beginning of each line, one by one. Or you could auto-

mate this task with a short Python script.

The bulletPointAdder.py script will get the text from the clipboard, add 

a star and space to the beginning of each line, and then paste this new 

text to the clipboard. For example, if I copied the following text (for the 

Wikipedia article “List of Lists of Lists”) to the clipboard:

Lists of animals

Lists of aquarium life

Lists of biologists by author abbreviation

Lists of cultivars

and then ran the bulletPointAdder.py program, the clipboard would then con-

tain the following:

* Lists of animals

* Lists of aquarium life

* Lists of biologists by author abbreviation

* Lists of cultivars

This star-prefixed text is ready to be pasted into a Wikipedia article as a 

bulleted list.

Step 1: Copy and Paste from the Clipboard

You want the bulletPointAdder.py program to do the following:

1. Paste text from the clipboard

2. Do something to it

3. Copy the new text to the clipboard

That second step is a little tricky, but steps 1 and 3 are pretty straight-

forward: They just involve the pyperclip.copy() and pyperclip.paste() func-

tions. For now, let’s just write the part of the program that covers steps 1 

and 3. Enter the following, saving the program as bulletPointAdder.py:

#! python3

# bulletPointAdder.py - Adds Wikipedia bullet points to the start

# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

# TODO: Separate lines and add stars.

pyperclip.copy(text)

The TODO comment is a reminder that you should complete this part of 

the program eventually. The next step is to actually implement that piece 

of the program.

Step 2: Separate the Lines of Text and Add the Star

The call to pyperclip.paste() returns all the text on the clipboard as one big 

string. If we used the “List of Lists of Lists” example, the string stored in 

text would look like this:

'Lists of animals\nLists of aquarium life\nLists of biologists by author 

abbreviation\nLists of cultivars'

The \n newline characters in this string cause it to be displayed with 

multiple lines when it is printed or pasted from the clipboard. There are 

many “lines” in this one string value. You want to add a star to the start of 

each of these lines.

You could write code that searches for each \n newline character in the 

string and then adds the star just after that. But it would be easier to use the 

split() method to return a list of strings, one for each line in the original 

string, and then add the star to the front of each string in the list.

Make your program look like the following:

#! python3

# bulletPointAdder.py - Adds Wikipedia bullet points to the start

# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.

lines = text.split('\n')

for i in range(len(lines)): # loop through all indexes in the "lines" list

 lines[i] = '* ' + lines[i] # add star to each string in "lines" list

pyperclip.copy(text)

We split the text along its newlines to get a list in which each item is one 

line of the text. We store the list in lines and then loop through the items in 

lines. For each line, we add a star and a space to the start of the line. Now 

each string in lines begins with a star.

Step 3: Join the Modified Lines

The lines list now contains modified lines that start with stars. But 

pyperclip.copy() is expecting a single string value, not a list of string values. 

To make this single string value, pass lines into the join() method to get a 

single string joined from the list’s strings. Make your program look like the 

following:

#! python3

# bulletPointAdder.py - Adds Wikipedia bullet points to the start

# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.

lines = text.split('\n')

for i in range(len(lines)): # loop through all indexes for "lines" list

 lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)

When this program is run, it replaces the text on the clipboard with 

text that has stars at the start of each line. Now the program is complete, and 

you can try running it with text copied to the clipboard.

Even if you don’t need to automate this specific task, you might want to 

automate some other kind of text manipulation, such as removing trailing 

spaces from the end of lines or converting text to uppercase or lowercase. 

Whatever your needs, you can use the clipboard for input and output.
