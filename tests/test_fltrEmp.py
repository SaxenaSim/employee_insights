import pytest , pandas as pd
from input.employee_details import Employee

test_obj = Employee()

def test_fltrEmp_len():
    mock_date="1990-07-21"
    mock_df=pd.DataFrame()
    mock_df=test_obj.filter_employee(mock_date)
    assert len(mock_df)>0
    
def test_fltrEmp_data():
    mock_date="1990-07-21"
    mock_df=pd.DataFrame()
    mock_df=test_obj.filter_employee(mock_date)
    assert 'EMP007' in mock_df['emp_code'].values