#!/usr/bin/python3
try:
    '''opening a file for writting'''

    word_list = ["hello\n", "worl\n", "week5\n", "test123\n", "PLP class of 2024\n"]
    fin = open("my_file.txt", 'w')
    for word in word_list:
        fin.write(word)
    fin.close()


    '''appending to the file'''
    fapen = open("my_file.txt", "a")
    append_list = ["python3\n", "is\n", "fun\n"]
    for wrd in append_list:
        fapen.write(wrd)
    fapen.close()

    '''reading from the file'''
    fout = open("my_file.txt", "r")
    for words in fout.readlines():
        print(words)
    fout.close()
except FileNotFoundError as err:
    print(err)
except PermissionError as perr:
    print(perr)
finally:
    print("all errors checked back i will run even in error or no error':)'")
