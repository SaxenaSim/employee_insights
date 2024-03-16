import pytest
from input.employee_details import Employee
import os

test_obj = Employee()

def test_save_avg_file():
    mock_designation="designation"
    mock_salary="salary"
    file=test_obj.save_avg_to_file(mock_designation,mock_salary)
    assert os.path.exists(file)