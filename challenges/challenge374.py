#https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/ [EASY]

input_number = 199

temp = input_number
loops = 0
while temp>9:
	loops +=1
	qsum = 0
	while temp>0:
		qsum += temp%10
		temp = int(temp/10)
	temp = qsum
print("Input: ", input_number)
print("Result: ", temp)
print("Loops: ", loops)