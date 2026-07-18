def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    num_digits = len(digits)
    sum_of_powers = sum(d ** num_digits for d in digits)
    return sum_of_powers == num


number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
