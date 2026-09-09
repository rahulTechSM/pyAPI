from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


employees = [
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


class Employee(BaseModel):
    name: str
    department: str
    salary: int


# GET all employees
@app.get("/employees")
def get_employees():

    return employees


# GET single employee
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    for employee in employees:

        if employee["id"] == employee_id:
            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# CREATE employee
@app.post(
    "/employees",
    status_code=201
)
def create_employee(employee: Employee):

    new_id = max(
        [emp["id"] for emp in employees],
        default=0
    ) + 1

    new_employee = {
        "id": new_id,
        "name": employee.name,
        "department": employee.department,
        "salary": employee.salary
    }

    employees.append(new_employee)

    return new_employee


# UPDATE employee
@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    employee: Employee
):

    for emp in employees:

        if emp["id"] == employee_id:

            emp["name"] = employee.name
            emp["department"] = employee.department
            emp["salary"] = employee.salary

            return emp

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# DELETE employee
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    for employee in employees:

        if employee["id"] == employee_id:

            employees.remove(employee)

            return {
                "message": "Employee deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )