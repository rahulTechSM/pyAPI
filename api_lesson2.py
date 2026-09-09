from fastapi import FastAPI
from pydantic import BaseModel,Field
from datetime import date
from typing import Literal

employees= [
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




class EmployeeStruc(BaseModel):
    name:str=Field(
        min_length=2,
        max_length=20
    )
    salary:float
    emp_id:int=Field(
        gt=10002,
        lt=100020
    )
    joining_date:date

    department:Literal[
        "Technical",
        "HR",
        "Sales"
    ]

    phone_number:int|None=None

obj = FastAPI()

@obj.get("/employee")
def get_emp():
    return {
        "message":employees
    }

@obj.get("/employee/{emp_id}")
def get_emp(emp_id:int):

    for empV in employees:
        if empV["id"] == emp_id:
            return {
                "message":empV
            }
        else:
            return{
                "message":"wrong emp id"
            }
        

@obj.post("/employee")
def create_employee(emp:EmployeeStruc):
    return {
        "message":"sucessfull",
        "employee":emp
    }