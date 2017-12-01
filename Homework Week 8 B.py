currentCharacter = 1
currentLine = 1
maxLine = 5

while currentLine <= maxLine:
	while currentCharacter <= currentLine:
		print ("* ", end = "")
		currentCharacter +=1
	print ("")
	currentCharacter = 1
	currentLine +=1
	
