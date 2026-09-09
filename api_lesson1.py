from fastapi import FastAPI
from pydantic import BaseModel

class EmployeeStruc(BaseModel):
    name:str
    salary:float
    emp_id:int

obj = FastAPI()

@obj.get("/employee")
def get_emp():
    return {
        "message":"yes returing emp"
    }

@obj.post("/employee")
def create_employee(emp:EmployeeStruc):
    return {
        "message":"sucessfull",
        "employee":emp
    }