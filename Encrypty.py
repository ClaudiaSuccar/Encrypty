  
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
r = alphabet[::-1] #Reverses the list by taking the front and back of the list, then going backwards.

message = input('Enter message to be encrypted:\n') #User inputs a short message through the command line.
split = list(message) #Message is split into an array.
print('Encrypted message:')
for i in split: #For every letter in the message...
    index = alphabet.index(i) #The letter's index is compared to the original alphabet
    new_letter = r[index] #Incorporates original index into the reversed alphabet list
    print(new_letter) #Prints out encrypted message