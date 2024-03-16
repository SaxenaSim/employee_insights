import pytest
from input.employee_details import Employee

test_obj = Employee()


def test_avg_salary():
     mock_designation="Scientist"
     result= test_obj.avg_salary(mock_designation)
     assert result == 78118.24
