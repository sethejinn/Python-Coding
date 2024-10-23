import random
import itertools
from math import prod

# Generate random data with customizable range
def generate_data(n, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(n)]

# Find all subsets of a list within a specific size range
def find_subsets(data, min_size=1, max_size=None):
    if max_size is None:
        max_size = len(data)
    subsets = []
    for r in range(min_size, max_size + 1):
        subsets.extend(itertools.combinations(data, r))
    return subsets

# Calculate the product of all elements in a subset
def product_of_subset(subset):
    return prod(subset)

# Calculate the sum of all elements in a subset
def sum_of_subset(subset):
    return sum(subset)

# Check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Find subsets with prime product or prime sum
def prime_subsets(data, prime_type="product", min_size=1, max_size=None):
    all_subsets = find_subsets(data, min_size, max_size)
    
    if prime_type == "product":
        prime_subsets = [subset for subset in all_subsets if is_prime(product_of_subset(subset))]
    elif prime_type == "sum":
        prime_subsets = [subset for subset in all_subsets if is_prime(sum_of_subset(subset))]
    else:
        raise ValueError("Invalid prime_type! Use 'product' or 'sum'.")
    
    return prime_subsets

# Display results with customization
def display_results(subsets, prime_type, show_subset=True):
    if not subsets:
        print(f"No subsets found with prime {prime_type}.")
        return
    
    print(f"Subsets with prime {prime_type}:")
    for subset in subsets:
        if prime_type == "product":
            value = product_of_subset(subset)
        elif prime_type == "sum":
            value = sum_of_subset(subset)
        
        if show_subset:
            print(f"Subset: {subset} --> {prime_type.capitalize()}: {value}")
        else:
            print(f"{prime_type.capitalize()}: {value}")

# Main function with user input for options
def main():
    print("Welcome to the Subset Analyzer!")
    
    # Customizable data generation
    num_elements = int(input("Enter the number of elements in the dataset: "))
    min_val = int(input("Enter the minimum value for random numbers: "))
    max_val = int(input("Enter the maximum value for random numbers: "))
    data = generate_data(num_elements, min_val, max_val)
    print(f"Generated Data: {data}")
    
    # User selects whether to analyze product or sum
    prime_type = input("Do you want to check subsets with prime 'product' or 'sum'? ").strip().lower()
    if prime_type not in ['product', 'sum']:
        prime_type = 'product'
    
    # Customizable subset size
    min_size = int(input(f"Enter the minimum subset size (1-{num_elements}): "))
    max_size = int(input(f"Enter the maximum subset size ({min_size}-{num_elements}): "))
    
    # Show subsets or only prime values
    show_subset = input("Do you want to display the subsets (y/n)? ").strip().lower() == 'y'
    
    # Find and display prime subsets
    prime_subsets_found = prime_subsets(data, prime_type, min_size, max_size)
    display_results(prime_subsets_found, prime_type, show_subset)

if __name__ == "__main__":
    main()
