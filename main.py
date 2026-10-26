from checker import check_password

print("=== Password Strength Checker ===")
password = input("Enter a sample password to test: ")
print(check_password(password))
