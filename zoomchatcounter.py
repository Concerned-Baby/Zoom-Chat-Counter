import sys
import datetime

#Takes the input file and sees who sent each message
#Parameters: File on read
#Returns: A list of who sent each message
def parseToSender(inputFile):
	pass

#Counts how many times a sender appears in the list
#Parameters: A list of who sent each message
#Returns: A dictionary of each sender and how many messages they sent
def consolidateToSenderCount(senders):
	pass

#Formats the dictionary so that it is alphabetized and margined
#Parameters: A dictonary of each sender and how many messages they sent
#Returns: A string that is ready to be outputted
def formatDictionary(senderDict):
	pass

#Writes the text to a file
#Parameters: The text to be written, a file on write
#Returns: Nothing
def writeToFile(text, outputFile):
	pass

#Does the whole process that this program is supposed to do
#Parameters: A file on read, A file on write
#Returns: Nothing
def doProcess(inputFile, outputFile):
	senders = parseToSender(inputFile)
	sendersCount = consolidateToSenderCount(senders)
	text = formatDictionary(sendersCount)
	writeToFile(text, outputFile)


def main():
	begin_time = datetime.datetime.now()
	if (len(sys.argv) != 3):
		print("\nInvalid Input: Type in the command \"python zoomchatcounter.py [input file] [output file]\"\n")
	else:
		try: 
			inFile = open(sys.argv[1], "r", encoding="utf8")
			outFile = open(sys.argv[2], "w", encoding="utf8")
			doProcess(inFile, outFile)
		except Exception:
			print("A problem occured while registering files")

	print("Runtime is:", end=" ")
	print(datetime.datetime.now() - begin_time)

if __name__ == "__main__":
	main()