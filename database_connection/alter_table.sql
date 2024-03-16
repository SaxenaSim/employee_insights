ALTER TABLE employee
ADD FOREIGN KEY (supervisor) REFERENCES employee(emp_code);
