import pyodbc
from argon2 import PasswordHasher, exceptions
import os
import re
import pyotp
import qrcode
import datetime

class Commands():       
    class SQL():
        def __init__(self):
            pass

        def landing_page(self):
                print("")
                print("")
                print("")
                print("------------------------------------")
                print("")
                print("Bowling Alley System")
                print("")
                print("")
                print("Press the valid number for your request")
                print("")
                print("1. Create Account")
                print("")
                print("2. Login Account")
                print("------------------------------------")
                

                while True:
                    user_input = input("Request: ")
                    if user_input.isdigit():

                        match str(user_input):
                            case "1":
                                self.create_account_page()
                                break

                            case "2":
                                self.login_account_page()
                                break
                            case _:
                                print("")
                                print("")
                                print("")
                                print("------------------------------------")
                                print("")
                                print("Bowling Alley System")
                                print("")
                                print("")
                                print("Please enter a valid number")
                                print("")
                                print("1. Create Account")
                                print("")
                                print("2. Login Account")
                                print("------------------------------------")
                    else:
                        
                        print("")
                        print("")
                        print("")
                        print("------------------------------------")
                        print("")
                        print("Bowling Alley System")
                        print("")
                        print("")
                        print("Please enter a number")
                        print("")
                        print("1. Create Account")
                        print("")
                        print("2. Login Account")
                        print("------------------------------------")
                    

        def create_account_page(self):
            print("")
            print("")
            print("")
            print("------------------------------------")
            print("")
            print("Create Account")
            print("")
            print("------------------------------------")
            print("")
            print("")
            print("")
            print("Input Your First Name")

            while True:
                f_name = input("First Name: ")
                if Commands.Verification.validate_name(f_name):
                    break
                print("")
                print("")
                print("")
                print("Invalid First Name ")
            
            print("")
            print("")
            print("")
            print("Input Your Last Name")
            while True:
                l_name = input("Last Name: ")
                if Commands.Verification.validate_name(l_name):
                    break
                print("")
                print("")
                print("")
                print("Invalid Last Name ")
            
            print("")
            print("")
            print("")
            print("Input Your Age")
            while True:
                age = input("Age: ")
                if Commands.Verification.validate_age(age):
                    break
                print("")
                print("")
                print("")
                print("Invalid Age ")
            
            print("")
            print("")
            print("")
            print("Input Your Email Adress")
            while True:
                email = input("Email Adress: ")
                if Commands.Verification.validate_email(email):
                    if Commands.Verification.validate_email_duplicate(self.cursor, email):
                        break
                    else:
                        print("")
                        print("")
                        print("")
                        print("Your Email Adress Is Already In Use")
                else:
                    print("")
                    print("")
                    print("")
                    print("Invalid Email Adress ")
           
            print("")
            print("")
            print("")
            print("Input Your Phone Number")
            while True:
                phone_number = input("Phone Number: ")
                if Commands.Verification.validate_phone_number(phone_number):
                    if Commands.Verification.validate_phone_number_duplicate(self.cursor ,phone_number):
                        break
                    else:
                        print("")
                        print("")
                        print("")
                        print("Your Phone Number Is Already In Use")
                else:
                    print("")
                    print("")
                    print("")
                    print("Invalid Phone Number ")
            
            print("")
            print("")
            print("")
            print("Input Your Password")
            print("Include (A-z, !$%#^, 0-9) ")
            while True:
                password = input("Password: ")
                if Commands.Verification.validate_password(password):
                    break
                print("")
                print("")
                print("")
                print("Invalid Password include (A-z, !$%#^, 0-9) ")
                print("Password Length must be longer than 8 charcters and less then 20 ")

            print("")
            print("")
            print("")
            secret_key = Commands.TwoFactor.create_secret_key()
            print(f"Your secrect key is {secret_key}")
            if Commands.TwoFactor.verify_key_create(secret_key):
                password_hash = Commands.Hashing.hashing_string(password)
                self.open_db_connection()
                self.add_users(f_name, l_name, age, email, phone_number, password_hash, secret_key)
                self.dashboard_page()

            else:
                print("Invalid OPT")
                self.landing_page()


        def login_account_page(self):
            print("")
            print("")
            print("")
            print("------------------------------------")
            print("")
            print("Login Account")
            print("")
            print("------------------------------------")
            print("")
            print("")
            print("")
            print("Input Your Email Adress")
            while True:
                email = input("Email Adress: ")
                if Commands.Verification.validate_email(email):
                    break
                else:
                    print("")
                    print("")
                    print("")
                    print("Invalid Email Adress")

            print("")
            print("")
            print("")
            print("Input Your Password")
            while True:
                password = input("Password: ")
                if Commands.Verification.validate_password(password):
                    break
                else:
                    print("")
                    print("")
                    print("")
                    print("Invalid Password")



            if Commands.Verification.validate_login(self.cursor, email, password):

                user_id = self.return_user_id(email, password)
                Commands.TwoFactor.verify_key_login(user_id)

            else:
                self.landing_page()
                

        def dashboard_page(self):
            print("")
            print("")
            print("")
            print("------------------------------------")
            print("")
            print("Welcome")
            print("")
            print("------------------------------------")
            print("")
            print("Choose a Selection")
            print("")
            print("1. Book a Session")
            print("2. ???")
            while True:
                    user_input = input("Request: ")
                    if user_input.isdigit():

                        match str(user_input):
                            case "1":
                                self.booking_page()
                                break

                            case "2":
                                self.login_account_page()
                                break
                            case _:
                                print("")
                                print("")
                                print("")
                                print("------------------------------------")
                                print("")
                                print("Welcome")
                                print("")
                                print("------------------------------------")
                                print("")
                                print("Invalid Number")
                                print("")
                                print("1. Book a Session")
                                print("2. ???")
                    else:
                        
                        print("")
                        print("")
                        print("")
                        print("------------------------------------")
                        print("")
                        print("Bowling Alley System")
                        print("")
                        print("------------------------------------")
                        print("")
                        print("Enter a Number")
                        print("")
                        print("1. Create Account")
                        print("")
                        print("2. Login Account")
                        

        def booking_page(self):
            print("")
            print("")
            print("")
            print("------------------------------------")
            print("")
            print("Booking Session")
            print("")
            print("------------------------------------")
            print("")
            print("Enter Session Date")
            print("")
            year = input("Year (YYYY): ")
            month = input("Month (MM): ")
            day = input("Day (DD): ")
            
            if Commands.Verification.validate_date(year, month, day):
                datetime.datetime(2024, 10, 10, 13, 30)
            

        def open_db_connection(self):
            connection_string = (
                r"Driver={ODBC Driver 17 for SQL Server};"
                r"Server=10.221.64.20\SQLEXPRESS;"
                r"Database=BowlingAlleyDB;"
                r"UID=BowlingUserAccount;"
                r"PWD=bRe3IprUKe@hE2LsW9!Vlbrus$PeylstigiCrIch%eBrOdUTRyaw;"
                r"Column Encryption Settings=Enabled;"
            )

            try:
                self.conn = pyodbc.connect(connection_string)
                print("Connection successful")
                self.cursor = self.conn.cursor()
            except pyodbc.InterfaceError as e:
                print(f"Error: {e}")

        def close_db_connection(self):
            self.cursor.close()
            self.conn.close()

        ###
        ### SQL QUERYS
        ###

        def create_user_table(self):
            self.cursor.execute("""
                    CREATE TABLE Users (
                    UserID int IDENTITY(1,1) PRIMARY KEY (UserID),
                    FirstName nvarchar(30),
                    LastName nvarchar(30),
                    Age tinyint,
                    Email nvarchar(50),
                    PhoneNum nvarchar(15),
                    PasswordHash nvarchar(250),
                    SecretKeyHash nvarchar(250),
                    );
                """)
            self.cursor.commit()
        
        def add_users(self, fname, lname, age, email, phone_num, password_hash, secret_key):
            self.cursor.execute("""
            INSERT INTO Users (FirstName, LastName, Age, Email, PhoneNum, PasswordHash, SecretKeyHash)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (fname, lname, age, email, phone_num, password_hash, secret_key))
            self.cursor.commit()
            self.AdminDisplayAllInUsers()

        def return_user_id(self, email, password):
            self.cursor.execute("""
            SELECT * FROM Users 
            WHERE Email = ?
            """, (email))
            users = self.cursor.fetchall()
            password_hasher = PasswordHasher()
            for user in users:
                try:
                    if password_hasher.verify(user[6], password):
                        return user[0]
                    
                except exceptions.VerifyMismatchError:
                    return False

        def AdminDisplayAllInUsers(self):
            self.cursor.execute("""
            SELECT * FROM Users
            """)
            users = self.cursor.fetchall()
            for user in users:
                print(user)

                   


        

    class Verification:
        def validate_phone_number_duplicate(cursor, phone_num):
            cursor.execute("""
            SELECT * FROM Users 
            WHERE PhoneNum = ?
            """, (phone_num))
            users = cursor.fetchall()
            if users == []:
                return True
            return False

        def validate_email_duplicate(cursor, email):
            cursor.execute("""
            SELECT * FROM Users 
            WHERE Email = ?
            """, (email))
            users = cursor.fetchall()
            if users == []:
                return True
            return False

        def validate_phone_number(phone):
            pattern = re.compile(r"^\+?[1-9]\d{1,14}$") 
            return pattern.match(phone)

        def validate_email(email): 
            pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$") 
            return pattern.match(email)
        
        def validate_name(name):
            if name.isalpha() and len(name) <= 30: 
                return True
            return False
        
        def validate_age(age):
            try:
                if age.isdigit() and 0 <= int(age) <= 120: 
                    return True
                return False
            except:
                return False
            
        def validate_password(password):
            if (len(password) >= 8 and len(password) <= 20 
                and re.search(r"[A-Z]", password) 
                and re.search(r"[a-z]", password) 
                and re.search(r"[0-9]", password) 
                and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
                return True
            return False
        
        def validate_login(cursor, email, password):
            cursor.execute("""
            SELECT * FROM Users 
            WHERE Email = ?
            """, (email))
            users = cursor.fetchall()

            password_hasher = PasswordHasher()
            for user in users:
                try:
                    if password_hasher.verify(user[6], password):
                        return user[0]
                    
                except exceptions.VerifyMismatchError:
                    return False
            return False

        def validate_date(year, month, day):
            year_regex = r"^\d{4}$" 
            month_regex = r"^(0[1-9]|1[0-2])$" 
            day_regex = r"^(0[1-9]|[12][0-9]|3[01])$"

            if not re.match(year_regex, year): 
                return False
            if not re.match(month_regex, month): 
                return False 
            if not re.match(day_regex, day): 
                return False
            return True
        
    class TwoFactor:
        def create_secret_key():
            return pyotp.random_base32()

        
        def verify_key_login(user_id, cursor):
            cursor.execute("""
                SELECT * FROM Student WHERE UserID = ?
            """, (user_id))
            user = cursor.fetchone()
            print(user)
            totp = pyotp.TOTP(user[7])
            otp = input("Enter the OTP: ")
            if totp.verify(otp):
                return True
            return False

        def verify_key_create(key):
            totp = pyotp.TOTP(key)
            otp = input("Enter the OTP: ")
            if totp.verify(otp):
                return True
            return False

    class SecretKeyService:
        pass

    class Hashing:
        def hashing_string(hash_string):
            while True:
                hasher = PasswordHasher()
                hashed_string = hasher.hash(hash_string)
                if hasher.verify(hashed_string, hash_string):
                    break
            return hashed_string
                