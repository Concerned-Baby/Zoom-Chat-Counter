import sys


class entry(object):
	def __init__ (self, inp):
		time = inp.split("\t")[0]
		rest = inp.split("\t")[1]
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




def run(inFileName, outFileName):
	inFile = open(inFileName, "r")
	outFile = open(outFileName, "w")
	text = ""
	studentDict = {}
	for inp in inFile.readlines():
		parsed = entry(inp)
		text += str(parsed.getFirstName()) + "\t" + str(parsed.getLastName()) + "\n"
	outFile.write(text)


if __name__ == "__main__":
	inFile = sys.argv[1]
	outFile = sys.argv[2]
	run(sys.argv[1], sys.argv[2])