
-- Use the database
USE BowlingAlleyDB;

CREATE TABLE Users (
    UserID int IDENTITY(1,1) PRIMARY KEY (UserID),
    FirstName nvarchar(30),
    LastName nvarchar(30),
    Age tinyint,
    Email nvarchar(50),
    PhoneNum nvarchar(13),
    PasswordHash nvarchar(250),
    SecretKey nvarchar(250),
    Admin BIT
);

INSERT INTO Users (FirstName, LastName, Age, Email, PhoneNum, PasswordHash, SecretKey, Admin) 
VALUES ('Mark', 'Brandon', 39, 'mark@sparebowling.com', '+61490787457', '$argon2id$v=19$m=65536,t=3,p=4$FDzJgoHS5ULYg7pPYClCEQ$G1BxwAzXKnv2Vxw+q9Lb55p2fS5oOKRMfNPicypOwFg', 'OEBV3OKWGCA2A6FVCSRFDMPO6SRIRPKO', 1);

CREATE TABLE Sessions (
    SessionID int IDENTITY(1,1) PRIMARY KEY (SessionID),
    DateTime smalldatetime,
    GroupAmount tinyint,
    CustomerID int FOREIGN KEY (CustomerID) REFERENCES Users (UserID),
    FirstName nvarchar(30) NULL,
    LastName nvarchar(30) NULL,
    PhoneNum nvarchar(13) NULL
);