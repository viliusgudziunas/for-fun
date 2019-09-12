# Password Validator

# Password validator is a program that validates passwords to match specific rules. For example,
# the minimum length of the password must be eight characters long and it should have
# at least one upper case letter in it.

# A valid password is the one that conforms to the following rules:
# - Minimum length is 5;
# - Maximum length is 10;
# - Should contain at least one number;
# - Should contain at least one special character (such as &, +, @, $, #, %, etc.);
# - Should not contain spaces

# Examples:
# Input: "Sololearn"
# Output: fasle

# Input: "John Doe"
# Output: false

# Input: "$ololearn7"
# Output: true

# Write a program to checks if the user input is a valid password or not.


def password_validator():
    print("Please enter your password")
    psw = input()
    if check_password(psw):
        print("true")
    else:
        print("false")


def check_password(psw):
    if len(psw) < 5:
        return False
    if len(psw) > 10:
        return False
    number = False
    special_char = False
    for char in psw:
        if char == " ":
            return False
        try:
            int(char)
            number = True
        except ValueError:
            pass
        if char in ["!", "\"", "£", "$", "%", "^", "&", "*", "(", ")", "_",
                    "+", "-", "=", "[", "]", "{", "}", ";", "'", ":", "@",
                    ",", "<", ".", ">", "/", "?", "#", "~", "`", "¬", "|"]:
            special_char = True
    if number & special_char:
        return True


password_validator()
