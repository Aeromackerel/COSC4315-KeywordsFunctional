import sys

# Class section

class Solution:

    # field variable initialization
    fileText = ""
    listContent = []
    listContentModified = []

    # Parses Arguments and passes back to main
    # @ params - input argument (argv[1])
    # @ error - if we get different number of arguments then -> notify user and exit program

    def argParser (argumentsList):

        # For easier parsing
        argumentsIn = argumentsList.replace(" ", "")
        tempList = argumentsIn.split(";")

        # Since we have a defined input with no variation - we can assume the first input is inputfilename ... etc
        # REPLACE THIS LATER - MUTATION HERE
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

    # Checks the parameters for validity
    # @ params - kNumbers, uppercase, mostFrequent
    # @ error - unknown input -> exit

    # Reads from text file that we have in the directory
    # and stores the text into the text field variable we
    # have in the class
    # @params - the input file name
    # @error - if something other than Y/N is passed in the uppercase slot -> notify user and exit

    def CheckParams (kNums, mostFreq, caseSpecified):
        if (kNums < 0):
            print ("kNumbers should be greater or equal to 0.")
            exit (1)
        elif (mostFreq != 'Y' and mostFreq != 'N'):
            print ("Most frequent should be either Y OR N")
            exit (1)
        elif (caseSpecified != 'Y' and caseSpecified != 'N'):
            print ("uppercase should be either Y OR N")
            exit (1)


    def fileHandler(self, fileName):

       try:
            with open(fileName,"r") as f:
               self.filtText = f.read()
       except:
            print("File Not Found.")

    # Prints the original list content
    def printText(self):
        print (self.fileText)


    def convertCase(self, caseSpecfied):
        if (caseSpecfied == 'Y'):
            print ("Uppercase chosen")


        elif (caseSpecfied == 'N'):
            print ("Lowercase chosen")


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

    # check the param validity
    Solution.CheckParams(kNum, mostFreq, uppercase)

    # Read input and stores the words in a string
    Solution.fileHandler(Solution, input)
