import random

def generate_password(min_length=14):
    if min_length <= 14:
        raise ValueError("Password length must be more than 14 characters.")
    
    upper_case = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    lower_case = "abcdefghijklmnñopqrstuvwxyz"
    digits = "0123456789"
    special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    
    length = random.randint(min_length + 1, min_length + 10)
    
    password = [
        random.choice(upper_case),
        random.choice(lower_case),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    all_characters = upper_case + lower_case + digits + special_chars
    
    while len(password) < length:
        char = random.choice(all_characters)
        if char not in password:
            password.append(char)
    
    random.shuffle(password)
    
    return ''.join(password)

print(generate_password(14))
