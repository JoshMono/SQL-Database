import pyodbc
from argon2 import PasswordHasher, exceptions
import os
import re
import pyotp
import datetime
import boto3
import json
from tabulate import tabulate

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
                email_hash = Commands.Hashing.hashing_string(email)
                phone_number_hash = Commands.Hashing.hashing_string(phone_number)
                password_hash = Commands.Hashing.hashing_string(password)
                self.open_db_connection()
                self.add_users(f_name, l_name, age, email_hash, phone_number_hash, password_hash, secret_key)
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
                self.user_id = user_id
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
            print("2. View Sessions")
            while True:
                    user_input = input("Request: ")
                    if user_input.isdigit():

                        match str(user_input):
                            case "1":
                                self.booking_page()
                                break

                            case "2":
                                self.view_sessions()
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
            while True:
                date = input("Date (DD/MM/YYYY): ")
                if Commands.Verification.validate_date(date):
                    break
                print("")
                print("Invalid Session Date")
                print("")

            print("")
            print("")


            while True:
                time = input("Time (HH:MM): ")
                if Commands.Verification.validate_time(time):
                    break
                print("")
                print("Invalid Session Time")
                print("")
                
            print("")
            print("")


            date_time = Commands.Verification.validate_date_time_string(date, time)
            
            
            while True:
                print("How many people will be playing (Max 6)")
                amount = input("Amount: ")
                if Commands.Verification.validate_group_size(amount):
                    break
                print("")
                print("Invalid Amount")
                print("")

            print("")
            print("")

            print("Comfirm your booking")
            print(f"Date: {date}")
            print(f"Time: {time}")
            print(f"Group Size: {amount}")
            while True:
                selection = input("Confirm (yes/y) or (no/n): ")
                value = Commands.Verification.validate_selection(selection)
                if value == True:
                    self.dashboard_page()
                elif value == False:
                    self.dashboard_page()
                print("")
                print("")
                print("Invalid Selection")

        def view_sessions(self):
            all_sessions = self.return_all_users_sessions()
            print("")
            print("")
            print("")
            print("------------------------------------")
            print("")
            print("All Sessions")
            print("")
            print("------------------------------------")
            print("")
            print("")
            print("")

            formated_sessions = []
            for row in all_sessions:
                session = [row[1], row[2]]
                formated_sessions.append(session)

            print(tabulate([formated_sessions], headers=['Date & Time', 'Group Size'], tablefmt='orgtbl'))


        def open_db_connection(self):
            secret_values = Commands.SecretKeyService.get_secret()
            connection_string = (
                r"Driver={ODBC Driver 17 for SQL Server};"
                f"Server={secret_values['ip']}\SQLEXPRESS;"
                f"Database={secret_values['db']};"
                f"UID={secret_values['uid']};"
                f"PWD={secret_values['pwd']};"
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
                    EmailHash nvarchar(250),
                    PhoneNumHash nvarchar(250),
                    PasswordHash nvarchar(250),
                    SecretKeyHash nvarchar(250),
                    );
                """)
            self.cursor.commit()

        def create_session_table(self):
            self.cursor.execute("""
                    CREATE TABLE Sessions (
                    SessionID int IDENTITY(1,1) PRIMARY KEY (SessionID),
                    DateTime smalldatetime,
                    GroupAmount tinyint,
                    User int FOREIGN KEY (User) REFERENCES Users (User_ID),
                    );
                """)
            self.cursor.commit()

        def return_all_users_sessions(self):
            self.cursor.execute("""
            SELECT * FROM Sessions 
            WHERE User_ID = ?
            """, (self.user_id))
            return self.cursor.fetchall()
        
        def add_users(self, fname, lname, age, email_hash, phone_num_hash, password_hash, secret_key):
            self.cursor.execute("""
            INSERT INTO Users (FirstName, LastName, Age, EmailHash, PhoneNumHash, PasswordHash, SecretKeyHash)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (fname, lname, age, email_hash, phone_num_hash, password_hash, secret_key))
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
        def validate_selection(selection):
            if selection.lower() == "yes" or selection.lower() == "y":
                return True
            if selection.lower() == "no" or selection.lower() == "n":
                return False
            return None


        def validate_group_size(amount):
            if amount.isdigit():
                if int(amount) > 0 and int(amount) <=6:
                    return True
            return False 

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

        def validate_date(date):
            pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
            if re.match(pattern, date):
                return True
            return False
        
        def validate_time(time):
            pattern = r"^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$"
            if re.match(pattern, time):
                return True
            return False
        
        def validate_date_time_string(date, time):
            date_list = date.split("/")
            time_list = time.split(":")

            day = int(date_list[0])
            month = int(date_list[0] )
            year = int(date_list[0] )
            hours = int(time_list[0] )
            minutes = int(time_list[1] )
            return datetime.datetime(year, month, day, hours, minutes)
             

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
        def get_secret():
            client = boto3.client(
                "secretsmanager", 
                aws_access_key_id=f"{os.environ['AWS_ACCESS_KEY_ID']}",
                aws_secret_access_key=f"{os.environ['AWS_SECRET_ACCESS_KEY']}",
                region_name=f"{os.environ['AWS_REGION_NAME']}")

            try:
                response = client.get_secret_value(SecretId=f"{os.environ['AWS_SECRET_NAME']}")
                if "SecretString" in response:
                    return json.loads(response["SecretString"])
                else:
                    return response["SecretBinary"]
            except Exception as e:
                return None

    class Hashing:
        def hashing_string(hash_string):
            hasher = PasswordHasher()
            return hasher.hash(hash_string)                    
                