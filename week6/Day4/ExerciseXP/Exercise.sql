--1.)Write a query to display the names (first_name, last_name) using an alias name “First Name”, “Last Name” from the employee table.
select first_name as "First Name",last_name as "Last Name" from employees;
--2.)Write a query to get unique departments ID from the employee table (ie. without duplicates).
select DISTINCT department_id,first_name as "First Name",last_name as "Last Name" from employees;
--3.)Write a query to get the details of all employees from the employee table, do so in descending order by first name.
select * from employees order by first_name desc;
--4.)Write a query to get the names (first_name, last_name), salary and 15% of salary as PF (ie. alias) for all the employees.
select first_name,last_name,salary,(salary*0.15) AS PF from employees;
--5.)Write a query to get the employee IDs, names (first_name, last_name) and salary in ascending order according to their salary.
select employee_id,first_name as "First Name",last_name as "Last Name",salary from employees order by salary asc;
--6.)Write a query to get the total sum of all salaries paid to the employees.
select sum(salary) from employees;
--7.)Write a query to get the maximum and minimum salaries paid to the employees.
select max(salary),min(salary) from employees;
--8.)Write a query to get the average salary paid to the employees.
SELECT AVG(salary),COUNT(*) AS "Avg Salary" FROM employees;
--9.)Write a query to get the number of employees working in the company.
--10.)Write a query to get all the first names from the employees table in upper case.
select UPPER(first_name) as "First Name",last_name as "Last Name" from employees;
--11.)Write a query to get the first three characters of each first name of all the employees in the employees table.
select SUBSTRING(first_name,1,3),last_name from employees;
--12.)Write a query to get the full names of all the employees in the employees table. You have to include the first name and last name.
select concat(first_name,' ',last_name) as full_name from employees;
--13.)Write a query to get the first name, last name and the length of the full name of all the employees from the employees table.
select concat(first_name,' ',last_name) as full_name,length(concat(first_name,' ',last_name)) as length_fullName from employees;
--14.)Write a query to check whether the first_name column of the employees table contains any numbers.
select * from employees where first_name SIMILAR to '%0|1|2|3|4|5|6|7|8|9%';
--15.)Write a query to select the first ten records from a table.
select * from employees LIMIT 10;


--Restricting And Sorting

--1.)Write a query to display the first_name, last_name and salary of all employees whose salary is between $10,000 and $15,000.
select first_name,last_name,salary from employees where salary between 10000 and 15000;
--2.)Write a query to display the first_name, last_name and hire date of all employees who were hired in 1987.
select first_name,last_name,hire_date from employees where TO_CHAR(hire_date,'YYY')  LIKE '%87'; 
--3.)Write a query to get the all employees whose first_name has both the letters ‘c’ and ‘e’.
select first_name,last_name from employees where first_name like '%c%' and first_name like '%e%';
--4.)Write a query to display the last_name, job, and salary of all the employees who don’t work as Programmers or Shipping Clerks, and who don’t receive a salary equal to $4,500, $10,000, or $15,000.
select emp.last_name,job.job_title,emp.salary from employees emp join jobs job on emp.job_id=job.job_id
where (job.job_title!='Programmer' or job.job_title!='Shipping Clerk')
and
(emp.salary!=4500 or emp.salary!=10000 or emp.salary!=15000);
--5.)Write a query to display the last names of all employees whose last name contains exactly six characters.
select last_name from employees where length(last_name)=6;
--6.)Write a query to display the last name of all employees who have the letter ‘e’ as the third character in the name.
select last_name from employees where last_name like '__e%';
--7.)Write a query to display the jobs title appearing in the employees table.
select e.job_id,j.job_title
from employees e,jobs j
where j.job_id=e.job_id;
--8.)Write a query to select all information of employees whose last name is either ‘JONES’ or ‘BLAKE’ or ‘SCOTT’ or ‘KING’ or ‘FORD’.
SELECT * 
FROM employees 
WHERE last_name IN ('BLAKE', 'SCOTT', 'KING', 'FORD');

