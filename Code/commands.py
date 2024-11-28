import pyodbc
from argon2 import PasswordHasher, verify_password
import os
import re
import pyotp
import qrcode

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
                    break
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
                    break
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
            password_hash = Commands.Hashing.password_hashing(password)
            self.open_db_connection()
            self.AddUser(f_name, l_name, age, email, phone_number, password_hash, secret_key)
            

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
        
        def AddUser(self, fname, lname, age, email, phone_num, password_hash, secret_key):
            self.cursor.execute("""
            INSERT INTO Users (Username, Age, Email, PhoneNum, PasswordHash, SecretKeyHash)
            VALUES (?, ?, ?, ?, ?, ?)

            """, (fname, lname, age, email, phone_num, password_hash, secret_key))

    class Verification:
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


    class TwoFactor:
        def create_secret_key(user_id):
            secret = pyotp.random_base32()
            return secret
        
        def verify_key(user_id, cursor):
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

    class SecretKeyService:
        pass

    class Hashing:
        def password_hashing(password):
            while True:
                password_hash = PasswordHasher(password)
                if verify_password(password_hash, password):
                    break
            return password_hash
                