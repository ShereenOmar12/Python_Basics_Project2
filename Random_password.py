import string
import random


characters = list(string.ascii_letters + string.digits + "_")

def generate_random_password():
    
    random.shuffle(characters)
	5
    password = []
    for i in range(7):
        password.append(random.choice(characters))

    random.shuffle(password)
    return("".join(password))


print(f"the Random password is:{generate_random_password()}")
