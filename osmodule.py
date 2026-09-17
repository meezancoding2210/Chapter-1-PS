#Write a python program to list all files and directories in a specified path.
import os #importing the os module 
path = r"C:\Users\padoa\Downloads" #path to the directory i want to print.
dir_list = os.listdir(path) #function
print("Files and directories in '", path, "' :") 
print(dir_list) 
