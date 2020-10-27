import sys


class entry(object):
	def __init__ (self, inp):
		print(inp)
		self.inp = inp
		self.time = inp.split("\t")[0]
		rest = inp.split("\t")[1]
		self.message = rest.split(":")[1]
		rest = rest.split(":")[0]
		rest = rest.split("to")[0]
		rest = rest.split("From")[1]
		self.name = rest.strip()
	def getcurrent(self):
		return self.name
	def getFirstName(self):
		if self.name.index(" ") == -1:
			return ""
		else:
			return self.name[:self.name.index(" ")]
	def getLastName(self):
		return self.name[self.name.index(" "):]
	def getMessage(self):
		return self.inp




def run(inFileName, outFileName):
	inFile = open(inFileName, "r")
	outFile = open(outFileName, "w")
	studentDict = {}
	for inp in inFile.readlines():
		parsed = entry(inp)
		name = (parsed.getLastName().ljust(25, " ") + " " + parsed.getFirstName().ljust(25, " ")).lower()
		if name in studentDict:
			studentDict[name] += "<[*}:>" + parsed.getMessage()
		else:
			studentDict[name] = parsed.getMessage()
	for student in sorted(studentDict.keys()):
		messages = studentDict[student].split("<[*}:>")
		outFile.write((student.ljust(40, " ") + str(len(messages)) + "\n"))
		for message in messages:
			outFile.write("\t" + message)

if __name__ == "__main__":
	run(sys.argv[1], sys.argv[2])