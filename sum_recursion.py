# Function to calculate sum from 1 to n using recursion

def recursive_sum(n):
    if n == 0:          # Base case
        return 0
    return n + recursive_sum(n-1)


# Main program
n = int(input("Enter n: "))
print("Sum =", recursive_sum(n))
