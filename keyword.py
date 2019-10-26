import sys

# Class section

class Solution:

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
            argOne = tempList[0].replace("input=", "")
            argTwo = int(tempList[1].replace('k=', ''))
            argThree = tempList[2].replace("mostfrequent=", '')
            argFour = tempList[3].replace("uppercase=", '')
            argFive = tempList[4].replace('output=', '')
        except:
            # Print parameters and what is expected of each parameter, otherwise exit
            print ("Invalid arguments")
            sys.exit(1)

        return argOne, argTwo, argThree, argFour, argFive

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


    def fileHandler(fileName, caseSpecified):

       try:
            with open(fileName,"r", encoding = "utf8") as f:
               tempString = f.read()
               fileContent = tempString.split()
               stopWords = (open("stopwords.txt", "r", encoding = "utf8")).read().split()
               stopWordsUpdated = list(filter(str.strip, stopWords))
               caseCorrectedList = Solution.caseHelper(fileContent, caseSpecified)
               noStopWordsList = Solution.RemoveStopWords(caseCorrectedList, stopWordsUpdated)
               print(noStopWordsList)
               wordCountedList = Solution.wordCounter(noStopWordsList, 0)
               for i in range(len(wordCountedList)):
                   print(wordCountedList[i][0]+' '+str(wordCountedList[i][1]))
 
       except:
            print("File Not Found.")
    def wordCounter(fileContent, index, wordCountedList = {}):
        word = fileContent[index]
        if(index == len(fileContent)-1):
            return fileContent
        else:
            if word in wordCountedList.keys():
                wordCountedList[word] += 1
            else:
                wordCountedList[word] = 1
            Solution.wordCounter(fileContent, index+1)
        return sorted(wordCountedList.items(), key=lambda x: (-x[1],x[0]))

    def RemoveStopWords(fileContent, stopWords):
        result = (map(lambda x : x.casefold() in stopWords, fileContent))
        listResult = list(result)
        #print(listResult)
        listNoStopWords = Solution.RemoveStopWordsHelper(fileContent, listResult, 0)
        return listNoStopWords


    def RemoveStopWordsHelper(fileContent, stopWords, listIndex):

        if (listIndex == len(fileContent)-1):
            if (stopWords[listIndex] == True):
                revisedList = fileContent[:listIndex] + stopWords[(listIndex+1):]
                return revisedList
            else:
                return fileContent

        if (stopWords[listIndex] == True):
            revisedList = fileContent[:listIndex] + fileContent[(listIndex+1):]
            stopWordsRevised = stopWords[:listIndex] + stopWords[(listIndex+1):]
            return Solution.RemoveStopWordsHelper(revisedList, stopWordsRevised, listIndex)
        else:
            return Solution.RemoveStopWordsHelper(fileContent, stopWords, listIndex+1)




    def caseHelper(listWords, caseSpecified):
        if (caseSpecified == "Y" ):
            print ("Uppercase Chosen")
            uppercaseList = Solution.UppercaseHelper(listWords)
            return uppercaseList

        elif (caseSpecified == "N"):
            print ("Lowercase Chosen")
            lowercaseList = Solution.LowercaseHelper(listWords)
            return lowercaseList
        else:
            print ("Incorrect input for case specified - please input either Y/N")
            print ("Exitting program.")
            exit(1)


    def LowercaseHelper(listWords):
        listIndex = 0
        charIndex = 0
        word = listWords[listIndex]

        # Pass to another helper that iterates character by character
        lowercaseList = Solution.LowercaseCharHelper(listWords, word, listIndex, charIndex)
        return lowercaseList

    # Functionality - recursively iterates character by character
    # through each word in the list and converts the character to
    # lowercase.
    # We slice the arrays given the indexes we passed in and concatenate
    # converted characters to the the sliced list to form a new list
    # in order to prevent mutations
    #
    # @ params - listWords [] , word evaluating, listIndex, characterIndex
    # @ special cases
    # 1) if we're at the end of the word then we increment listIndex by 1
    # 2) if we're at the end of the list then we return the list


    def LowercaseCharHelper(listWords, string,  listIndex, charIndex):

        string = listWords[listIndex]
        character = string[charIndex]

        # check if the character is not an alphabet character
        if (not character.isalpha()):
            tempString = string[:charIndex] + string[(charIndex+1):]
            if (charIndex < len(tempString)):
                revisedList = listWords[0:listIndex] + [tempString] + listWords[listIndex + 1:len(listWords)]
                return Solution.LowercaseCharHelper(revisedList, tempString, listIndex, charIndex)
            elif (charIndex == len(tempString)):
                if (len(tempString) == 0):
                    revisedList = listWords[0:listIndex] + listWords[listIndex + 1:len(listWords)]
                    return Solution.LowercaseCharHelper(revisedList, revisedList[listIndex], listIndex, 0)
                elif (len(tempString) > 0):
                    revisedList = listWords[0:listIndex] + [tempString] + listWords[listIndex + 1:len(listWords)]
                    return Solution.LowercaseCharHelper(revisedList, revisedList[listIndex], listIndex, 0)

        # check if we reach the end of the list or word

        if (charIndex == len(string) - 1 and listIndex == len(listWords) - 1):
            if (character.isalpha() and not character.islower()):
                tempString = string[0:charIndex] + character.lower()
                tempList = listWords[0:listIndex] + [tempString]
                return tempList
            else:
                return listWords

        elif (charIndex == len(string) - 1):
            if (character.isalpha() and not character.islower()):
                tempString = string[0:charIndex] + character.lower()
                tempList = listWords[0:listIndex] + [tempString] + listWords[listIndex+1:len(listWords)]
                return Solution.LowercaseCharHelper(tempList, tempList[listIndex+1], listIndex+1, 0)

            return Solution.LowercaseCharHelper(listWords, listWords[listIndex+1], listIndex+1, 0)
        else:
            if (character.isalpha() and not character.islower()):
                tempString = string[0:charIndex] + character.lower() + string[charIndex + 1:len(string)]
                tempList = listWords[0:listIndex] + [tempString] + listWords[listIndex+1:len(listWords)]
                return Solution.LowercaseCharHelper(tempList, tempString, listIndex, charIndex + 1)
            else:
                return Solution.LowercaseCharHelper(listWords, listWords[listIndex], listIndex, charIndex+1)



    def UppercaseHelper(listWords):
        listIndex = 0
        charIndex = 0

        # Pass to another helper that iterates character by character
        uppercaseList = Solution.UppercaseCharHelper(listWords, listWords[listIndex], listIndex, charIndex)
        return uppercaseList

    def UppercaseCharHelper(listWords, string, listIndex, charIndex):

        string = listWords[listIndex]
        character = string[charIndex]

        # Check if the character is a non-alphabet character

        if (not character.isalpha()):
            tempString = string[:charIndex] + string[(charIndex+1):]

            if (charIndex < len(tempString)):
                revisedList = listWords[0:listIndex] + [tempString] + listWords[listIndex+1:len(listWords)]
                return Solution.UppercaseCharHelper(revisedList, tempString, listIndex, charIndex)
            elif(charIndex == len(tempString)):
                if (len(tempString) == 0):
                    revisedList = listWords[0:listIndex] + listWords[listIndex+1:len(listWords)]
                    return Solution.UppercaseCharHelper(revisedList, revisedList[listIndex], listIndex, 0)
                elif (len(tempString) > 0):
                    revisedList = listWords[0:listIndex] + [tempString] + listWords[listIndex+1:len(listWords)]
                    return Solution.UppercaseCharHelper(revisedList, revisedList[listIndex], listIndex, 0)




        # check if we reach the end of the list or word
        if (charIndex == len(string) - 1 and listIndex == len(listWords) - 1):
            if (character.isalpha() and not character.isupper()):
                tempString = string[0:charIndex] + character.upper()
                tempList = listWords[0:listIndex] + [tempString]
                return tempList
            else:
                return listWords
        elif (charIndex == len(string) - 1):
            if (character.isalpha() and not character.isupper()):
                tempString = string[0:charIndex] + character.upper()
                tempList = listWords[0:listIndex] + [tempString] + listWords[listIndex+1:len(listWords)]
                return Solution.UppercaseCharHelper(tempList, tempList[listIndex+1], listIndex+1, 0)

            return Solution.UppercaseCharHelper(listWords, listWords[listIndex+1], listIndex+1, 0)
        else:
            if (character.isalpha() and not character.isupper()):
                tempString = string[0:charIndex] + character.upper() + string[charIndex+1:len(string)]
                tempList = listWords[0:listIndex] + [tempString] + listWords[listIndex+1:len(listWords)]
                return Solution.UppercaseCharHelper(tempList, tempString, listIndex, charIndex+1)
            else:
                return Solution.UppercaseCharHelper(listWords, listWords[listIndex], listIndex, charIndex+1)




# Driver code

if __name__ == "__main__":

    tempArgHolder = sys.argv[1]
    input, kNum, mostFreq, uppercase, output = Solution.argParser(tempArgHolder)

    # check the param validity
    Solution.CheckParams(kNum, mostFreq, uppercase)
    # Read input and stores the words in a string
    Solution.fileHandler(input, uppercase)