def is_palindrome(string):
    string = string.replace(" ", "").lower()
    if string == string[::-1]:
        return True
    else:
        return False

str = input("Enter a string:")
if is_palindrome(str):
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")