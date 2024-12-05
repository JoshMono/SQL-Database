
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

CREATE TABLE Sessions (
    SessionID int IDENTITY(1,1) PRIMARY KEY (SessionID),
    DateTime smalldatetime,
    GroupAmount tinyint,
    CustomerID int FOREIGN KEY (CustomerID) REFERENCES Users (UserID) ON DELETE CASCADE, 
    FirstName nvarchar(30) NULL,
    LastName nvarchar(30) NULL,
    PhoneNum nvarchar(13) NULL
);