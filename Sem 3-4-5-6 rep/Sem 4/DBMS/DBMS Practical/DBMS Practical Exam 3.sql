/*CREATE database CarsAcc2;
USE CarsAcc2;

CREATE TABLE PERSON (
Driver_ID VARCHAR (50),
DNAME VARCHAR(100),
ADDRESS VARCHAR(200)
);

CREATE TABLE CARS(
RegNo VARCHAR (50),
Model VARCHAR (100),
CYear INT
);

CREATE TABLE OWNS(
DriverID VARCHAR (50),
RegNo VARCHAR (50)
);

CREATE TABLE ACCIDENT(
﻿Report_Number VARCHAR (100),
AccDate VARCHAR(50),
Location VARCHAR (100)
);

CREATE TABLE PARTICIPATED (
Driver_ID VARCHAR (50),
RegNo VARCHAR (50),
Report_No VARCHAR (100),
Damage_Amt INT
);

﻿INSERT INTO PERSON (Driver_ID,DName,Address) VALUES 
('DI12335','Alan Paige','Address_Alan@1234'),
('DI24567','Abel Smith','Address_Abel@1278'),
('DI15623','John Smith','Address_John@2039'),
('DI91865','John Walter','Address_John@7821'),
('DI74310','Kate Walker','Address_Kate@3401'),
('DI59234','Catherine Peralta','Address_Cath@9021');

INSERT INTO CARS VALUES
('AACC1010','Honda',1989),
('AABB2000','Mazda',1989),
('AABB4520','Mazda',2000),
('ABAB1234','Toyota',2009),
('ACDE0916','Ferrari',1980),
('ANMD2941','Peugeot',1991);

INSERT INTO OWNS VALUES
('DI15623','AABB4520'),
('DI91865','ABAB1234'),
('DI74310','AACC1010'),
('DI12335','AABB2000'),
('DI24567','ACDE0916'),
('DI59234','ANMD2941');

INSERT INTO ACCIDENT VALUES
('AR2001','25-06-1991','Texas'),
('AR2036','25-12-1989','California'),
('AR2197','25-01-1989','Alabama'),
('AR4561','19-07-2005','Texas'),
('AR2107','18-11-2020','New York'),
('AR3590','23-04-1998','New York');

INSERT INTO PARTICIPATED VALUES
('DI15623','AABB2000','AR2197',2500),
('DI91865','ABAB1234','AR2001',2100),
('DI74310','AACC1010','AR2107',4500),
('DI12335','AABB4520','AR2036',1457),
('DI24567','ACDE0916','AR3590',1000),
('DI59234','ANMD2941','AR4561',2300);*/

﻿/*INSERT INTO PERSON VALUES 
('DI12335','Alan Paige','Address_Alan@1234'),
('DI24567','Abel Smith','Address_Abel@1278'),
('DI15623','John Smith','Address_John@2039'),
('DI91865','John Walter','Address_John@7821'),
('DI74310','Kate Walker','Address_Kate@3401'),
('DI59234','Catherine Peralta','Address_Cath@9021');*/

#a.
select * from accident;
SELECT COUNT(Report_Number) from Accident where AccDate like '%1989';

#b.
select count(report_number) from participated part, person p where p.driver_id = part.driver_id and p.name = "John Smith";

#c.

