from fastapi import FastAPI
from pydantic import BaseModel

ramesh= FastAPI();

@ramesh.get("/")

def home():
    return{
        "message" : "Fast API is working"
    }

@ramesh.get("/employees")

def employees():
     return {
        "employees": [
            {
                "id": 1,
                "name": "Rahul",
                "department": "Technical",
                "salary": 30000
            },
            {
                "id": 2,
                "name": "Ravi",
                "department": "Technical",
                "salary": 25000
            },
            {
                "id": 3,
                "name": "Neha",
                "department": "HR",
                "salary": 22000
            }
        ]
    }
@ramesh.get("/emp/{emp_id}")
def emp(emp_id: int):
    return emp_id
employees=[]
class Employee(BaseModel):
    name:str
    department:str
    salary:int


@ramesh.post("/createEmployee")    
def createEmployee(emp: Employee):
    new_employee = {
        "id":len(employees)+1,
        "name":emp.name,
        "department":emp.department,
        "salary":emp.salary
        
    }
    employees.append(new_employee)
    return new_employee





    
