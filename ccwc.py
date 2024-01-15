#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:11:39 2024

@author: anirbanchatterjee
"""

import sys
import os.path

"""
Function to get the right byte size for string using utf-8 encoding, 
using size of function return size of the string object

"""

def utf8len(s):
    return len(s.encode('utf-8'))

"""
Wrapper function to call the byte size function

"""

def getBytesize(filename):
    size = 0
    f = open(filename)
    for x in f:
        size_of_byte = utf8len(x)
        size = size + size_of_byte + 1
    f.close()
    return size
    

"""
Function to get the line numbers for a file

"""

def getLinenumber(filename):
    count_of_line = 0
    f = open(filename)
    for x in f:
        count_of_line = count_of_line + 1
    f.close()
    return count_of_line

"""
Function to get the number of words in file, currently getting slighltly 
lower number than wc command

"""

def getWordcount(filename):
    count_of_word = 0
    f = open(filename)
    for x in f:
        count = x.strip().split(" ")
        if count != ['']:
            count_of_word = count_of_word + len(count)
    f.close()
    return count_of_word

"""
Function to get the number of characters in file

"""

def getCharcount(filename):
    count_of_char = 0
    f = open(filename)
    for x in f:
        count = len(x)
        count_of_char = count_of_char + count + 1
    f.close()
    return count_of_char

"""
Calling the different functions based on passed arguments

"""


def main():
    
    """
    To handle input from stdin
    
    """
    
    if not sys.stdin.isatty():
        received = sys.stdin
        f = open("test_new.txt","w")
        for line in received:
            f.write(line)
        filename = "test_new.txt"
        f.close()
        # if os.path.isfile(sys.argv[1]):
        #     filename = sys.argv[1]
        #     print (getLinenumber(filename),getWordcount(filename), getBytesize (filename), filename)
            
        # else:
                
        value = sys.argv[1]
        if value == "-c":
            print (getBytesize (filename))
        if value == "-l":
            print (getLinenumber(filename))
        if value == "-w":
            print (getWordcount(filename))
        if value == "-m":
            print (getCharcount(filename))
      

        """
        
        To handle arguments passed in commandline
        
        """                                                                                              
    
    else:
        if os.path.isfile(sys.argv[1]):
            filename = sys.argv[1]
            print (getLinenumber(filename),getWordcount(filename), getBytesize (filename), filename)
            
        else:
                
            value = sys.argv[1]
            filename = sys.argv[2]
            if value == "-c":
                print (getBytesize (filename), filename)
            if value == "-l":
                print (getLinenumber(filename), filename)
            if value == "-w":
                print (getWordcount(filename), filename)
            if value == "-m":
                print (getCharcount(filename), filename)
            
"""
Calling the main functions to initiate

"""

if __name__ == "__main__":
    main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

