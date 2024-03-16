from setuptools import setup , find_packages

setup(
    name='packageSensitiveInfo',
    version="1.0.0",
    author='Simran',
    author_email='simran.saxena@dataverze.ai',
    description='This package is used to get the employee details like employees whose date_of_joining is greater than input date_of_joining and average salary of empolyees of a particular designation.',
    packages=find_packages(),
    #namespace_packages=['packageSensitiveInfo'],
    #package_dir={'packageSensitiveInfo': 'src'},
    install_requires=[
        'black==24.3.0',
        'pytest==8.0.2',
        'setuptools==69.1.1',
        'wheel==0.42.0',
        'twine==5.0.0',
        'pre-commit==3.6.2'
    ],
    package_data={'employee_insights': ['logs/*', 'tests/*.py']},
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    
)