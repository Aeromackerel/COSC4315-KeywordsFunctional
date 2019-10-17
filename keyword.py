import sys

# Class section

class Solution:

    # Field variables
    originalText = []
    alteredText = []
    list_keywords =  []
    list_keywordsFreq = []

    # Parses Arguments and passes back to main
    # @ params - input argument (argv[1])
    # @ error - if we get different number of arguments then -> notify user and exit program

    def argParser (argumentsList):

        # For easier parsing
        argumentsIn = argumentsList.replace(" ", "")
        tempList = argumentsIn.split(";")

        # Since we have a defined input with no variation - we can assume the first input is inputfilename ... etc
        try:
            tempList[0] = tempList[0].replace("input=", "")
            tempList[1] = int(tempList[1].replace('k=', ''))
            tempList[2] = tempList[2].replace("mostfrequent=", '')
            tempList[3] = tempList[3].replace("uppercase=", '')
            tempList[4] = tempList[4].replace('output=', '')
        except:
            # Print parameters and what is expected of each parameter, otherwise exit
            print ("Invalid arguments")
            sys.exit(1)

        return tempList[0], tempList[1], tempList[2], tempList[3], tempList[4]

    # Reads from text file that we have in the directory
    # while removing all stopwords that is encountered
    # and stores the text into the text field variable we
    # have in the class
    # @params - the input file name
    # @error - if something other than Y/N is passed in the uppercase slot -> notify user and exit

    def fileHandler(self, fileName, stopwordsFile):
       try:
            with open(fileName,"r") as f:
                self.text =f.read().split()
       except:
            print("File Not Found.")
            sys.exit(1)
       try:
            with open(stopwordsFile,"r") as g:
                stopwords = g.read().split()
       except:
            print("stopwords.txt Not Found.")
            sys.exit(1)
       for word in self.text:
            if word in stopwords:
                self.text.remove(word)
       #below should be all the keywords in the file
       #print(self.text)    

    # Given the case specified that we read in from argv, we
    # look through the text list that we have and iterate
    # character by character to set words to lower case

    def CaseHandler(self, caseSpecified):

        # if conditionals to determine the cases selected

        if (caseSpecified == 'Y'):
            print("Uppercase chosen")




        elif (caseSpecified == 'N'):
            print("Lowercase chosen")
        else:
            print("Unknown argument passed in for 'uppercase' field. Please use either Y/N to denote uppercase or lowercase. Terminating program")
            exit(1)

    # Helper functions to main functions
    # check if the character is a valid letter
    # and adds 32/subtracts 32 to ASCII value
    # then passes the character back

    # if we don't have to convert - just pass back the
    # character

    def LowercaseHelper(character):
        if (character.isalpha() and not character.islower()):
            print("This is not a lowercase character")
            return chr(ord(character) + 32)
        else:
            return character


    def UppercaseHelper(character):
        if (character.isalpha() and not character.isupper()):
            print("this is not an uppercase character")
            return chr(ord(character) - 32)
        else:
            return character




# Driver code

if __name__ == "__main__":

    tempArgHolder = sys.argv[1]

    input, kNum, mostFreq, uppercase, output = Solution.argParser(tempArgHolder)

    #print ("input : " + input)
    #print ("kNumbers : " + str(kNum))
    #print ("most Frequent : " + mostFreq)
    #print ("uppercase : " + uppercase)
    #print("output : " + output)

    # Read input and store them in the list in the class
    Solution.fileHandler(Solution, input, "stopwords.txt")

    Solution.CaseHandler(Solution, uppercase)

    sample = Solution.LowercaseHelper("A")
    sample2 = Solution.UppercaseHelper("c")
    print(sample)
    print(sample2)