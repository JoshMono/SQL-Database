import pyodbc
from argon2 import PasswordHasher, exceptions
import os
import re
import pyotp
import qrcode
import datetime
import boto3
import json
from tabulate import tabulate

class Commands():       
    class SQL():
        def __init__(self):
            pass


        def landing_page(self):
                self.user_id = None
                print("")
                print("")
                print("")
                print("------------------------------------")
                print("")
                print("Bowling Alley System")
                print("")
                print("")
                print("Press the valid number for your request")
                print("Enter exit to close")
                print("")
                print("1. Create Account")
                print("")
                print("2. Login Account")
                print("")
                print("3. Create Admin Account")
                print("------------------------------------")
                

                while True:
                    user_input = input("Request: ")
                    if Commands.Verification.exit_input(user_input):
                        self.close_db_connection()
                        exit()

                    if user_input.isdigit():

                        match str(user_input):
                            case "1":
                                self.create_account_page()
                                break

                            case "2":
                                self.login_account_page()
                                break
                            case "3":
                                self.create_admin_account_page()
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
            print("Enter exit to return")
            print("")
            print("------------------------------------")
            print("")
            print("")
            print("")
            print("Input Your First Name")

            while True:
                
                f_name = input("First Name: ")
                if Commands.Verification.exit_input(f_name):
                        self.landing_page()
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
                if Commands.Verification.exit_input(l_name):
                        self.landing_page()
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
                if Commands.Verification.exit_input(age):
                        self.landing_page()
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
                if Commands.Verification.exit_input(email):
                        self.landing_page()
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
            print("Input Your Phone Number e.g.(+61490767436)")
            while True:
                phone_number = input("Phone Number: ")
                if Commands.Verification.exit_input(phone_number):
                        self.landing_page()
                if Commands.Verification.validate_phone_number(phone_number):
                    break
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
                if Commands.Verification.exit_input(password):
                        self.landing_page()
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

            if Commands.TwoFactor.verify_key_create(secret_key):
                password_hash = Commands.Hashing.hashing_string(password)
                self.add_users(f_name, l_name, age, email, phone_number, password_hash, secret_key)
                user_id = self.return_user_id(email, password)
                self.user_id = user_id
                self.dashboard_page()

            else:
                print("Invalid OPT")
                self.landing_page()








        def create_admin_account_page(self):
            print("")
            print("")
            print("")
            print("------------------------------------")
            print("")
            print("Create Admin Account")
            print("Enter exit to return")
            print("")
            print("------------------------------------")
            print("")
            print("")
            print("")
            print("Input Your First Name")

            while True:
                
                f_name = input("First Name: ")
                if Commands.Verification.exit_input(f_name):
                        self.landing_page()
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
                if Commands.Verification.exit_input(l_name):
                        self.landing_page()
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
                if Commands.Verification.exit_input(age):
                        self.landing_page()
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
                if Commands.Verification.exit_input(email):
                        self.landing_page()
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
            print("Input Your Phone Number e.g.(+61490767436)")
            while True:
                phone_number = input("Phone Number: ")
                if Commands.Verification.exit_input(phone_number):
                        self.landing_page()
                if Commands.Verification.validate_phone_number(phone_number):
                    break
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
                if Commands.Verification.exit_input(password):
                        self.landing_page()
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
            print("Input Admin Code")
            admin_code = input("Code: ")
            secrets = Commands.SecretKeyService.get_secret()
            if secrets['admin_sc'] != admin_code:
                print("Invalid")
                self.landing_page()            
            else:
                print("")
                print("")
                print("")
                secret_key = Commands.TwoFactor.create_secret_key()
                if Commands.TwoFactor.verify_key_create(secret_key):
                    password_hash = Commands.Hashing.hashing_string(password)
                    self.add_users(f_name, l_name, age, email, phone_number, password_hash, secret_key, 1)
                    user_id = self.return_user_id(email, password)
                    self.user_id = user_id
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
            print("Enter exit to return")
            print("")
            print("------------------------------------")
            print("")
            print("")
            print("")
            print("Input Your Email Adress")
            while True:
                email = input("Email Adress: ")
                if Commands.Verification.exit_input(email):
                        self.landing_page()
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
                if Commands.Verification.exit_input(password):
                        self.landing_page()
                if Commands.Verification.validate_password(password):
                    break
                else:
                    print("")
                    print("")
                    print("")
                    print("Invalid Password")



            if Commands.Verification.validate_login(self.cursor, email, password):

                user_id = self.return_user_id(email, password)
                if Commands.TwoFactor.verify_key_login(user_id, self.cursor):
                    self.user_id = user_id
                    self.dashboard_page()
                else:
                    print("Incorrect")
                    self.landing_page()
            else:
                self.landing_page()
                

        def dashboard_page(self):
            if not self.check_admin():
                print("")
                print("")
                print("")
                print("------------------------------------")
                print("")
                print("Welcome")
                print("Enter exit to return")
                print("")
                print("------------------------------------")
                print("")
                print("Choose a Selection")
                print("")
                print("1. Book a Session")
                print("2. View/Cancel/Update Sessions")
                while True:
                        user_input = input("Request: ")
                        if Commands.Verification.exit_input(user_input):
                            self.landing_page()
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
                                    print("Choose a Selection")
                                    print("")
                                    print("1. Book a Session")
                                    print("2. View/Cancel/Update Sessions")
                        else:
                            
                            print("")
                            print("")
                            print("")
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
                            print("2. View/Cancel/Update Sessions")
            else:
                print("")
                print("")
                print("")
                print("------------------------------------")
                print("")
                print("Welcome")
                print("Enter exit to return")
                print("")
                print("------------------------------------")
                print("")
                print("Choose a Selection")
                print("")
                print("1. Book a Session")
                print("2. View/Cancel/Update All Sessions")
                print("3. View/Delete Users")
                while True:
                        user_input = input("Request: ")
                        if Commands.Verification.exit_input(user_input):
                            self.landing_page()
                        if user_input.isdigit():

                            match str(user_input):
                                case "1":
                                    self.booking_page()
                                    break

                                case "2":
                                    self.admin_display_all_sessions()
                                    break

                                case "3":
                                    self.admin_display_all_users()
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
                                    print("Choose a Selection")
                                    print("")
                                    print("1. Book a Session")
                                    print("2. View/Cancel/Update All Sessions")
                                    print("3. View/Delete Users")
                        else:
                            
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
                            print("2. View/Cancel/Update All Sessions")
                            print("3. View/Delete Users")









        def booking_page(self):
            if not self.check_admin():
                print("")
                print("")
                print("")
                print("------------------------------------")
                print("")
                print("Booking Session")
                print("Enter exit to return")
                print("")
                print("------------------------------------")
                print("")
                print("Enter Session Date")
                print("")
                while True:
                    date = input("Date (DD/MM/YYYY): ")
                    if Commands.Verification.exit_input(date):
                            self.dashboard_page()
                    if Commands.Verification.validate_date(date):
                        break
                    print("")
                    print("Invalid Session Date")
                    print("")

                print("")
                print("")


                while True:
                    time = input("Time (HH:MM): ")
                    if Commands.Verification.exit_input(time):
                            self.dashboard_page()
                    if Commands.Verification.validate_time(time):
                        break
                    print("")
                    print("Invalid Session Time")
                    print("")
                    
                print("")
                print("")


                date_time = Commands.Verification.validate_date_time_string(date, time)
                
                
                print("How many people will be playing (Max 6)")
                while True:
                    amount = input("Amount: ")
                    if Commands.Verification.exit_input(amount):
                            self.dashboard_page()
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
                print("")
                while True:
                    selection = input("Confirm (yes/y) or (no/n): ")
                    if Commands.Verification.exit_input(selection):
                            self.dashboard_page()
                    value = Commands.Verification.validate_selection(selection)
                    if value == True:
                        self.add_session(date_time, amount, self.user_id)
                        self.dashboard_page()
                    elif value == False:
                        self.dashboard_page()
                    print("")
                    print("")
                    print("Invalid Selection")

            else:
                print("")
                print("")
                print("")
                print("------------------------------------")
                print("")
                print("Booking Session")
                print("Enter exit to return")
                print("")
                print("------------------------------------")
                print("")
                print("Enter Session Date")
                print("")
                while True:
                    date = input("Date (DD/MM/YYYY): ")
                    if Commands.Verification.exit_input(date):
                            self.dashboard_page()
                    if Commands.Verification.validate_date(date):
                        break
                    print("")
                    print("Invalid Session Date")
                    print("")

                print("")
                print("")


                while True:
                    time = input("Time (HH:MM): ")
                    if Commands.Verification.exit_input(time):
                            self.dashboard_page()
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
                    if Commands.Verification.exit_input(amount):
                            self.dashboard_page()
                    if Commands.Verification.validate_group_size(amount):
                        break
                    print("")
                    print("Invalid Amount")
                    print("")

                print("")
                print("")

                print("Input Your First Name")

                while True:
                    f_name = input("First Name: ")
                    if Commands.Verification.exit_input(f_name):
                            self.dashboard_page()
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
                    if Commands.Verification.exit_input(l_name):
                            self.dashboard_page()
                    if Commands.Verification.validate_name(l_name):
                        break
                    print("")
                    print("")
                    print("")
                    print("Invalid Last Name ")

                print("")
                print("")

                print("")
            
                print("Input Your Phone Number e.g.(+61490767436)")
                while True:
                    phone_number = input("Phone Number: ")
                    if Commands.Verification.exit_input(phone_number):
                            self.dashboard_page()
                    if Commands.Verification.validate_phone_number(phone_number):
                        break
                    else:
                        print("")
                        print("")
                        print("")
                        print("Invalid Phone Number ")

                print("")
                print("")
                print("")
                print("Comfirm your booking")
                print(f"Date: {date}")
                print(f"Time: {time}")
                print(f"Group Size: {amount}")
                print(f"First Name: {f_name}")
                print(f"Last Name: {l_name}")
                print(f"Phone Number: {phone_number}")
                print("")
                while True:
                    selection = input("Confirm (yes/y) or (no/n): ")
                    if Commands.Verification.exit_input(selection):
                            self.dashboard_page()
                    value = Commands.Verification.validate_selection(selection)
                    if value == True:
                        self.add_session(date_time, amount, self.user_id, f_name, l_name, phone_number)
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
            print("Enter exit to return")
            print("")
            print("------------------------------------")
            print("")
            print("")
            print("")

            formated_sessions = []
            for row in all_sessions:
                date_time = datetime.datetime.strptime(str(row[1]), "%Y-%m-%d %H:%M:%S") 
                formatted_datetime = date_time.strftime("%d/%m/%Y %H:%M")
                session = [row[0] ,formatted_datetime, row[2]]
                formated_sessions.append(session)

            print(tabulate(formated_sessions, headers=['Session ID', 'Date & Time', 'Group Size'], tablefmt='orgtbl'))
            print("")
            print("")
            print("Enter Selection")
            print("1. Cancel Booking")
            print("2. Update Booking")
            print("Enter to continue")
            print("")

            
            user_input = input("Selection: ")
            if user_input == "1":
                while True:
                    print("")
                    print("Enter Session ID")
                    session_id = input("Selection: ")
                    if Commands.Verification.exit_input(session_id):
                        self.dashboard_page()

                    if session_id.isdigit():

                        self.cursor.execute(
                            """
                            SELECT * FROM Sessions 
                            WHERE SessionID = ?
                        """, (session_id))
                        session = self.cursor.fetchone()
                        if session != [] and session != None:
                            if session[3] == self.user_id:
                                print("")
                                print(f"Are you sure you want to delete session: {session_id}")
                                while True:
                                    selection = input("Confirm (yes/y) or (no/n): ")
                                    if Commands.Verification.exit_input(selection):
                                        self.dashboard_page()
                                    value = Commands.Verification.validate_selection(selection)
                                
                                    if value == True:
                                        self.remove_session(session_id)
                                        self.dashboard_page()
                                    elif value == False:
                                        self.dashboard_page()
                                    print("Invalid Selection")
                            else:
                                print(f"Invalid Session ID")

                        else:
                            print(f"Invalid Session ID")
                    else:
                        print("Must be a digit")
                        print("")

            elif user_input == "2":
                while True:
                    print("")
                    print("Enter Session ID")
                    session_id = input("Selection: ")
                    if Commands.Verification.exit_input(session_id):
                        self.dashboard_page()

                    if session_id.isdigit():

                        self.cursor.execute(
                            """
                            SELECT * FROM Sessions 
                            WHERE SessionID = ?
                        """, (session_id))
                        session = self.cursor.fetchone()
                        if session != [] and session != None:
                            if session[3] == self.user_id:
                                date_time = datetime.datetime.strptime(str(session[1]), "%Y-%m-%d %H:%M:%S")
                                updates = {}
                                print("Enter Session Date (Leave Empty for Original)")
                                print("")
                                while True:
                                    date = input("Date (DD/MM/YYYY): ")
                                    if Commands.Verification.exit_input(date):
                                            self.dashboard_page()
                                    if date == '':
                                        date = None
                                        
                                        break
                                    elif Commands.Verification.validate_date(date):
                                        stripped_date = datetime.datetime.strptime(date, "%d/%m/%Y")
                                        date = stripped_date.strftime("%Y-%m-%d")
                                        break
                                    print("")
                                    print("Invalid Session Date")
                                    print("")

                                print("")
                                print("")


                                while True:
                                    time = input("Time (HH:MM): ")
                                    if Commands.Verification.exit_input(time):
                                            self.dashboard_page()
                                    if time == '':
                                        time = None
                                        break
                                    elif Commands.Verification.validate_time(time):
                                        break
                                    print("")
                                    print("Invalid Session Time")
                                    print("")
                                    
                                print("")
                                print("")

                                if time == None and date == None:
                                    updates["DateTime"] = str(datetime.datetime.strptime(f"{str(date_time.date())} {str(date_time.time())}", "%Y-%m-%d %H:%M:%S"))
                                elif time == None:
                                    updates["DateTime"] = str(datetime.datetime.strptime(f"{str(date)} {str(date_time.time())}", "%Y-%m-%d %H:%M:%S"))
                                elif date == None:
                                    updates["DateTime"] = str(datetime.datetime.strptime(f"{str(date_time.date())} {str(time)}:00", "%Y-%m-%d %H:%M:%S"))
                                else:
                                    updates["DateTime"] = str(datetime.datetime.strptime(f"{str(date)} {str(time)}:00", "%Y-%m-%d %H:%M:%S"))

                                

                                print("How many people will be playing (Max 6) (Leave Empty for Original)")
                                while True:
                                    amount = input("Amount: ")
                                    if Commands.Verification.exit_input(amount):
                                            self.dashboard_page()
                                    if amount == '':
                                        amount = None
                                        break
                                    if Commands.Verification.validate_group_size(amount):
                                        
                                        updates["GroupAmount"] = int(amount)
                                        break
                                    print("")
                                    print("Invalid Amount")
                                    print("")

                                print("")
                                print("")

                                print("Comfirm your session update")
                                print(f"Date: {date}")
                                print(f"Time: {time}")
                                print(f"Group Size: {amount}")
                                print("")
                                while True:
                                    selection = input("Confirm (yes/y) or (no/n): ")
                                    if Commands.Verification.exit_input(selection):
                                            self.dashboard_page()
                                    value = Commands.Verification.validate_selection(selection)
                                    if value == True:
                                        self.update_session(session_id, updates)
                                        self.dashboard_page()
                                    elif value == False:
                                        self.dashboard_page()
                                    print("")
                                    print("")
                                    print("Invalid Selection")

            self.dashboard_page()




        def admin_display_all_sessions(self):
            try:
                print("")
                print("")
                print("")
                print("------------------------------------")
                print("")
                print("All Users Sessions")
                print("Enter exit to return")
                print("")
                print("------------------------------------")
                print("")
                print("")
                print("")
                self.cursor.execute("""
                SELECT * FROM Sessions
                ORDER BY DateTime;
                """)
                
                sessions = self.cursor.fetchall()
                
                formated_sessions = []
                for row in sessions:
                    self.cursor.execute("""
                    SELECT * FROM Users
                    WHERE UserID = ?;
                    """, row[3])
                    user = self.cursor.fetchone()
                    
                    date_time = datetime.datetime.strptime(str(row[1]), "%Y-%m-%d %H:%M:%S") 
                    formatted_datetime = date_time.strftime("%d/%m/%Y %H:%M")


                    if user[8] == 1:
                        session = [row[0] ,formatted_datetime, row[2], row[4], row[5], row[6], "Yes"]
                    else:
                        session = [row[0], formatted_datetime, row[2], user[1], user[2], user[5], ""]
                    
                    formated_sessions.append(session)

                print(tabulate(formated_sessions, headers=['Session ID' ,'Date & Time', 'Group Size', 'First Name', 'Last Name', 'Phone Number', 'Admin'], tablefmt='orgtbl'))
                print("")
                print("Enter Selection")
                print("1. Cancel Booking")
                print("2. Update Booking")
                print("Enter to continue")
                print("")
                
                user_input = input("Selection: ")
                if user_input == "1":
                    while True:
                        print("")
                        print("Enter Session ID")
                        session_id = input("Selection: ")
                        if Commands.Verification.exit_input(session_id):
                            self.dashboard_page()

                        if session_id.isdigit():

                            self.cursor.execute(
                                """
                                SELECT * FROM Sessions 
                                WHERE SessionID = ?
                            """, (session_id))
                            session = self.cursor.fetchone()
                            if session != [] and session != None:
                                print("")
                                print(f"Are you sure you want to delete session: {session_id}")
                                while True:
                                    selection = input("Confirm (yes/y) or (no/n): ")
                                    if Commands.Verification.exit_input(selection):
                                        self.dashboard_page()
                                    value = Commands.Verification.validate_selection(selection)
                                
                                    if value == True:
                                        self.remove_session(session_id)
                                        self.dashboard_page()
                                    elif value == False:
                                        self.dashboard_page()
                                    print("Invalid Selection")

                            else:
                                print(f"Session ID {session_id} dosn't exist")
                        else:
                            print("Must be a digit")
                            print("")
                
                if user_input == "2":
                    while True:
                        print("")
                        print("Enter Session ID")
                        session_id = input("Selection: ")
                        if Commands.Verification.exit_input(session_id):
                            self.dashboard_page()

                        if session_id.isdigit():

                            self.cursor.execute(
                                """
                                SELECT * FROM Sessions 
                                WHERE SessionID = ?
                            """, (session_id))
                            session = self.cursor.fetchone()
                            if session != [] and session != None:
                                date_time = datetime.datetime.strptime(str(session[1]), "%Y-%m-%d %H:%M:%S")
                                updates = {}
                                print("Enter Session Date (Leave Empty for Original)")
                                print("")
                                while True:
                                    date = input("Date (DD/MM/YYYY): ")
                                    if Commands.Verification.exit_input(date):
                                            self.dashboard_page()
                                    if date == '':
                                        date = None
                                        break
                                    elif Commands.Verification.validate_date(date):
                                        stripped_date = datetime.datetime.strptime(date, "%d/%m/%Y")
                                        date = stripped_date.strftime("%Y-%m-%d")
                                        break
                                    print("")
                                    print("Invalid Session Date")
                                    print("")

                                print("")
                                print("")


                                while True:
                                    time = input("Time (HH:MM): ")
                                    if Commands.Verification.exit_input(time):
                                            self.dashboard_page()
                                    if time == '':
                                        time = None
                                        break
                                    elif Commands.Verification.validate_time(time):
                                        break
                                    print("")
                                    print("Invalid Session Time")
                                    print("")
                                    
                                print("")
                                print("")

                                if time == None and date == None:
                                    updates["DateTime"] = str(datetime.datetime.strptime(f"{str(date_time.date())} {str(date_time.time())}", "%Y-%m-%d %H:%M:%S"))
                                elif time == None:
                                    updates["DateTime"] = str(datetime.datetime.strptime(f"{str(date)} {str(date_time.time())}", "%Y-%m-%d %H:%M:%S"))
                                elif date == None:
                                    updates["DateTime"] = str(datetime.datetime.strptime(f"{str(date_time.date())} {str(time)}:00", "%Y-%m-%d %H:%M:%S"))
                                else:
                                    updates["DateTime"] = str(datetime.datetime.strptime(f"{str(date)} {str(time)}:00", "%Y-%m-%d %H:%M:%S"))

                                print("How many people will be playing (Max 6) (Leave Empty for Original)")
                                while True:
                                    amount = input("Amount: ")
                                    if Commands.Verification.exit_input(amount):
                                            self.dashboard_page()
                                    if amount == '':
                                        amount = None
                                        break
                                    if Commands.Verification.validate_group_size(amount):
                                        
                                        updates["GroupAmount"] = int(amount)
                                        break
                                    print("")
                                    print("Invalid Amount")
                                    print("")

                                print("")
                                print("")
                                self.cursor.execute("""
                                SELECT * FROM Users
                                WHERE UserID = ?;
                                """, session[3])
                                user = self.cursor.fetchone()
                                
                                if user[8] == 1:
                                    print("")
                                    print("")

                                    print("Input Your First Name")

                                    while True:
                                        f_name = input("First Name: ")
                                        if Commands.Verification.exit_input(f_name):
                                                self.dashboard_page()
                                        if f_name == '':
                                            f_name = session[4]
                                            break
                                        elif Commands.Verification.validate_name(f_name):
                                            updates["FirstName"] = f_name 
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
                                        if Commands.Verification.exit_input(l_name):
                                                self.dashboard_page()
                                        if l_name == '':
                                            l_name = session[5]
                                            break
                                        elif Commands.Verification.validate_name(l_name):
                                            updates["LastName"] = l_name 
                                            break
                                        print("")
                                        print("")
                                        print("")
                                        print("Invalid Last Name ")

                                    print("")
                                    print("")

                                    print("")
                                
                                    print("Input Your Phone Number e.g.(+61490767436)")
                                    while True:
                                        phone_number = input("Phone Number: ")
                                        if Commands.Verification.exit_input(phone_number):
                                                self.dashboard_page()
                                        if phone_number == '':
                                            phone_number = session[6]
                                            break
                                        if Commands.Verification.validate_phone_number(phone_number):
                                            updates['PhoneNum'] = phone_number
                                            break
                                        else:
                                            print("")
                                            print("")
                                            print("")
                                            print("Invalid Phone Number ")

                                    print("")
                                    print("")
                                    print("")
                                    print("Comfirm your session update")
                                    print(f"Date: {date}")
                                    print(f"Time: {time}")
                                    print(f"Group Size: {amount}")
                                    print(f"First Name: {f_name}")
                                    print(f"Last Name: {l_name}")
                                    print(f"Phone Number: {phone_number}")
                                    print("")

                                else:

                                    print("Comfirm your session update")
                                    print(f"Date: {date}")
                                    print(f"Time: {time}")
                                    print(f"Group Size: {amount}")
                                    print("")

                                while True:
                                    selection = input("Confirm (yes/y) or (no/n): ")
                                    if Commands.Verification.exit_input(selection):
                                        self.dashboard_page()
                                    value = Commands.Verification.validate_selection(selection)
                                    if value == True:
                                        self.update_session(session_id, updates)
                                        self.dashboard_page()
                                    elif value == False:
                                        self.dashboard_page()
                                    print("")
                                    print("")
                                    print("Invalid Selection")

                self.dashboard_page()
            except TypeError as e:
                print(f"Error Occured {e}")
                self.landing_page()


        def admin_display_all_users(self):
            try:
                print("")
                print("")
                print("")
                print("------------------------------------")
                print("")
                print("All Users")
                print("Enter exit to return")
                print("")
                print("------------------------------------")
                print("")
                print("")
                print("")
                self.cursor.execute("""
                SELECT * FROM Users
                """)
                
                users = self.cursor.fetchall()
                
                formated_sessions = []
                for user in users:
                    if user[8] != 1:
                        row = [user[0],user[1], user[2], user[3], user[4], user[5]]
                    
                        formated_sessions.append(row)

                print(tabulate(formated_sessions, headers=['User ID', 'First Name', 'Last Name', 'Age', 'Email', 'Phone Number'], tablefmt='orgtbl'))
                print("")
                print("Enter Selection: ")
                print("1. Delete User")
                print("Enter to Continue")
                print("")
                user_input = input("Selection: ")
                if user_input == "1":
                    while True:
                        print("")
                        print("")
                        print("Enter UserID: ")
                        print("")
                        user_id = input("User ID: ")
                        if Commands.Verification.exit_input(user_id):
                            self.dashboard_page()
                        if user_id.isdigit():
                            self.cursor.execute(
                                """
                                SELECT * FROM Users
                                WHERE UserID = ?
                            """, int(user_id))
                            user = self.cursor.fetchone()
                            if user == [] or user == None:
                                print("UserID dosn't exist")
                                self.dashboard_page()
                            else:
                                print(F"Are you sure you would like to delete UserID {user_id}")
                                while True:
                                    selection = input("Confirm (yes/y) or (no/n): ")
                                    if Commands.Verification.exit_input(selection):
                                        self.dashboard_page()
                                    value = Commands.Verification.validate_selection(selection)
                                    if value == True:
                                        self.delete_user(int(user_id))
                                        self.dashboard_page()
                                    elif value == False:
                                        self.dashboard_page()
                                    print("")
                                    print("")
                                    print("Invalid Selection")
                            


                self.dashboard_page()
            except TypeError as e:
                print(f"Error Occured {e}")
                self.landing_page()






        def open_db_connection(self):
            secret_values = Commands.SecretKeyService.get_secret()
            if secret_values != None:

                print(secret_values)
                # connection_string = (
                #     r"Driver={ODBC Driver 17 for SQL Server};"
                #     f"Server={secret_values['ip']};"
                #     f"Database={str(secret_values['db'])};"
                #     f"UID={secret_values['uid']};"
                #     f"PWD={secret_values['pwd']};"
                #     r"Column Encryption Settings=Enabled;"
                # )
                connection_string = (
                    r"Driver={ODBC Driver 17 for SQL Server};"
                    r"Server=DESKTOP-AGJD7U8\SQLEXPRESS;"
                    r"Database=BowlingAlleyDB;"
                    r"Trusted_Connection=yes;"
                    
                )

                try:
                    self.conn = pyodbc.connect(connection_string)
                    print("Connection successful")
                    self.cursor = self.conn.cursor()
                    self.landing_page()
                except pyodbc.InterfaceError as e:
                    print(f"Error: {e}")

            else:
                print("Error")
                
                

        def close_db_connection(self):
            try:
                self.cursor.close()
                self.conn.close()
            except:
                print("Error")

        ###
        ### SQL QUERYS
        ###

        def delete_user(self, user_id):
            try:
                self.cursor.execute("""
                DELETE FROM Users WHERE UserID = ?;
                """, (user_id))
                self.cursor.commit()
            except:
                print("Error")
                self.landing_page()


        def update_session(self, session_id, updates):
            try:
                query = "UPDATE Sessions SET "
                pramaters = []
                for key, value in updates.items():
                    if value is not None:
                        query += f"{key} = ?, "
                        pramaters.append(value)
                query = query.rstrip(", ")
                query += " WHERE SessionID = ?"
                pramaters.append(session_id)
                print(query)
                print(pramaters)
                self.cursor.execute(query, pramaters)
                self.cursor.commit()

            except TypeError as e:
                print(f"Error {e}")
                self.landing_page()
                


        def remove_session(self, session_id):
            try:
                self.cursor.execute(
                    """
                    DELETE FROM Sessions
                    WHERE SessionID = ?
            
                """, (session_id))
                self.cursor.commit()
            except:
                print("Error")
                self.landing_page()



        def check_admin(self):
            try:
                self.cursor.execute(
                    """
                    SELECT * FROM Users 
                    WHERE UserID = ?
                """, (self.user_id))
                user = self.cursor.fetchone()
                if user[8] == 1:
                    return True
                return False
            except:
                print("Error")
                self.landing_page()
            

        # def create_user_table(self):
        #     self.cursor.execute("""
        #             CREATE TABLE Users (
        #             UserID int IDENTITY(1,1) PRIMARY KEY (UserID),
        #             FirstName nvarchar(30),
        #             LastName nvarchar(30),
        #             Age tinyint,
        #             Email nvarchar(50),
        #             PhoneNum nvarchar(13),
        #             PasswordHash nvarchar(250),
        #             SecretKeyHash nvarchar(250),
        #             Admin BIT
        #             );
        #         """)
        #     self.cursor.commit()

        # def create_session_table(self):
        #     self.cursor.execute("""
        #             CREATE TABLE Sessions (
        #             SessionID int IDENTITY(1,1) PRIMARY KEY (SessionID),
        #             DateTime smalldatetime,
        #             GroupAmount tinyint,
        #             CustomerID int FOREIGN KEY (CustomerID) REFERENCES Users (UserID)
        #             );
        #         """)
        #     self.cursor.commit()

        def return_all_users_sessions(self):
            try:
                self.cursor.execute("""
                SELECT * FROM Sessions 
                WHERE CustomerID = ?
                """, (self.user_id))
                return self.cursor.fetchall()
            except:
                print("Error")
                self.landing_page()




        def add_session(self, date_time, group_amount, user_id, f_name=None, l_name=None, phone_num=None):
            try:
                self.cursor.execute("""
                INSERT INTO Sessions (DateTime, GroupAmount, CustomerID, FirstName, LastName, PhoneNum)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (date_time, group_amount, user_id, f_name, l_name, phone_num))
                self.cursor.commit()
            except TypeError as e:
                print(f"Error {e}")
                self.dashboard_page()

        
        def add_users(self, fname, lname, age, email, phone_num, password_hash, secret_key, admin=0):
            try:
                self.cursor.execute("""
                INSERT INTO Users (FirstName, LastName, Age, Email, PhoneNum, PasswordHash, SecretKey, Admin)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (fname, lname, age, email, phone_num, password_hash, secret_key, admin))
                self.cursor.commit()
            except:
                print("Error Occured")
                self.landing_page()

        def return_user_id(self, email, password):
            try:
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
            except:
                print("Error Occured")
                self.landing_page()

        

    class Verification:
        def exit_input(input):
            if input.lower() == 'exit':
                return True
            return False


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
                input_date = datetime.datetime.strptime(date, "%d/%m/%Y")

                if datetime.datetime.now() < input_date <= datetime.datetime.now() + datetime.timedelta(days=10*365.25): 
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
            month = int(date_list[1] )
            year = int(date_list[2] )
            hours = int(time_list[0] )
            minutes = int(time_list[1] )
            return f"{year}-{month}-{day} {hours}:{minutes}:00"
             

    class TwoFactor:
        def create_secret_key():
            return pyotp.random_base32()
        
        def verify_key_login(user_id, cursor):
            cursor.execute("""
                SELECT * FROM Users WHERE UserID = ?
            """, (user_id))
            user = cursor.fetchone()
            
            totp = pyotp.TOTP(user[7])
            otp = input("Enter the OTP: ")
            if totp.verify(otp):
                return True
            return False

        def verify_key_create(key):
            totp = pyotp.TOTP(key)
            
            uri = pyotp.totp.TOTP(key).provisioning_uri(name="Spare Bowling Alley")
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(uri)
            qr.make(fit=True) 
            img = qr.make_image(fill_color="black", back_color="white")
            img.show()

            
            otp = input("Enter the OTP: ")
            if totp.verify(otp):
                return True
            return False

    class SecretKeyService:
        def get_secret():
            try:
                client = boto3.client(
                "secretsmanager", 
                aws_access_key_id=f"{os.environ['AWS_ACCESS_KEY_ID']}",
                aws_secret_access_key=f"{os.environ['AWS_SECRET_ACCESS_KEY']}",
                region_name=f"{os.environ['AWS_REGION_NAME']}")

            
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
                