from configCharacter import *
import string
import re

def checkUsername(username):
    userNameOK = True
    if not validation(username): userNameOK = False
    if len(username) < minCharacterUsername: userNameOK = False
    print("userNameOK", userNameOK)
    return userNameOK

def checkPassword(Password):
    PasswordOK = True
    if not validation(Password): PasswordOK = False
    print("validationPassword ", PasswordOK)
    if len(Password) < minCharacterUsername: PasswordOK = False
    print("lenPassword ", PasswordOK)
    digits_num, digits_only = check_digits_num(Password)
    if digits_num < minDigitsbersOnPassword: PasswordOK = False
    print("checkDigitsPassword", PasswordOK)
    if checkUpperCase(Password) < minUpperCasePassword: PasswordOK = False
    print("checkUpperCasePassword", PasswordOK)
    if checkLowerCase(Password) < minLowCostPassword: PasswordOK = False
    print("checkLowerCasePassword",PasswordOK )
    if checkPunctuation(Password) < minPunctuationOnPassword: PasswordOK = False
    print("checkPunctuationPassword", PasswordOK)
    if not check_password_from_file(Password): PasswordOK = False
    print("check_password_from_file", PasswordOK)
    return PasswordOK

def checkPhone(value):
    digits_num, digits_only = check_digits_num(value)
    if 8 < digits_num <= 10 and digits_only:
        print("checkPhone", True)
        return True
    else:
        print("checkPhone", False)
        return False


def check_digits_num(value):
    countDigits = 0
    digits_only = True
    for letter in value:
        if letter in string.digits:
            countDigits += 1
        else:
            digits_only = False
    return countDigits, digits_only



def checkUpperCase(value):
    countUpperCase = 0
    for letter in value:
        if letter in string.ascii_uppercase:
            countUpperCase += 1
    return countUpperCase

def checkLowerCase(value):
    countLowerCase = 0
    for letter in value:
        if letter in string.ascii_lowercase:
            countLowerCase += 1
    return countLowerCase

def checkPunctuation(value):
    countPunctuation = 0
    for letter in value:
        if letter in "._=+@$%^&":
            countPunctuation += 1
    return countPunctuation

def validation(value):
    pat = re.compile(r"[A-Za-z0-9._=+@$%^&]+")
    if re.fullmatch(pat, value):
        return True
    else:
        return False

# print(validation("daskal"))

def validation_code(value):
    pat = re.compile(r"[A-Za-z0-9]+")
    if re.fullmatch(pat, value):
        return True
    else:
        return False


def check_password_from_file(password):
    with open('rockyou.txt') as password_list:
        password = password.lower()
        if password in password_list.read():
            return False
        else:
            return True

# print(check_password_from_file("princess"))