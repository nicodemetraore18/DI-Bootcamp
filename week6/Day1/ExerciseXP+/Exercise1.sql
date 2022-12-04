CREATE TABLE students(
 student_id SERIAL PRIMARY KEY,
 last_name VARCHAR (100) NOT NULL,	
 first_name VARCHAR (50) NOT NULL,
 birth_date DATE NOT NULL
);
INSERT INTO students(last_name,first_name,birth_date)
VALUES('Marc','Benichou' ,'02/11/1998'),
('Yoan','Cohen' ,'03/12/2010'),
('Lea','Benichou' ,'27/07/1987'),
('Amelia','Dux' ,'07/04/1996'),
('David','Grez' ,'14/06/2003'),
('Omer','Simpson' ,'03/10/1980'),
('Nicodeme','Traore' ,'17/11/2003');
/*
Fetch all of the data from the table.
Fetch all of the students first_names and last_names.
For the following questions, only fetch the first_names and last_names of the students.
Fetch the student which id is equal to 2.
Fetch the student whose last_name is Benichou AND first_name is Marc.
Fetch the students whose last_names are Benichou OR first_names are Marc.
Fetch the students whose first_names contain the letter a.
Fetch the students whose first_names start with the letter a.
Fetch the students whose first_names end with the letter a.
Fetch the students whose second to last letter of their first_names are a (Example: Leah).
Fetch the students whose id’s are equal to 1 AND 3 .
Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
*/
select * from students;
select last_name,first_name from students;
select last_name,first_name from students where student_id=1;
select last_name,first_name from students where last_name='Marc' and first_name='Benichou';
select last_name,first_name from students where last_name='Marc' or first_name='Benichou';
select last_name,first_name from students where last_name ilike '%a%';
select last_name,first_name from students where last_name ilike '%a';
select last_name,first_name from students where last_name ilike 'a%';
select last_name,first_name from students where student_id=1 and student_id=3;

select * from students where birth_date>='1/01/2000';

