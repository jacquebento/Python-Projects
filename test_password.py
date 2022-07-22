from unittest import mock
from webbrowser import get
from password import check_pass_length, get_choice, get_password, print_lists, save_passwords
import pytest
import string
import unittest
import csv
import random

def test_get_choice():

    with mock.patch('builtins.input', return_value = "yes"):
        assert get_choice("password") == string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def test_check_pass_length():
    with mock.patch('builtins.input', return_value = "10"):
        assert check_pass_length() == 10

def test_get_password():
    # test for a lowercase password:
    password = "a"
    assert get_password(password,string.ascii_lowercase, 10).islower() == True
    assert len(get_password(password,string.ascii_lowercase, 10)) == 10

    # test for an uppercase password:
    password = "A"
    assert get_password(password,string.ascii_uppercase, 10).isupper() == True

    # test for a numeric password:
    password = "4"
    assert get_password(password,string.digits, 10).isnumeric() == True

    # test for a lowercase and an uppercase password:
    password = "aL"
    password = get_password(password,string.ascii_lowercase+string.ascii_uppercase, 10)
    check_lower = False
    check_upper = False
    valid_password = 0
    for i in password:
        if i.islower() == True:
            check_lower = True
        if i.isupper() == True:
            check_upper = True
    if check_lower == True and check_upper == True:
        valid_password = 1
    assert valid_password == 1

    # test for a lowercase, uppercase and numeric password:
    password = "aL4"
    password = get_password(password,string.ascii_lowercase+string.ascii_uppercase+string.digits, 10)
    check_lower = False
    check_upper = False
    check_number = False
    valid_password = 0
    for i in password:
        if i.islower() == True:
            check_lower = True
        if i.isupper() == True:
            check_upper = True
        if i.isnumeric() == True:
            check_number = True
    if check_lower == True and check_upper == True and check_number == True:
        valid_password = 1
    assert valid_password == 1

    # test for a lowercase and numeric password:
    password = "z3"
    password = get_password(password,string.ascii_lowercase+string.digits, 10)
    check_lower = False
    check_upper = False
    check_number = False
    valid_password = 0
    for i in password:
        if i.islower() == True:
            check_lower = True
        if i.isupper() == True:
            check_upper = True
        if i.isnumeric() == True:
            check_number = True
    if check_lower == True and check_upper == False and check_number == True:
        valid_password = 1
    assert valid_password == 1

    # test for an uppercase and numeric password:
    password = "E4"
    password = get_password(password,string.ascii_uppercase+string.digits, 10)
    check_lower = False
    check_upper = False
    check_number = False
    valid_password = 0
    for i in password:
        if i.islower() == True:
            check_lower = True
        if i.isupper() == True:
            check_upper = True
        if i.isnumeric() == True:
            check_number = True
    if check_lower == False and check_upper == True and check_number == True:
        valid_password = 1
    assert valid_password == 1

    # test for a symbols password:
    password = random.choice(string.punctuation)
    punct_list = list(string.punctuation)
    password = get_password(password,string.punctuation, 10)
    check_symbol = False
    valid_password = 0
    for i in password:
        if i in punct_list:
            check_symbol = True
    if check_symbol == True:
        valid_password = 1
    assert valid_password == 1

    # test for a lowercase and symbols password:
    password = "e@"
    password = get_password(password,string.ascii_lowercase+string.punctuation, 10)
    check_lower = False
    check_upper = False
    check_number = False
    check_symbol = False
    valid_password = 0
    for i in password:
        if i.islower() == True:
            check_lower = True
        if i.isupper() == True:
            check_upper = True
        if i.isnumeric() == True:
            check_number = True
        if i in punct_list:
            check_symbol = True
    if check_lower == True and check_upper == False and check_number == False and check_symbol == True:
        valid_password = 1
    assert valid_password == 1

    # test for a uppercase and symbols password:
    password = "L@"
    password = get_password(password,string.ascii_uppercase+string.punctuation, 10)
    check_lower = False
    check_upper = False
    check_number = False
    check_symbol = False
    valid_password = 0
    for i in password:
        if i.islower() == True:
            check_lower = True
        if i.isupper() == True:
            check_upper = True
        if i.isnumeric() == True:
            check_number = True
        if i in punct_list:
            check_symbol = True
    if check_lower == False and check_upper == True and check_number == False and check_symbol == True:
        valid_password = 1
    assert valid_password == 1

    # test for a numeric and symbols password:
    password = "8@"
    password = get_password(password,string.digits+string.punctuation, 10)
    check_lower = False
    check_upper = False
    check_number = False
    check_symbol = False
    valid_password = 0
    for i in password:
        if i.islower() == True:
            check_lower = True
        if i.isupper() == True:
            check_upper = True
        if i.isnumeric() == True:
            check_number = True
        if i in punct_list:
            check_symbol = True
    if check_lower == False and check_upper == False and check_number == True and check_symbol == True:
        valid_password = 1
    assert valid_password == 1

    # test for a lowercase, numeric and symbols password:
    password = "a4@"
    password = get_password(password,string.ascii_lowercase+string.digits+string.punctuation, 10)
    check_lower = False
    check_upper = False
    check_number = False
    check_symbol = False
    valid_password = 0
    for i in password:
        if i.islower() == True:
            check_lower = True
        if i.isupper() == True:
            check_upper = True
        if i.isnumeric() == True:
            check_number = True
        if i in punct_list:
            check_symbol = True
    if check_lower == True and check_upper == False and check_number == True and check_symbol == True:
        valid_password = 1
    assert valid_password == 1

    # test for a lowercase, uppercase ans symbols password:
    password = "aE@"
    password = get_password(password,string.ascii_lowercase+string.ascii_uppercase+string.punctuation, 10)
    check_lower = False
    check_upper = False
    check_number = False
    check_symbol = False
    valid_password = 0
    for i in password:
        if i.islower() == True:
            check_lower = True
        if i.isupper() == True:
            check_upper = True
        if i.isnumeric() == True:
            check_number = True
        if i in punct_list:
            check_symbol = True
    if check_lower == True and check_upper == True and check_number == False and check_symbol == True:
        valid_password = 1
    assert valid_password == 1

    # test for an uppercase, numeric and symbols password:
    password = "E2@"
    password = get_password(password,string.ascii_uppercase+string.digits+string.punctuation, 10)
    check_lower = False
    check_upper = False
    check_number = False
    check_symbol = False
    valid_password = 0
    for i in password:
        if i.islower() == True:
            check_lower = True
        if i.isupper() == True:
            check_upper = True
        if i.isnumeric() == True:
            check_number = True
        if i in punct_list:
            check_symbol = True
    if check_lower == False and check_upper == True and check_number == True and check_symbol == True:
        valid_password = 1
    assert valid_password == 1

    # test for a lowercase, uppercase, numeric and symbols password:
    password = "aE2@"
    password = get_password(password,string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation, 10)
    check_lower = False
    check_upper = False
    check_number = False
    check_symbol = False
    valid_password = 0
    for i in password:
        if i.islower() == True:
            check_lower = True
        if i.isupper() == True:
            check_upper = True
        if i.isnumeric() == True:
            check_number = True
        if i in punct_list:
            check_symbol = True
    if check_lower == True and check_upper == True and check_number == True and check_symbol == True:
        valid_password = 1
    assert valid_password == 1

def test_print_lists():
    accounts = ("Gmail", "Facebook")
    usernames = ("jackc@gmail.com", "jackc")
    passwords = ("cy:aP[Kf'5", "KWip'mEV|E")
    rows = list(zip(accounts, usernames, passwords))
    assert rows == [("Gmail", "jackc@gmail.com", "cy:aP[Kf'5"), ("Facebook", "jackc", "KWip'mEV|E")]

def test_save_passwords():
    test = True
    # wrong file name to test
    file = "passords.csv"  
    try:
        f = open(file)
    except FileNotFoundError:
        test = False
    assert test == False


pytest.main(["-v", "--tb=line", "-rN", __file__])  