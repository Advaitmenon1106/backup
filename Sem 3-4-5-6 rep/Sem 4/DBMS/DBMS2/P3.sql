/* CREATE database EMPLOYEE_DATABASE2;
USE EMPLOYEE_DATABASE2;

CREATE TABLE DEPARTMENT(
DName VARCHAR (200),
DNumber INT,
Mgr_ssn INT,
Mgr_start_date VARCHAR (150)
);

CREATE TABLE EMPLOYEE(
Ssn INT,
Fname CHAR(100),
Minit CHAR(100),
Lname CHAR(100),
BDate VARCHAR(100),
Address VARCHAR(250),
Sex VARCHAR (2),
Super_Ssn INT,
Dno INT,
Salary INT
);

CREATE TABLE DPT_LOCATIONS(
Dnumber INT,
Dlocation VARCHAR
);

CREATE TABLE PROJECTS(
Pname VARCHAR (200),
Pnumber INT,
PLocation VARCHAR (250),
Dnum INT
);

CREATE TABLE WORKS_ON(
Ssn INT,
Pno INT,
Hours INT
);

CREATE TABLE DEPENDENTS(
Ssn INT,
DEPENDENT_NAME VARCHAR(250),
GENDER VARCHAR (250),
Bdate VARCHAR (200),
RELATIONSHIP VARCHAR (250)
);


# Entering values


INSERT INTO Employee (Fname, Minit, Lname, Ssn, BDate, Address, Sex, Salary, Super_Ssn, Dno) VALUES ('John','B','Smith',123456789,'1965-01-09','731 Fondren, Houston, TX','M',30000,333445555,5);
INSERT INTO Employee (Fname, Minit, Lname, Ssn, BDate, Address, Sex, Salary, Super_Ssn, Dno) VALUES ('Franklin','T','Wong',333445555,'1955-12-08','638 Voss, Houston, TX','M',40000,888665555,5);
INSERT INTO Employee (Fname, Minit, Lname, Ssn, BDate, Address, Sex, Salary, Super_Ssn, Dno) VALUES ('Alicia','J','Zelaya',999887777,'1968-01-19','3321 Castle, Spring, TX','F',25000,987654321,4);
INSERT INTO Employee (Fname, Minit, Lname, Ssn, BDate, Address, Sex, Salary, Super_Ssn, Dno) VALUES('Jennifer','S','Wallace',987654321,'1941-06-20','291 Berry, Bellaire, TX','F',43000,888665555,4);
INSERT INTO Employee (Fname, Minit, Lname, Ssn, BDate, Address, Sex, Salary, Super_Ssn, Dno) VALUES ('Ramesh','K','Narayan',666884444,'1962-09-15','975 Fire Oak, Humble, TX','M',38000,333445555,5);
INSERT INTO Employee (Fname, Minit, Lname, Ssn, BDate, Address, Sex, Salary, Super_Ssn, Dno) VALUES ('Joyce','A','English',453453453,'1972-07-31','5631 Rice, Houston, TX','F',25000,333445555,5);
INSERT INTO Employee (Fname, Minit, Lname, Ssn, BDate, Address, Sex, Salary, Super_Ssn, Dno) VALUES ('Ahmad','V','Jabbar',987987987,'1969-03-29','980 Dallas, Houston, TX','M',25000,987654321,4);
INSERT INTO Employee (Fname, Minit, Lname, Ssn, BDate, Address, Sex, Salary, Super_Ssn, Dno) VALUES ('James','E','Borg',888665555,'1937-11-10','450 Stone, Houston, TX','M',55000,NULL,1);


INSERT INTO DEPARTMENT (DName, DNumber, Mgr_ssn, Mgr_start_date) VALUES ('Research',5,333445555,'1985-05-22');
INSERT INTO DEPARTMENT (DName, DNumber, Mgr_ssn, Mgr_start_date) VALUES ('Administration',4,987654321,'1995-01-01');
INSERT INTO DEPARTMENT (DName, DNumber, Mgr_ssn, Mgr_start_date) VALUES ('Headquarters',1,888665555,'1981-06-19');
*/

