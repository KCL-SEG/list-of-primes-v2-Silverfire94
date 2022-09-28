"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    counter = 0
    num = 2
    while counter < number_of_primes:
         flag = True
         for i in range(2, num):
             if num % i == 0:
                 flag = False
                 break
         if flag:
             list.append(num)
             counter += 1
         num += 1
    if counter <= 0:
        raise ValueError(f"The number supplied is not valid! \n{number_of_primes}")
    return list
