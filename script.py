import sys

class entry(object): # '”' is causing issues '"'
	def __init__ (self, inp):
		self.inp = inp
		temp = inp.split(" ")
		self.time = temp[0]
		rest = temp[4]
		for i in range(5, inp.count(" ")):
			rest += temp[i]
		self.message = rest.split(":")[1]
		self.name = temp[2] + " " +  temp[3]
	def getcurrent(self):
		return self.name
	def getFirstName(self):
		if self.name.index(" ") == -1:
			return ""
		return self.name[:self.name.index(" ")]
	def getLastName(self):
		return self.name[self.name.index(" "):]
	def getMessage(self):
		return self.inp

def run(inFileName, outFileName):
	inFile = open(inFileName, "r", encoding="utf8")
	outFile = open(outFileName, "w", encoding="utf8")
	studentDict = {}
	text = ""
	for inp in inFile.readlines():
		parsed = entry(inp)
		name = (parsed.getLastName().ljust(20, " ") + " " + parsed.getFirstName().ljust(20, " ")).lower()
		if name in studentDict:
			studentDict[name] += "<[*}:>" + parsed.getMessage()
		else:
			studentDict[name] = parsed.getMessage()
	for student in sorted(studentDict.keys()):
		messages = studentDict[student].split("<[*}:>")
		outFile.write((student.ljust(40, " ") + str(len(messages)) + "\n"))
		text += (student.ljust(40, " ") + "\n")
		for message in messages:
			text += ("\t" + message)
	outFile.write("\n\n" + text)

if __name__ == "__main__":
	run(sys.argv[1], sys.argv[2])