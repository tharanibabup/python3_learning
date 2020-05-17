

secretword = 'goldfish'
pw = ''
retryCounter = 0

while (pw != secretword and retryCounter < 3):
    pw = input('What is secret word ?')
    if pw == secretword:
        print('Congratulations ! \nYou are unlocked the door')
        break
    else:
        print('Code not matching')
        retryCounter += 1

if (retryCounter == 3):
    print('You are exceeded the maximum allowed limit !')