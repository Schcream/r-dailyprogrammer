firstLine = 1
dimens = []
inputVect = []
outputVect = []

def turnRight(input, dimensions):
	outputVect = []
	for x in range(dimensions[0],0,-1):
		for i in range(len(input)-x,-1,-dimensions[0]):
			outputVect.append(input[i])	
			
	return outputVect, [dimensions[1],dimensions[0]]
	
def turnLeft(input, dimensions):
	outputVect = []
	for x in range(dimensions[0],0,-1):
		for i in range(x - 1, len(input),dimensions[0]):
			outputVect.append(input[i])	
			
	return outputVect, [dimensions[1],dimensions[0]]

def mirrorHorizontal(input, dimension):
	outputVect = []
	for x in range(dimension[1],-1,-1):
		for i in range(x*dimension[0],(x+1)*dimension[0]):
			outputVect.append(input[i])
			
	return outputVect, dimensions
	
def mirrorVertical(input, dimension):
	outputVect = []
	for x in range(0,dimension[1]):
		for i in range((x+1)*dimension[0]-1,x*dimension[1]-1,-1):
			outputVect.append(input[i])
			
	return outputVect, dimensions	
	
with open("earth.pgm","r") as f:
	for line in f:
		if firstLine > 0:
			dimens = line.split(" ")[1:2]
			firstLine = 0
		else:
			inputVect.append(int(line))

