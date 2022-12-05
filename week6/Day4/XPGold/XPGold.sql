--Part1
--Update Statement
--1.)Write a SQL statement to change the following details belonging all employes who’s department_id is 110:
	--email column should be: ‘not available’
	--commission_pct column should be: 0.10
update employees
SET email='not available'
where department_id=110;

--2.)Write a SQL statement which will change the email column of all employees to ‘available’ whom work in the ‘Accounting’ department.
update employees
set email='vailable' from departments where employees.department_id=departments.department_id and	departments.department_name='Accounting';
--3.)Write a SQL statement to change the salary of the employee whose ID is 105. If the existing salary is less than 5000, change it to 8000.
update employees
set salary=8000 
where employee_id=105 and salary<5000;


--Aggregate Functions
--1.)Write a query to find the number of jobs available in the employees table.
select COUNT(DISTINCT job_id) from employees;
--2.)Write a query to get the number of employees working in each post.
select job_title,count(employee_id) from employees,jobs where employees.job_id=jobs.job_id group by job_title;
--3.)Write a query to get the difference between the highest and lowest salaries.
select max(salary)-min(salary) from employees;
--4.)Write a query to find a manager ID and the salary of the lowest-paid employee under that manager.
select manager_id,min(salary)
from employees
where manager_id is not NULL
group by manager_id
order by min(salary) desc;
--5.)Write a query to get the average salary for each post excluding programmer.
select job.job_title,avg(emp.salary)
from employees emp join jobs job
on emp.job_id=job.job_id
where job.job_title!='Programmer'
group by job.job_title;
--6.)Write a query to get the average salary for all departments that employ more than 10 employees.
select dept.department_name,avg(emp.salary),count(emp.employee_id) as Number_employees
from employees emp join departments dept
on emp.department_id=dept.department_id
group by dept.department_name
having count(emp.employee_id)>10;

--Alter Table Statement

--1.)Write a SQL statement to change the name of the column “state_province” to “state” in the locations table, keeping the same data type and size.
Alter table locations
RENAME COLUMN state_province TO state;
--2.)Write a SQL statement to add a primary key to the “location_id” column in the locations table.
--ALTER TABLE locations 
--add primary key(location_id);

--Part2

--Create Tables

--1.)Write a SQL statement to create a simple table “new_countries” including columns country_id and country_name.
	--make sure that no duplicate data is added to the country_id column (which data type should you use for the column country_id ?)
	--make sure that no countries except Italy, India and China will be entered in the table.

CREATE TABLE IF NOT EXISTS new_countries(
	country_id integer NOT NULL,
	country_name varchar(40) NOT NULL,
	UNIQUE(country_id),
	check(country_name in ('Italy', 'India','China'))
);

--2.)Write a SQL statement to create a duplicate copy of the “new_countries” table including the structure and the data of the “new_countries” table.

CREATE TABLE IF NOT EXISTS dup_countries as 
select * from new_countries;

--3.)Write a SQL statement to create a table named “new_jobs” including columns job_id, job_title, min_salary, max_salary
	--make sure that the max_salary column won’t exceed 25000.
	--make sure that job_title, min_salary and max_salary have the following default values:
	--job_title is blank
	--min_salary is 8000
	--max_salary is NULL.

create table new_jobs(
	job_id VARCHAR(10) NOT NULL UNIQUE, 
	job_title varchar(35) DEFAULT ' ',
	min_salary decimal(6,0) DEFAULT 8000,
	max_salary decimal(6,0) DEFAULT NULL,
	check(max_salary < 25000)
);

--4.)Write an SQL statement to create a table called “new_employees” the table should include the following columns: employee_id, first_name, last_name, email, phone_number hire_date, job_id and salary.
     --make sure that, the employee_id column does not contain any duplicate value at the time of insertion,
     --make sure that the foreign key column job_id, references the column job_id in the “new_jobs” table.

create table new_employees(
	employee_id varchar(5) unique,
	first_name varchar(50),
	last_name varchar(50),
	email varchar(30),
	phone_number varchar(10) default null,
	hire_date date not null,
	job_id varchar(10) NOT NULL,
	salary decimal(6,0),
	foreign key(job_id) references new_jobs(job_id)
	
);

