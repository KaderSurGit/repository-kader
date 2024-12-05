import random

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def math_challenge_factorial():
    n = random.randint(1, 10)
    correct = factorial(n)
    print(f"Math Challenge: Calculate the factorial of {n}.")
    answer = int(input("Your answer: "))
    if answer == correct:
        print("Correct! You win a key.")
        return True
    print(f"Incorrect. The correct answer was {correct}.")
    return False
