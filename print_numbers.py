# Function to print numbers from 1 to n using recursion

def print_numbers(n):
    if n == 0:          # Base case
        return
    print_numbers(n-1)  # Recursive call
    print(n)            # Print after recursion


# Main program
n = int(input("Enter n: "))
print_numbers(n)
