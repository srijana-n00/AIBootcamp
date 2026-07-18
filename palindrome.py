def is_palindrome(n):
    str_num = str(n)
    return str_num == str_num[::-1]

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
