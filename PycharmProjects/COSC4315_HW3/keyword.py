import sys

# Class section

class Solution:

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


# Driver code

if __name__ == "__main__":

    tempArgHolder = sys.argv[1]

    input, kNum, mostFreq, uppercase, output = Solution.argParser(tempArgHolder)

    print ("input : " + input)
    print ("kNumbers : " + str(kNum))
    print ("most Frequent : " + mostFreq)
    print ("uppercase : " + uppercase)
    print("output : " + output)

