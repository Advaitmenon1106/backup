/*create database university;
use university;

create table classroom
(building varchar (15),
room_number varchar (7),
capacity numeric (4,0),
primary key (building, room_number));

create table department
(dept_name varchar (20),
building varchar (15),
budget int,
primary key (dept_name));

create table course
(course_id varchar (8),
title varchar (50),
dept_name varchar (20),
credits int,
primary key (course_id),
foreign key (dept_name) references department(dept_name));

create table instructor
(instructor_id varchar (5),
iname varchar (20),
dept_name varchar (20),
salary int,
primary key (instructor_id),
foreign key (dept_name) references department(dept_name));

create table section
(course_id varchar (8),
sec_id int,
semester varchar(10),
yearof int,
building varchar (15),
room_number varchar (7),
time_slot_id varchar (4),
foreign key (course_id) references course(course_id),
foreign key (building, room_number) references classroom(building, room_number),
primary key (course_id, sec_id, semester, yearof));

create table teaches
(instructor_id varchar (5),
course_id varchar (8),
sec_id int,
semester varchar(10),
yearof int,
primary key (instructor_id, course_id, sec_id, semester, yearof),
foreign key (course_id, sec_id, semester, yearof) references section(course_id, sec_id, semester, yearof),
foreign key (instructor_id) references instructor(instructor_id));

create table student
(student_id varchar (5),
sname varchar (20) not null,
dept_name varchar (20),
tot_cred int,
primary key (student_id),
foreign key (dept_name) references department(dept_name));

create table takes
(student_id varchar (5),
course_id varchar (8),
sec_id int,
semester varchar(10),
yearof int,
grade varchar (10) default null,
foreign key (course_id, sec_id, semester, yearof) references section(course_id, sec_id, semester, yearof),
foreign key (student_id) references student(student_id),
primary key (student_id, course_id, sec_id, semester, yearof));

create table advisor
(student_id varchar (5),
instructor_id varchar (5),
primary key (student_id, instructor_id),
foreign key (instructor_id) references instructor (instructor_id),
foreign key (student_id) references student (student_id));

create table prereq
(course_id varchar(8),
prereq_id varchar(8),
primary key (course_id, prereq_id),
foreign key (course_id) references course(course_id),
foreign key (prereq_id) references course(course_id));

create table timeslot
(time_slot_id varchar (4),
dayw varchar(1),
start_time int,
end_time int,
primary key (time_slot_id, dayw, start_time));

insert into classroom values
("Packard", '101', 500),
("Painter", '514', 10),
("Taylor", '3128', 70),
("Watson", '100', 30),
("Watson", '120', 50);

insert into department values
("Biology", "Watson", 90000),
("Comp. Sci", "Taylor", 100000),
("Elec. Eng", "Taylor", 85000),
("Finance", "Painter", 120000),
("History", "Painter", 50000),
("Music", "Packard", 80000),
("Physics", "Watson", 70000);

insert into course values
("BIO-101", "Intro to Biology", "Biology", 4),
("BIO-301", "Genetics", "Biology", 4),
("BIO-399", "Computational Biology", "Biology", 3),
("CS-101", "Intro to Computer Science", "Comp. Sci", 4),
("CS-190", "Game Design", "Biology", 4),
("CS-315", "Robotics", "Biology", 3),
("CS-319", "Image Processing", "Comp. Sci", 3),
("CS-347", "Database System Concepts", "Comp. Sci", 3),
("EE-181", "Intro to Digital Systems", "Elec. Eng", 3),
("FIN-201", "Investment Banking", "Finance", 3),
("HIS-351", "World History", "History", 3),
("MU-199", "Music Video Production", "Music", 3),
("PHY-101", "Physical Principles", "Physics", 4);

desc instructor;
insert into instructor values
('10101', "Srinivasan", "Comp. Sci", 65000),
('12121', "Wu", "Finance", 90000),
('15151', "Mozart", "Music", 40000),
('22222', "Einstein", "Physics", 95000),
('32343', "El Said", "History", 60000),
('33456', "Gold", "Comp. Sci", 75000),
('58583', "Califieri", "History", 62000),
('76543', "Singh", "Finance", 80000),
('76766', "Crick", "Biology", 72000),
('83821', "Brandt", "Comp. Sci", 92000),
('98345', "Kim", "Elec. Eng", 80000);

insert into timeslot values
("A", "M", 8.00, 8.50),
("A", "W", 8.00, 8.50),
("A", "F", 8.00, 8.50),
("B", "M", 9.00, 9.50),
("B", "W", 9.00, 9.50),
("B", "F", 9.00, 9.50),
("C", "M", 11.00, 11.50),
("C", "W", 11.00, 11.50),
("C", "F", 11.00, 11.50),
("D", "M", 13.00, 13.50),
("D", "W", 13.00, 13.50),
("D", "F", 13.00, 13.50),
("E", "T", 10.30, 11.45),
("E", "R", 10.30, 11.45),
("F", "T", 14.30, 15.45),
("F", "R", 14.30, 15.45),
("G", "M", 16.00, 16.50),
("G", "W", 16.00, 16.50),
("G", "F", 16.00, 16.50),
("H", "W", 10.00, 12.30);

desc section;
insert into section(course_id, sec_id, semester, yearof, building, room_number, time_slot_id) values
("BIO-101", 1, "Summer", 2009, "Painter", '514', "B"),
("BIO-301", 1, "Summer", 2010, "Painter", '514', "A"),
("CS-101", 1, "Fall", 2009, "Packard", '101', "H"),
("CS-101", 1, "Spring", 2010, "Packard", '101', "F"),
("CS-190", 1, "Spring", 2009, "Taylor", '3128', "E"),
("CS-190", 2, "Spring", 2009, "Taylor", '3128', "A"),
("CS-315", 1, "Spring", 2010, "Watson", '120', "D"),
("CS-319", 1, "Spring", 2010, "Watson", '100', "B"),
("CS-319", 2, "Spring", 2010, "Taylor", '3128', "C"),
("CS-347", 1, "Fall", 2009, "Taylor", '3128', "A"),
("EE-181", 1, "Spring", 2009, "Taylor", '3128', "C"),
("FIN-201", 1, "Spring", 2010, "Packard", '101', "B"),
("HIS-351", 1, "Spring", 2010, "Painter", '514', "C"),
("MU-199", 1, "Spring", 2010, "Packard", '101', "D"),
("PHY-101", 1, "Fall", 2009, "Watson", '100', "A");


insert into teaches values
('10101', "CS-101", 1, "Fall", 2009),
('10101', "CS-315", 1, "Spring", 2010),
('10101', "CS-347", 1, "Fall", 2009),
('10101', "FIN-201", 1, "Spring", 2010),
('12121', "MU-199", 1, "Spring", 2010),
('22222', "PHY-101", 1, "Fall", 2009),
('32343', "HIS-351", 1, "Spring", 2010),
('22222', "CS-101", 1, "Spring", 2010),
('22222', "CS-319", 1, "Spring", 2010),
('76766', "BIO-101", 1, "Summer", 2009),
('76766', "BIO-301", 1, "Summer", 2010),
('83821', "CS-190", 1, "Spring", 2009),
('83821', "CS-190", 2, "Spring", 2009),
('83821', "CS-319", 2, "Spring", 2010),
('98345', "EE-181", 1, "Spring", 2009);

insert into student values
('00128', "Zhang", "Comp. Sci", 102),
('12345', "Shankar", "Comp. Sci", 32),
('19991', "Brandt", "History", 80),
('23121', "Chavez", "Finance", 110),
('44553', "Peltier", "Physics", 56),
('45678', "Levy", "Physics", 46),
('54321', "Williams", "Comp. Sci", 54),
('55739', "Sanchez", "Music", 38),
('70557', "Snow", "Physics", 0),
('76543', "Brown", "Comp. Sci", 58),
('76653', "Aoi", "Elec. Eng", 60),
('98765', "Bouriks", "Elec. Eng", 98),
('98988', "Tanaka", "Biology", 120);

insert into takes(student_id, course_id, sec_id, semester, yearof, grade) values
('00128', "CS-101", 1, "Fall", 2009, "A"),
('00128', "CS-347", 1, "Fall", 2009, "A-"),
('12345', "CS-101", 1, "Fall", 2009, "C"),
('12345', "CS-190", 2, "Spring", 2009, "A"),
('12345', "CS-315", 1, "Spring", 2010, "A"),
('12345', "CS-347", 1, "Fall", 2009, "A"),
('19991', "HIS-351", 1, "Spring", 2010, "B"),
('23121', "FIN-201", 1, "Spring", 2010, "C+"),
('44553', "PHY-101", 1, "Fall", 2009, "B-"),
('45678', "CS-101", 1, "Fall", 2009, "F"),
('45678', "CS-101", 1, "Spring", 2010, "B+"),
('45678', "CS-319", 1, "Spring", 2010, "B"),
('54321', "CS-101", 1, "Fall", 2009, "A-"),
('54321', "CS-190", 2, "Spring", 2009, "B+"),
('55739', "MU-199", 1, "Spring", 2010, "A-"),
('76543', "CS-101", 1, "Fall", 2009, "A"),
('76543', "CS-319", 2, "Spring", 2010, "A"),
('76653', "EE-181", 1, "Spring", 2009, "C"),
('98765', "CS-101", 1, "Fall", 2009, "C-"),
('98765', "CS-315", 1, "Spring", 2010, "B"),
('98988', "BIO-101", 1, "Summer", 2009, "A"),
('98988', "BIO-301", 1, "Summer", 2010, null);

insert into advisor values
('00128', '22222'),
('12345', '10101'),
('23121', '76543'),
('44553', '22222'),
('45678', '22222'),
('76543', '22222'),
('76653', '98345'),
('98765', '98345'),
('98988', '76766');

insert into prereq values
("BIO-301", "BIO-101"),
("BIO-399", "BIO-101"),
("CS-190", "CS-101"),
("CS-315", "CS-101"),
("CS-319", "CS-101"),
("CS-347", "CS-101"),
("EE-181", "PHY-101");
*/

