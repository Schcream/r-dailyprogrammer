#https://www.reddit.com/r/dailyprogrammer/comments/4ybbcz/20160818_challenge_279_intermediate_text_reflow/

input = 'In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\n'
input = input + 'And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.'

result = ''

for par in input.split('\n'):
	rowCount = 0
	for word in par.split(' '):
		if len(word) + rowCount <= 40:
			result = result + word + ' '
			rowCount = rowCount + len(word) + 1
		else:
			result = result + '\n'	+ word + ' '
			rowCount = len(word) + 1
	
	result = result + '\n\n'
	
print (result)