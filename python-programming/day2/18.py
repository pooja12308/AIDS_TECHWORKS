#palindromes print
def is_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        no = n % 10
        rev = rev * 10 + no
        n = n // 10
    if original == rev:
        print("Yes, Palindrome")
    else:
        print("No, Not Palindrome")

n = int(input("Enter a number: "))
is_palindrome(n)
