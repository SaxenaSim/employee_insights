import pytest
from input.employee_details import Employee
import os

test_obj = Employee()


def test_save_data_file():
    mock_data="This is my sample data"
    file=test_obj.save_data_to_file(mock_data)
    assert os.path.exists(file)