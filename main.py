def find_prime_factors(n):
    """Function to find the prime factors of a given number n"""
    prime_factors = []
    # Divide by 2 to remove all even factors
    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2

    # n must be odd at this point, so we can skip one element (Note i = i + 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        # While i divides n, append i and divide n
        while n % i == 0:
            prime_factors.append(i)
            n = n // i

    # If n is a prime number greater than 2
    if n > 2:
        prime_factors.append(n)

    return prime_factors


# Main program starts here
if __name__ == "__main__":
    try:
        # Taking input from the user
        num = int(input("Enter a number to find its prime factors: "))
        if num < 1:
            print("Please enter a number greater than 0.")
        else:
            # Finding the prime factors
            factors = find_prime_factors(num)
            # Displaying the prime factors
            print(f"The prime factors of {num} are: {', '.join(map(str, factors))}")
    except ValueError:
        print("Please enter a valid integer.")
