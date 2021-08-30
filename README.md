>From the book: Automate the Boring Stuff with Python. Writer: Al Sweigart 

# ADDING BULLETS to WIKI MARKUP

It's a practice project for python beginners.

When editing a Wikipedia article, you can create a bulleted list by putting each list item on its own line and placing a star in front. But say you have a really large list that you want to add bullet points to. You could just type those stars at the beginning of each line, one by one. Or you could mate this task with a short Python script.
 
***The bulletPointAdder.py script will get the text from the clipboard, add a star and space to the beginning of each line, and then paste this new text to the clipboard.
For example, if I copied the following text (for the Wikipedia article “List of Lists of Lists”) to the clipboard:***
```
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
```
***and then ran the bulletPointAdder.py program, the clipboard would then contain the following:***
```
* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars
```
***When your program is run, it should replaces the text on the clipboard with text that has stars at the start of each line. The star-prefixed text should be ready to be pasted into a Wikipedia article as a bulleted list.*** 

**HINT: You want the bulletPointAdder.py program to do the following:**
**-1. Paste text from the clipboard**
**-2. Do something to it**
**-3. Copy the new text to the clipboard
That second step is a little tricky, but steps 1 and 3 are pretty straightforward: They just involve the `pyperclip.copy()` and `pyperclip.paste()` functions**

Even if you don’t need to automate this specific task, you might want to automate some other kind of text manipulation, such as removing trailing spaces from the end of lines or converting text to uppercase or lowercase. Whatever your needs, you can use the clipboard for input and output.


