import sys

# Class section

class Solution:

    def exampleInput(self):
        print("input format is as follows : 'input=tc1.txt;k=3 (integer number here); mostfrequent = Y (Y or N uppercase ONLY); uppercase = N (Y or N uppercase ONLY); output = output.txt ")
        exit(0)


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
            print("Parameter one in the input should be : input= *FILENAME GOES HERE* example - input.txt")
            print("Parameter two should be : k= *INTEGER NUMEBR GOES HERE* example - 3")
            print("Parameter three should be : mostfrequent= *Y/N goes here CASE MATTERS* example - Y")
            print("Parameter four should be : uppercase= *Y/N goes here CASE MATTERS* example - N")
            print("Parameter five should be : output= *OUTPUT FILENAME GOES HERE* example - output.txt")
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
            print("the input for mostfrequent should be as follows - (example) mostfrequent=N")
            print("CASE matters -> mostfrequent (SHOULD BE LOWERCASE)")
            print ("Most frequent should be either Y OR N")
            exit (1)
        elif (caseSpecified != 'Y' and caseSpecified != 'N'):
            print("the input for uppercase section should be as follows - (example) uppercase=Y")
            print("CASE matters uppercase (SHOULD BE LOWERCASE)")
            print ("uppercase should be either Y OR N")
            exit (1)


    def fileHandler(fileName, caseSpecified, mostfreq, k, output):

       try:
            with open(fileName,"r", encoding = "utf8") as f:
               tempString = f.read()
               fileContent = tempString.split()
               stopWords = (open("stopwords.txt", "r", encoding = "utf8")).read().split()
               stopWordsUpdated = list(filter(str.strip, stopWords))
               caseCorrectedList = Solution.caseHelper(fileContent, caseSpecified)
               noStopWordsList = Solution.RemoveStopWords(caseCorrectedList, [], stopWordsUpdated, 0)

               if (len(noStopWordsList) == 0):
                    outputFile = open(output, "w", encoding = "utf8")
                    Solution.writeEmptyFile(outputFile)
                    exit(0)
               else:
                   wordCountedList = Solution.countWords(noStopWordsList, [] ,0)
                   subWordFreqList = Solution.correctList(wordCountedList, 0, [])
                   CorrectedWordList = Solution.wordSorter(subWordFreqList, 0, mostFreq, k)
                   outputFile = open(output, "w", encoding = "utf8")
                   Solution.writeFile(CorrectedWordList, outputFile, 0)
       except:
            print("An error occured. Please check if the input file is in the directory")
            print("input format is as follows : 'input=tc1.txt;k=3 (integer number here); mostfrequent = Y (Y or N uppercase ONLY); uppercase = N (Y or N uppercase ONLY); output = output.txt ")
            print("please check if your output file has been written - might've caught an exit(0)")

    # If nothing is in the input file
    # print nothing to the output file
    # @params - split word list, outputfilename

    def handleEmptyFile(fileContent, output):
        outputFile = open(output, "w", encoding = "utf8")
        Solution.writeEmptyFile(outputFile)
        exit(0)

    # writes "" to the filename
    def writeEmptyFile(outFile):
        outFile.write("")

    #Functionality - Gets list and write to output File
    # @params - given list, output file name, index
    def writeFile(wordList, outFile, index):
      if(index == len(wordList)):
        return wordList
      else: 
        outFile.write(wordList[index][0] + ' ' + str(wordList[index][1]) + '\n')
        return Solution.writeFile(wordList, outFile, index+1)


    #Functionality - Checks if the word is in the list or not
    # if it is then we return true, otherwise we return false
    # @params - word to find, list of words to search, index

    def WordFinder(wordToFind, listSearch, index):

      if (len(listSearch) == 0):
        return False

      # check if we found the work that we're looking for or no
      # if we have return true, otherwise recursively call the
      # function

      if (index < len(listSearch) - 1):
        if (wordToFind == listSearch[index]):
          return True
        else:
          return Solution.WordFinder(wordToFind, listSearch, index+1)
      elif (index == len(listSearch) - 1):
        if (wordToFind == listSearch[index]):
          return True
        else:
          return False


    # Functionality - Creates a list with sublists
    # given the word-frequency list we have
    # @ params - word-frequency list, index, list

    def correctList(wordFreqList, indexWordFreq, prevList):

      if (indexWordFreq == len(wordFreqList)):
       return prevList

      word = wordFreqList[indexWordFreq]
      frequency = wordFreqList[indexWordFreq + 1]
      newSubList = [[word, frequency]]
      prevListNew = prevList[:indexWordFreq] + newSubList
      return Solution.correctList(wordFreqList, indexWordFreq + 2, prevListNew)


    # Functionality - Counts words and passes back a list
    # [string, count, string, count, ... etc]
    # @ params : list of words(without stopwords), index

    def countWords (wordList, FreqList, index):
      tempBool = Solution.WordFinder(wordList[index], FreqList, 0)

      # Catch statement to signify we're done
      if (index == len(wordList)-1):
        if tempBool == True:
          wordIndex = FreqList.index(wordList[index])
          FreqIndex = wordIndex + 1
          FreqUpdate = FreqList[FreqIndex] + 1
          FreqListnew = FreqList[0:FreqIndex] + [FreqUpdate] + FreqList[FreqIndex+1:]
          return FreqListnew
        else:
          FreqListNew = FreqList + [wordList[index]] + [1]
          return FreqListNew

      # boolean to check if the word is in the list or not
      if tempBool == True:
        wordIndex = FreqList.index(wordList[index])
        FreqIndex = wordIndex+1
        FreqUpdate = FreqList[FreqIndex] + 1
        FreqListNew = FreqList[0:FreqIndex] + [FreqUpdate] + FreqList[FreqIndex+1:]
        return Solution.countWords(wordList, FreqListNew, index+1)
        
      else:
        FreqListNew = FreqList + [wordList[index]] + [1]
        return Solution.countWords(wordList, FreqListNew, index+1)
     

    # Returns each word and its word frequency.
    # @ params : list of sublists, index, mostFreq, # of frequency, empty list
    def wordSorter(fileContent, index, mostFreq, k):
        if(index == len(fileContent)-1):
            return fileContent
        else:
            if (mostFreq == 'Y'):
                freqSortedList = sorted(fileContent, key=lambda x: (-x[1], x[0]))
            elif (mostFreq == 'N'):
                freqSortedList = sorted(fileContent, key=lambda x: (x[1], x[0]))
            
            # print(freqSortedList)
            kFreqSortedList = Solution.correctSortedList(freqSortedList, [] , k, 0)
            # print(kFreqSortedList)
            # print(len(freqSortedList))
            # print(len(kFreqSortedList))

            return kFreqSortedList

    
    # Functionality - corrects the sorted list given k numbers
    # passes back a sliced sorted list w.r.t k Numbers
    # @ params - tbd
    def correctSortedList(freqSortedList, prevList, kNums, index):

      if (kNums == 0):
        return prevList
      
      elif (index == len(freqSortedList) - 1):
        freqSortedListNew = prevList[:index] + freqSortedList[index:index+1]
        return freqSortedListNew


      if (kNums > 0):
        if (freqSortedList[index][1] == freqSortedList[index+1][1]):
          freqSortedListNew = prevList[:index] + freqSortedList[index:index+1]
          return Solution.correctSortedList(freqSortedList, freqSortedListNew, kNums, index+1)
        elif (freqSortedList[index][1] != freqSortedList[index+1][1]):
          freqSortedListNew = prevList[:index] + freqSortedList[index:index+1]
          return Solution.correctSortedList(freqSortedList, freqSortedListNew ,kNums - 1, index+1)




    def RemoveStopWords(fileContent, boolList ,stopWords, index):
        if (index < len(fileContent)):
          currentString = fileContent[index].casefold()
          isStopWordBool = Solution.WordFinder(currentString, stopWords, 0)
          boolListNew = boolList[:index] + [isStopWordBool]
          return Solution.RemoveStopWords(fileContent, boolListNew, stopWords, index+1)
        elif (index == len(fileContent)):
          listNoStopWords = Solution.RemoveStopWordsHelper(fileContent, boolList, 0)
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
            # print ("Uppercase Chosen")
            uppercaseList = Solution.UppercaseHelper(listWords)
            return uppercaseList

        elif (caseSpecified == "N"):
            # print ("Lowercase Chosen")
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

        if (charIndex == len(string) - 1 and listIndex == len(listWords)-1):
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

    # check if system arguments are passed in
    if (len(sys.argv) == 1):
        print("You only gave one argument")
        Solution.exampleInput(Solution)


    tempArgHolder = sys.argv[1]
    input, kNum, mostFreq, uppercase, output = Solution.argParser(tempArgHolder)

    #manually adding arguments
    # input = "t1.txt"
    # kNum = 1
    # mostFreq = 'N'
    # uppercase = 'N'
    # output = "output.txt"

    # check the param validity
    Solution.CheckParams(kNum, mostFreq, uppercase)
    # Read input and stores the words in a string
    Solution.fileHandler(input, uppercase, mostFreq, kNum, output)