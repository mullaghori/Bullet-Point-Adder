

#BulletPointAdder.py adds bullets to the start of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
	lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)