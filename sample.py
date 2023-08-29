import random
import string

#print(string.ascii_letters)
#print(string.ascii_lowercase)
#print(string.digits)
#print(string.punctuation)

#Generating 12 length password
#define the function generate_password
def generate_password(length=12):

    #Contains at least one lowercase character
    lowercase = string.ascii_lowercase
    #Contains at least one uppercase character
    uppercase = string.ascii_uppercase
    #Contains at least one digit
    digits = string.digits
    #Contains at least one special character
    specialcharacters = string.punctuation

    #defining 'all' variable with all characters to select characters for remaining length
    all = lowercase + uppercase + digits + specialcharacters

    a = random.choice(lowercase)
    b = random.choice(uppercase)
    c = random.choice(digits)
    d = random.choice(specialcharacters)

    #generate additional 8 characters to fit for the total length
    i=0
    additional = []
    for i in range(8):
        e = random.choice(all)
        additional.append(e)

    #concatenate all the randomly generated strings together
    print('your password: ' +a+b+c+d+''.join(additional))
generate_password()
