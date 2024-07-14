create database jud1;
use jud1;
CREATE TABLE CD_COMPLETED(
case_id varchar(225),
case_type varchar(225),
date_of_commencement varchar(225),
final_judgement_date varchar(225),
judge_id varchar(225),
defendant_name varchar(225),
prosecutor_name varchar(225),
Full_documentation varchar(225)
);


CREATE TABLE CD_PENDING(
case_id varchar(225),
case_type varchar(225),
date_of_commencement varchar(225),
next_hearing_date varchar(225),
judge_id varchar(225),
defendant_name varchar(225),
prosecutor_name varchar(225),
Full_documentation varchar(225)
);


CREATE TABLE PENDING(
case_id varchar(225),
documented_name varchar(225)
);

CREATE TABLE COMPLETED(
case_id varchar(225),
documented_name varchar(225)
);

CREATE TABLE JUDGE(
judge_id varchar(225) ,
judge_name varchar(225),
court_name varchar(225),
tenure varchar(225)
);

CREATE TABLE ADVOCATE(
reg_num varchar(225) UNIQUE,
advocate_name varchar(225),
bar_council varchar(225),
age int,
cases_won int,
cases_lost int
);

CREATE TABLE COURTS(
court_id VARCHAR (100),
court_name VARCHAR(100) UNIQUE ,
city VARCHAR(100),
judges int
);

CREATE TABLE JURISDICTION
( 

	court_name varchar(225) UNIQUE,
	jurisdiction varchar(225)
);

