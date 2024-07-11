import random
import string
def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password_generator():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    password_generator()
