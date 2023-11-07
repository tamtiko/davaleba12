CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(50)
);

CREATE TABLE EmployeeDetails (
    EmployeeDetailsID INT PRIMARY KEY,
    EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID),
    PassportNumber VARCHAR(50),
    PassportExpiryDate DATE
);

CREATE TABLE Address (
    AddressID INT PRIMARY KEY,
    EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID),
    AddressLine1 VARCHAR(50),
    AddressLine2 VARCHAR(50),
    City VARCHAR(50),
    State VARCHAR(50),
    Country VARCHAR(50),
    ZipCode VARCHAR(50)
);

CREATE TABLE Skill (
    SkillID INT PRIMARY KEY,
    SkillName VARCHAR(50)
);

CREATE TABLE EmployeeSkill (
    EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID),
    SkillID INT FOREIGN KEY REFERENCES Skill(SkillID),
    ProficiencyLevel INT
);