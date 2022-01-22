import random
import string


characters = list(string.ascii_letters + string.digits + ",!@#$%^&*()>?/_-=+")

def generate_random_passwd():
    length = int(input("Password lenght: "))
    
    random.shuffle(characters)

    password = []
    for i in range(length): password.append(random.choice(characters))
    
    random.shuffle(password)
    
    print("".join(password))

if __name__=="__main__": generate_random_passwd()
