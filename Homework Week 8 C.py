from random import randint
currentAttempt = 1
maxAttempt = 3

code = str(randint(1000, 9999))
print ("The passcode is " + code + ".")

while currentAttempt <= maxAttempt:
        print ("Attempt " + str(currentAttempt) + " / " + str(maxAttempt) + ":")
        playerInput = input()
        
        if playerInput == code:
                print ("You have successfully logged in.")
                quit()
        else:	
                print ("That is not the corrct passcode.")
        currentAttempt += 1
print ("You have been denied access.")
quit()	
