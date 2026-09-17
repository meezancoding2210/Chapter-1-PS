#write a python program to print the following string in a specific format.
import pyfiglet
''' 
This code uses the pyfiglet library to create ASCII art from text.
we can specify the text and the font to use for the ASCII art. 
'''
text = "Python is Fun!"
font = "slant" #we can change the font to any available font.
ascii_art = pyfiglet.figlet_format(text, font=font)
print(ascii_art)