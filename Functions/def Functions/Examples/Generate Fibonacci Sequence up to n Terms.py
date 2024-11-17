### Generate Fibonacci Sequence up to n terms ###

def fibonacci(n):
    # Initialize first two terms
    fib_sequence = [0, 1]
    
    # Generate Fibonacci sequence up to n terms
    for i in range(2, n):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)
    
    return fib_sequence[:n]  # Return sequence up to n terms

# Get desired number of terms from the user
n = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Ensure valid input
if n <= 0:
    print("Please enter a positive integer.")
else:
    # Generate and display the Fibonacci sequence
    sequence = fibonacci(n)
    print("Fibonacci sequence up to ", n, "terms: ", sequence)
