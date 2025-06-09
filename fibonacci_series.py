def fibonacci_series(n):
    """Returns the Fibonacci series up to the n-th term."""
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Taking input from the user
try:
    num_terms = int(input("Enter the number of Fibonacci terms you want: "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        result = fibonacci_series(num_terms)
        print("Fibonacci series:", result)
except ValueError:
    print("Invalid input! Please enter an integer.")
