from datetime import date
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr


app = FastAPI()


class EmployeeCreate(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr

    department: Literal[
        "Technical",
        "HR",
        "Sales",
        "Operations"
    ]

    salary: int = Field(
        ge=10000,
        le=500000
    )

    joining_date: date

    phone: str | None = None


@app.post("/employees")
def create_employee(
    emp: EmployeeCreate
):

    return {
        "message": "Employee validated successfully",
        "employee": emp
    }