/*
3. Find their names and the course ID of all courses they taught for all
instructors in the university who have taught some course.
5. Find the names of all instructors whose salary is greater than at least one
instructor in the Biology department.
14.Find the average salary of all instructors
15.For each course section offered in 2009, find the average total credits (tot
cred) of all students enrolled in the section, if the section had at least 2
students
16.Find all the courses taught in the Fall 2009 semester but not in the Spring
2010 semester
17.Find the total number of (distinct) students who have taken course sections
taught by the instructor with ID 110011
18.Find all courses that were offered at least twice in 2009”
19.Delete all tuples in the instructor relation pertaining to instructors in the
Finance department.
20.Delete all instructors with a salary between $13,000 and $15,000.
21 Find the titles of courses in the Comp. S i. department that has 3 credits.
22. Find the IDs of all students who were taught by an instructor named Einstein;
make sure there are no duplicates in the result.
23.Find the highest salary of any instructor.
24.. Find all instructors earning the highest salary (there may be more than one
with the same salary).
25.. Find the enrollment of each section that was offered in Fall 2017.
26. Find the maximum enrollment, across all sections, in Fall 2017.
27.. Find the sections that had the maximum enrollment in Fall 2017.
*/


#1.
select * from instructor where salary>70000;

#2.
select iname, instructor.dept_name from instructor, department where department.dept_name = instructor.dept_name;