/*ALTER TABLE DPT_LOCATIONS
MODIFY COLUMN Dlocation VARCHAR(100);
INSERT INTO DPT_LOCATIONS (DNumber, Dlocation) VALUES(1, 'Houston');
INSERT INTO DPT_LOCATIONS (DNumber, Dlocation) VALUES(4, 'Stafford');
INSERT INTO DPT_LOCATIONS (DNumber, Dlocation) VALUES(5, 'Bellaire');
INSERT INTO DPT_LOCATIONS (DNumber, Dlocation) VALUES(5, 'Sugarland');
INSERT INTO DPT_LOCATIONS (DNumber, Dlocation) VALUES(5, 'Houston');*/

/*INSERT INTO PROJECTS (Pname, Pnumber, PLocation, Dnum) VALUES ('ProductX', 1, 'Bellaire', 5),
('ProductY', 2, 'Sugarland', 5),
('ProductZ', 3, 'Houston', 5),
('Computerization', 10, 'Stafford', 4),
('Reorganization', 20, 'Houston', 1),
('Newbenefits', 30, 'Stafford', 4);*/


/*
INSERT INTO WORKS_ON(Ssn, Pno, Hours)  VALUES (123456789, 1, 32.5);
INSERT INTO WORKS_ON(Ssn, Pno, Hours)  VALUES (123456789, 2, 7.5);
INSERT INTO WORKS_ON(Ssn, Pno, Hours)  VALUES (666884444, 3, 40.0);
INSERT INTO WORKS_ON (Ssn, Pno, Hours) VALUES (453453453, 1, 20.0);
INSERT INTO WORKS_ON (Ssn, Pno, Hours) VALUES (453453453, 2, 20.0);
INSERT INTO WORKS_ON (Ssn, Pno, Hours) VALUES (333445555, 2, 10.0);
INSERT INTO WORKS_ON (Ssn, Pno, Hours) VALUES (333445555, 3, 10.0);
INSERT INTO WORKS_ON (Ssn, Pno, Hours) VALUES (333445555, 10, 10.0);
INSERT INTO WORKS_ON (Ssn, Pno, Hours) VALUES (333445555, 20, 10.0);
INSERT INTO WORKS_ON (Ssn, Pno, Hours) VALUES (999887777, 30, 30.0);
INSERT INTO WORKS_ON (Ssn, Pno, Hours) VALUES (999887777, 10, 10.0);
INSERT INTO WORKS_ON (Ssn, Pno, Hours) VALUES (987987987, 10, 35.0);
INSERT INTO WORKS_ON (Ssn, Pno, Hours) VALUES  (987987987, 30, 5.0);
INSERT INTO WORKS_ON (Ssn, Pno, Hours) VALUES (987654321, 30, 20.0);
INSERT INTO WORKS_ON (Ssn, Pno, Hours) VALUES (987654321, 20, 15.0);
INSERT INTO WORKS_ON (Ssn, Pno, Hours) VALUES (888665555, 20, NULL);
*/
/*
INSERT INTO DEPENDENTS (Ssn, DEPENDENT_NAME, GENDER, Bdate, RELATIONSHIP) VALUES(333445555, 'Alice', 'F', '1986-04-05', 'Daughter');
INSERT INTO DEPENDENTS (Ssn, DEPENDENT_NAME, GENDER, Bdate, RELATIONSHIP) VALUES (333445555, 'Theodore', 'M', '1983-10-25', 'Son');
INSERT INTO DEPENDENTS (Ssn, DEPENDENT_NAME, GENDER, Bdate, RELATIONSHIP) VALUES(333445555, 'Joy', 'F', '1958-05-03', 'Spouse');
INSERT INTO DEPENDENTS (Ssn, DEPENDENT_NAME, GENDER, Bdate, RELATIONSHIP) VALUES(987654321, 'Abner', 'M', '1942-02-28', 'Spouse');
INSERT INTO DEPENDENTS (Ssn, DEPENDENT_NAME, GENDER, Bdate, RELATIONSHIP) VALUES(123456789, 'Michael', 'M', '1988-01-04', 'Son');
INSERT INTO DEPENDENTS (Ssn, DEPENDENT_NAME, GENDER, Bdate, RELATIONSHIP) VALUES(123456789, 'Alice', 'F', '1988-12-30', 'Daughter');
INSERT INTO DEPENDENTS (Ssn, DEPENDENT_NAME, GENDER, Bdate, RELATIONSHIP) VALUES(123456789, 'Elizabeth', 'F', '1967-05-05', 'Spouse');
*/
SELECT * FROM EMPLOYEE;
SELECT * FROM DEPENDENTS;
SELECT * FROM WORKS_ON;
SELECT * FROM DPT_LOCATIONS;
SELECT * FROM PROJECTS;
SELECT * FROM DEPARTMENT;


