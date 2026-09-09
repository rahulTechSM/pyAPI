from fastapi import APIRouter

router = APIRouter()

@router.get("/employees")
def get_employees():
    return {
        "message": "Employee list"
    }
