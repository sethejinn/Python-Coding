def decimal_to_binary(number):
    return bin(number)[2:]
def converter():
    while True:
        user_input = input("Enter a number (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        try:
            number = int(user_input)
            binary = decimal_to_binary(number)
            print(f"The number {number} in binary is {binary}")
        except ValueError:
            print("Enter a valid number.")
if __name__ == "__main__":
    converter()
