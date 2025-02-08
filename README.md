# Endpoint - Backend Coding Challenge

## Summary

Recreate a simplied version of `mkdir`, `mv`, and `ls` commands, I've chosen to do it in Python, detailed problem statement and instructions below.

For dev purposes, I created a `DEBUG` flag on line 2. If it is set to `True`, it will show debug print statements.

You can also save commands in a file where each row is a command, and then assign the file path to `TEST_FILE` on line 4, the the program will execute the commands in the file line by line.

## Deliverable

We're expecting you to send your solution as a single page app, command line script or executable.  Some examples:

```bash
$ node directories.js
$ ruby directories.rb
$ python directories.py
$ yarn start
```

If you are doing the challenge with compiled code, please deliver both the source code and an executable or instructions for creating it.

Please share the submission via a file-sharing service such as Dropbox

## The problem

A common method of organizing files on a computer is to store them in hierarchical directories. For instance:
 
```
photos/
  birthdays/
    joe/
    mary/
  vacations/
  weddings/
```
 
In this challenge, you will implement commands that allow a user to create, move and delete directories.
 
A successful solution will take the following input:
 
```
CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
DELETE fruits/apples
DELETE foods/fruits/apples
LIST
```
 
and produce the following output
 
```
CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
fruits
  apples
    fuji
grains
vegetables
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
foods
  fruits
    apples
      fuji
  grains
  vegetables
    squash
DELETE fruits/apples
Cannot delete fruits/apples - fruits does not exist
DELETE foods/fruits/apples
LIST
foods
  fruits
  grains
  vegetables
    squash
```