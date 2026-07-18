try:
    num = int(input("Enter an integer: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Invalid input! Please enter an integer.")
