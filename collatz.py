# The number we will perform the Collatz operation on.
n = int(input("Please enter a positive integer: "))

# Keep looping until we reach 1.
# Note: this assumes the Collatz conjecture is true.
while n != 1:
    print(n)
    if n % 2 == 0:
        # If n is even, divide it by two.
        n = n // 2
    else:
        # If n is odd, multiple it by three and add 1.
        n = (3 * n) + 1

# Finally, print the 1.
print(n)