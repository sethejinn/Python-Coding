def is_even(num):
    return num % 2 == 0

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def analyze_number(num):
    if isinstance(num, int):
        type_of_number = "integer"
    elif isinstance(num, float):
        type_of_number = "decimal"
    else:
        type_of_number = "invalid"
    
    print(f"Type of number: {type_of_number}")
    
    if isinstance(num, (int, float)):
        if is_even(num):
            print(f"The number {num} is even.")
        else:
            print(f"The number {num} is odd.")
        
        if isinstance(num, int):
            if is_prime(num):
                print(f"The number {num} is prime.")
            else:
                print(f"The number {num} is not prime.")
                print(f"Prime numbers that {num} is divisible by:")
                for i in range(2, num):
                    if is_prime(i) and num % i == 0:
                        print(i)
    else:
        print("Cannot determine parity or primality for this type of number.")

while True:
    entry = input("Enter a number (or 'exit' to quit): ")
    
    if entry.lower() == 'exit':
        print("Goodbye!")
        break
    
    try:
        number = eval(entry)
        analyze_number(number)
    except (NameError, SyntaxError):
        print("Invalid input. Please enter an integer or a decimal number.")
    except ZeroDivisionError:
        print("Division by zero not allowed.")
    except Exception as e:
        print(f"Error: {e}")
