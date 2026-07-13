"""Main program for the python-lab project.

Prompts the user for a number and prints its square, whether it is
even or odd, and its equivalent temperature in Fahrenheit (treating
the input as a Celsius value).
"""

from utils import square, is_even, celsius_to_fahrenheit


def main():
    number = float(input("Enter a number: "))

    print(f"Square: {square(number)}")
    parity = "even" if is_even(number) else "odd"
    print(f"The number is {parity}.")
    print(f"{number} C = {celsius_to_fahrenheit(number)} F")


if __name__ == "__main__":
    main()
