import sys
import datetime

#Takes the input file and sees who sent each message
#Parameters: File on read
#Returns: A list of who sent each message
def parseToSender(inputFile):
	senders = []
	for inputLine in inputFile.readlines():
		try:
			indexOne = inputLine.index("From") + 5
			indexTwo = inputLine.index("to") - 1
			senders.append(inputLine[indexOne:indexTwo])
		except ValueError: #overflow line, can ignore
			pass 
	return senders

#Counts how many times a sender appears in the list
#Parameters: A list of who sent each message
#Returns: A dictionary of each sender and how many messages they sent
def consolidateToSenderCount(senders):
	senderDict = {} #String sender, int times
	for sender in senders:
		try:
			senderDict[sender] = senderDict.get(sender) + 1
		except TypeError: #sender is not in dictionary yet
			senderDict[sender] = 1
	return senderDict

#Formats the dictionary so that it is alphabetized and margined
#Parameters: A dictonary of each sender and how many messages they sent
#Returns: A string that is ready to be outputted
def formatDictionary(senderDict):
	toSend = ""
	maxNameLength = 25
	for sender in sorted(senderDict.keys()):
		if (len(sender) > maxNameLength):
			toSend += sender[:maxNameLength] + str(senderDict[sender]) + "\n"
		else:
			toSend += sender.ljust(maxNameLength) + str(senderDict[sender]) + "\n"
	return toSend

#Writes the text to a file
#Parameters: The text to be written, a file on write
#Returns: Nothing
def writeToFile(text, outputFile):
	outputFile.write(text)

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
		#try: 
		inFile = open(sys.argv[1], "r", encoding="utf8")
		outFile = open(sys.argv[2], "w", encoding="utf8")
		doProcess(inFile, outFile)
		#except Exception:
		#	print("A problem occured while registering files")

	print("Runtime is:", end=" ")
	print(datetime.datetime.now() - begin_time)

if __name__ == "__main__":
	main()