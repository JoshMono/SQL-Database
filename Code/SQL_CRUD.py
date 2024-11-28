import pyodbc
from argon2 import PasswordHasher
import os

Hasher = PasswordHasher()
# class Querys:

#     ###
#     ### Hashing and Verify Passwords 
#     ###

#     def HashPassword(password):
#         return Hasher.hash(password)

#     def VerifyPassword(username, password):
#         cursor.execute("SELECT * FROM Users WHERE Username = ?", (username,))
#         user = cursor.fetchone()
#         if Hasher.verify(user[2], password):
#             return user
#         return False

#     ###
#     ### CRUD Querys 
#     ###

#     def AddUser(username, age, email, phone_number, password):
#         username = username.lower()
#         cursor.execute("SELECT * FROM Users WHERE Username = ?", (username,))
#         users = cursor.fetchall()
#         if users == []:
#             hash_password = Querys.HashPassword(password)
#             cursor.execute("""
#                 INSERT INTO Users (Username, Age, Email, PhoneNum, Password_Hash)
#                 VALUES (?, ?, ?, ?, ?)
#             """, (username, age, email, phone_number, hash_password))
#             cursor.commit()
#             return True
#         return False

#     def DeleteUser(username, password):
#         if Querys.VerifyPassword(username, password):
#             cursor.execute("""
#                 DELETE FROM Users
#                 WHERE Username = ? AND ;
#             """, (username,))
#             cursor.commit()

#     def UpdateRecord(user_id, new_username):
#         cursor.execute("""
#             UPDATE Users
#             SET
#             Username = ?
#             WHERE UserID = ?;
#         """, (new_username, user_id))
#         cursor.commit()

#     ###
#     ### Create Tables
#     ###

    
        
        

# connection_string = (
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=JOSH-YOGA-7\SQLEXPRESS;"
#     "Database=BowlingAlleyDB;"
#     "Trusted_Connection=yes;"
#     )


class Querys:
    class SQL_Querys:
        def CreateUserTable():
            cursor.execute("""
                    CREATE TABLE Users (
                    UserID int IDENTITY(1,1) PRIMARY KEY (UserID),
                    FirstName nvarchar(25),
                    LastName nvarchar(35),
                    Age tinyint,
                    Email nvarchar(50),
                    PhoneNum nvarchar(15),
                    Password_Hash nvarchar(250),
                    );
                """)
            cursor.commit()


    class Validation:
        
    
    class TwoFactor:
        def create_secret_key():
            pass

if Querys.Validation.validate_email("erfghnmknjnjn@gmail.com"):
    print("Valide")
else:
    print("wrong")


import pyotp
import qrcode
import os



secret = pyotp.random_base32()
print(f"Your secret key: {secret}")

totp = pyotp.TOTP("IUXAKN4AK35BF77M54H6V35C4WH2XSLF")
uri = totp.provisioning_uri(name='user@example.com', issuer_name='YourAppName')

qr = qrcode.make(uri)
qr.save("qrcode.png")

print("QR code generated and saved as qrcode.png")
 
file_path = os.path.abspath("qrcode.png")
print(f"Open the QR code image: file://{file_path}")

# Step 4: Verify the OTP
# otp = input("Enter the OTP: ")
# if totp.verify(otp):
#     print("OTP is valid")
# else:
#     print("Invalid OTP")


os.environ['DB_PASSWORD'] = r"2o%.:c;4T#FPyp8';fmMGb=C8CSF:IlM&[}m23v85I%rSK`Mj;"

connection_string = (
    r"Driver={ODBC Driver 17 for SQL Server};"
    r"Server=10.221.64.20\SQLEXPRESS;"
    r"Database=BowlingAlleyDB;"
    r"UID=BowlingUserAccount;"
    r"PWD=bRe3IprUKe@hE2LsW9!Vlbrus$PeylstigiCrIch%eBrOdUTRyaw;"
    r"Column Encryption Settings=Enabled;"
)

print(connection_string)

try:
    conn = pyodbc.connect(connection_string)
    print("Connection successful")
    cursor = conn.cursor()

    cursor.close()
    conn.close()
    
except pyodbc.InterfaceError as e:
    print(f"Error: {e}")



# cursor.execute("""
#             CREATE TABLE Person (
#             Name nvarchar(50),
#             );
#         """)
# cursor.commit()


# Querys.CreateUserTable()
# if not Querys.AddUser("Test12", 30, "test@gmail.com", "0490 767 412" ,"12345"):
#     print("Username already taken")
# else:
#     print("Success")

# cursor.execute("""
#     INSERT INTO Person (Name)
#     VALUES (?);
# """, ("Josh"))
# cursor.commit()

# users = cursor.execute("""
#     SELECT * FROM Person;
# """)

# for i in users:
#     print(i)






