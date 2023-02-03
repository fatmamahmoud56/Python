import random
lottery= random.randint(0,100)
yourguess=eval(input('enter your guess (2 digit please)'))
strlottery=str(lottery) #convert from integar to string
stryourguess=str(yourguess)
if lottery == yourguess: # check if the lottery match the guess
    print("Great \nit's correct lottery is "+str(lottery)+" and your guess is"+str(yourguess))
elif strlottery[0]==stryourguess[0] or strlottery[0]==stryourguess[1]: # check if one digit from lottery match one digit from guess
    print("Great \nyou guessed one digit lottery is " + str(lottery)+" "+ " and your guess is " +" "+  str(yourguess))
elif strlottery[1]==stryourguess[0] or strlottery[1]==stryourguess[1]:
    print("Great\nyou guessed one digit lottery is " + str(lottery) +" "+ " and your guess is " +" "+ str(yourguess))
else:            # check if the lottery doesn't match the guess
    print("Sorry \nyou cannot guess because lottery is  " + str(lottery) +" "+ " and your guess is " +" "+ str(yourguess) )
