import sys


class entry(object):
	def __init__ (self, inp):
		time = inp.split("\t")[0]
		rest = inp.split("\t")[1]

def run(inFileName, outFileName):
	inFile = open(inFileName, "r")
	outFile = open(outFileName, "w")
	studentDict = {}
	for inp in inFile.readlines():
		parsed = entry(inp)

if __name__ == "__main__":
	inFile = sys.argv[1]
	outFile = sys.argv[2]
	run(sys.argv[1], sys.argv[2])