# Make Foreign and primary keysdepartment

# Q1
SELECT * FROM EMPLOYEE WHERE Fname = "John";

# Q2
SELECT * FROM EMPLOYEE, DEPARTMENT WHERE DName = "Research";

# Q3
SELECT Pnumber, Dnumber, Lname, Address FROM DEPARTMENT, EMPLOYEE, PROJECTS WHERE Mgr_ssn = Ssn and Dnumber = Dnum and Plocation = "Stafford";

#Q4

SELECT Pnumber FROM PROJECTS, EMPLOYEE WHERE Lname = 'Smith';

#Q5

SELECT * FROM EMPLOYEE WHERE Address LIKE '%HOUSTON%';

#Q6

SELECT * FROM EMPLOYEE WHERE BDate LIKE '%195';

#Q7

SELECT Salary+(0.1*Salary) FROM EMPLOYEE, PROJECTS WHERE Pname = 'ProductX';

#Q8

SELECT * FROM EMPLOYEE, dpt_locations WHERE Dnumber = 5 AND Salary BETWEEN 30000 AND 40000;

#Q9

SELECT * FROM EMPLOYEE, works_on, projects
ORDER BY Lname, Fname;

#Q10

SELECT Fname, Lname FROM EMPLOYEE, department WHERE Mgr_ssn = Ssn;

#Q11

SELECT distinct Fname, Lname from Employee, Department where Mgr_ssn != Ssn;

#Q12

SELECT Fname, Lname, Dependent_name from Employee, Dependents where Fname = Dependent_name and Employee.Sex = Dependents.Gender;

#Q13

SELECT DISTINCT Fname, Minit, Lname from Employee, Dependents where employee.ssn != dependents.ssn;
#Q14

SELECT DISTINCT Fname, Minit, Lname from Employee, Department, Dependents where employee.ssn = Mgr_ssn and Mgr_ssn = dependents.Ssn;

#Q15

SELECT DISTINCT Ssn, Pname, Pnumber from Employee, Projects where Pnumber = 1 or Pnumber = 2 or Pnumber = 3 
order by Pnumber asc;

#Q16

SELECT MIN(SALARY) FROM EMPLOYEE;
SELECT MAX(SALARY) FROM EMPLOYEE;
SELECT avg(SALARY) FROM EMPLOYEE;

#Q17

SELECT SUM(SALARY) FROM EMPLOYEE, DEPARTMENT WHERE DName = "Research";

#Q18

select COUNT(Ssn) from employee;

#Q19

select count(Ssn) from employee, department where DName = "Research";

#Q20

select count(distinct(salary)) from employee;


#Q21
select Dnumber, count(works_on.ssn), avg(Salary) from employee, department, projects, works_on group by Dnumber;

#Q22
select Pnumber, Pname, count(works_on.ssn) as NoOfEmployees from projects, works_on where projects.Pnumber= works_on.Pno GROUP BY projects.Pnumber, Projects.Pname;

#Q23

select Pnumber, Pname, count(works_on.ssn) as CountOfEmployees from projects, works_on where projects.Pnumber= works_on.Pno GROUP BY projects.Pnumber, Projects.Pname having CountOfEmployees>2;

#Q24

select Pnumber, Pname, count(works_on.ssn) as Count from projects, works_on where projects.Pnumber = works_on.Pno and projects.Dnum = 5 group by projects.Pnumber, Projects.Pname;

#Q25
select d.Dnumber, count(e.SSN) as num_employees_above_40k from Department d join Employee e on d.Dnumber = e.Dno where e.Salary > 40000 group by d.Dnumber having count(e.SSN) > 5;