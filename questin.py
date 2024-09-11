def is_prime(n):
    # Prime numbers are greater than 1
    if n <= 1:
        return False
    
    
    for i in range(2, int(n**0.5) + 1):  # Loop from 2 to sqrt(n)
        if n % i == 0:  # If divisible by any number in this range, it's not prime
            return False
    return True  


number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
