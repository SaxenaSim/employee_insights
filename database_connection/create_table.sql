CREATE TABLE employee(
emp_code varchar(10) primary key NOT NULL,
first_name varchar(25) NOT NULL,
last_name varchar(25) NOT NULL,
designation varchar(50) NOT NULL,
date_of_joining datetime NOT NULL,
salary float NOT NULL,
supervisor varchar(10) NOT NULL
);