#https://www.reddit.com/r/dailyprogrammer/comments/4z04vj/20160822_challenge_280_easy_0_to_100_real_quick/

def checkIfHandIsValid(bin, hand):
	
	if hand == 'l':
		dir = 1
		start = 0
		end = 3
	else:
		dir = -1
		start = 4
		end = 1
	
	valid = True
	last = '0'
	
	i = start
	while valid and i != end+dir:
		if last == '0' or last == bin[i]:
			last = bin[i]
			i = i + dir
		else:
			valid = False
			
	return valid
	
def calculate(bin):
	result = 0
	i = 0
	while i < 4:
		if bin[i] == '1':
			result = result + 10#
		i = i + 1
	if bin[4] == '1':
		result = result + 50
	
	i = 6
	while i < 10:
		if bin[i] == '1':
			result = result + 1
		i = i + 1
	if bin[5] == '1':
		result = result + 5

	return result

input = '0011101110'

if(checkIfHandIsValid(input[0:5],'l') and checkIfHandIsValid(input[5:10],'r')):
	print(calculate(input))
else:
	print('Invalid...')