#3
#select 

#4
select iname, course_id from teaches, instructor where instructor.instructor_id = teaches.instructor_id;

#6

select * from instructor where salary > 90000 and salary < 100000;

#7

select course_ID from teaches where semester = 'Fall' and teaches.yearof = 2009;

#8
select course_ID from teaches where semester = 'Spring' and teaches.yearof = 2010;

#9
select distinct course_ID from teaches where semester = 'Fall' and teaches.yearof = 2010 or semester = 'Spring' and teaches.yearof = 2009 ;

#10
select distinct course.title from course, teaches where course.course_id = teaches.course_id and semester = 'Spring' and teaches.yearof = 2010 and semester - 'Fall' and teaches.yearof=2009;
 
#11
select course.title from teaches, course where course.course_id = teaches.course_id and teaches.semester = 'Fall' and teaches.yearof = 2009
and not teaches.semester = 'Spring' and teaches.yearof = 2010;

#13

select dept_name, avg(salary)from instructor group by dept_name;

#12
select dept_name, avg(salary)as Average from instructor where dept_name = 'Comp. Sci';

#14
select avg(salary) from instructor;

#15
select avg(student.tot_cred) from student.takes where student.ID=takes.ID group by takes.course_id having
count(student.ID);

#16

select course.title from teaches, course where course.course_id = teaches.course_id and teaches.yearof = 2009 and teaches.semester = 'Fall' and not teaches.yearof = 2010 and teaches.semester = 'Spring';

#17 

select distinct count(takes.ID) from takes, teaches where takes.course_id=teaches.course_id and teaches.ID=110011;

#18

Select course.title from course,teaches where course.course_id=teaches.course_id and teaches.year=2009 group by
t.course_id having count(teaches.year);

#19

delete from instructor where dept_name='Finance';

#20
delete from instructor where salary between 13000 and 15000;


#21
select * from course where course_id like 'CS%' and credits = 3;

#22
select distinct(student.student_id) from takes, instructor where iname = 'Einstein';

#23	
select max(salary) from instructor;

#24
select name from instructor group by name having max(salary);

#27
select max(count(distinct sec_id)) from takes where semester = 'Fall' and yearof = 2017;

#26
select max(count(distinct sec_id)) from takes where semester = 'Fall' and yearof = 2017;

#a.
update instructor
set salary = salary + salary*0.1;

#b. 