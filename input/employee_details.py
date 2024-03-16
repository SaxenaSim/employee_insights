import yaml,mysql.connector,logging,logging.config
from datetime import datetime
import pandas as pd
import os


class Employee:
    def __init__(self):
        # root_dir = os.path.abspath(os.sep)

        # config_dir = os.path.join(root_dir, 'configuration')

        # file_name = 'config.yaml'
        
        # main_script_dir = os.path.dirname(os.path.abspath(__file__))

        # config_file_path = os.path.join(main_script_dir, '..', 'config.yaml')

        # config_logging_path = os.path.join(main_script_dir,"..","logging_config.yaml")
        #config_file_path = os.path.join(config_dir, file_name)

        
        with open("configuration/config.yaml", 'r') as config_file:
            self.db_config = yaml.safe_load(config_file)
        self.conn = mysql.connector.MySQLConnection(user=self.db_config['database']['user'],password=self.db_config['database']['password'],host=self.db_config['database']['host'],port=self.db_config['database']['port'],database=self.db_config['database']['database']
)
        with open("configuration/logging_config.yaml", 'r') as f:
            self.logging_config = yaml.safe_load(f)
            logging.config.dictConfig(self.logging_config)
            
        self.logger = logging.getLogger('file_size_logger')
        self.employee_df=pd.DataFrame()
        self.create_dataframe()

        
    def create_dataframe(self):
        self.employee_df = pd.read_sql_query("SELECT * FROM employee",self.conn)
    
    def filter_employee(self,input_date):
        try:
            self.logger.info("::Entering into filter_employee method::")
            self.employee_df['date_of_joining'] = pd.to_datetime(self.employee_df['date_of_joining'])
            filtered_df = self.employee_df[self.employee_df['date_of_joining'] > input_date]
            self.logger.info("::Filtered dataframe::")
            self.logger.debug(filtered_df)
            return filtered_df
        except Exception as e:
            self.logger.info("::Entering into Filter exception::")
            self.logger.error(e)
            return None
        
    def save_data_to_file(self,employees):
        try:
            self.logger.info("::Entering into save_data_to_file method::")
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            filename=f"output/filtered_employees_{timestamp}.txt"
            self.logger.debug(filename)
            self.logger.debug(timestamp)
            with open(filename, 'w') as f:
                f.write(employees.to_string(index=False))
            return filename
        except Exception as e:
            self.logger.info("::Entering into save_data_to_file exception::")
            self.logger.error(e)
            return False
            
    def avg_salary(self,designation):
        try:
            self.logger.info(":: ENtering into avg_salary method::")
            filtered_df = self.employee_df[self.employee_df['designation'] == designation]
            self.logger.info("::Filtered df::")
            self.logger.debug(filtered_df)
            average_salary = filtered_df['salary'].mean()
            self.logger.info("::average salary::")
            self.logger.debug(average_salary)
            return average_salary
        except Exception as e:
            self.logger.info("::Entering into average_salary exception")
            self.logger.error(e)
            return None
            
    def save_avg_to_file(self,position,salary):
        try:
            self.logger.info("::Entering into save_avg_to_file method::")
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            filename=f"output/avg_salary.txt"
            self.logger.debug(filename)
            self.logger.debug(timestamp)
            with open(filename, 'a') as f:
                f.write(f"{timestamp}: Average Salary for the {position} is {salary:.2f}\n")
            return filename
        except Exception as e:
            self.logger.info("::Entering into save_avg_to_file exception::")
            self.logger.error(e)
            return False
        
        
    
if __name__=="__main__":
    
    input_date = input()
        
    obj = Employee()
    
    employees=obj.filter_employee(input_date)
    obj.save_data_to_file(employees)
    
    designation = input()
    
    salary=obj.avg_salary(designation)
    obj.save_avg_to_file(designation,salary)
    
    
        