import random
import array

MAX_LEN = int(input("Enter the Size of the Password : ")) #Getting the password Length

#Creating Array of Characters 
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
locaseCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
upcaseCharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

#Combining the Character set to A Single SET
combinedList = digits + upcaseCharacters + locaseCharacters + symbols

#Randomly choosing one character from the Character set
randDigit = random.choice(digits)
randUpper = random.choice(upcaseCharacters)
randLower = random.choice(locaseCharacters)
randSymbol = random.choice(symbols)


#Combining the randomnly selected Characters
tempPass = randDigit + randUpper + randLower + randSymbol
#Filling the password with randomized characters in the Combined List

for x in range(MAX_LEN - 4):
    tempPass= tempPass+ random.choice(combinedList)
    temp_list = array.array('u', tempPass)
    random.shuffle(temp_list)

# traverse the temporary password array and append the chars to form the password
password = "" 
for x in temp_list:
		password = password + x
print(password)
