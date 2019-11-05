Group Number: 19

Member 1 : Frank Nguyen
	   1436640

Member 2 : Richer Pham
	   1514130
	   

How to run code
*NOTE* : please input the stopwords file in as stopwords.txt within the same directory the .py file is located.
Our program does not require a stopwords.txt input, so the file MUST have the name 'stopwords.txt'.
	- Hexcode might be different (there might be warnings in all the file)
	-> due to hexcode differences perhaps (from google groups - "Curious case of different bytes" thread)

Example input = python3 keywords.py "input=testcase1.txt;k=3;mostfrequent=Y;uppercase=N;output=outputTc1.txt"

- Y and N must be uppercase
- k should be an integer; no floats or doubles.
- The words at and before the = operator are imporant; mostfrequent=, uppercase=, etc. are necessary

input the following into the terminal within the directory

Explanation

Lambda expressions 
we use them where we thought it could be trivial i.e iterating through a list without the use of for/while
loops while sorting. But for the most part, we used recursion for the bulk of our program, because we couldn't figure
out how to get lambda functions to call other Solution helper functions within the lambda statement.

Search algorithms - we went with a recursive sequential search algorithm, so runtime for that was O(n)
Sort algorithm - used sorted with recursive tie-breaker method for k number of words O(n log n)
	- sorted returns a new list, so it shouldn't mutate

Case changing algorithm(s) - worst case O(n*m) where n is the number of words in the list and m are the number of characters in
the word.
	- Passed character index and list index to keep track of where we are in the lists and use those to slice from the parent list
	and passed and updated convertedList to the sequential functions to ensure we had an up-to-date copy.

