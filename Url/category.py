from fastapi import APIRouter

sanjeetC = APIRouter()


@sanjeetC.get("/category")
def get_category():
    return{
        "message":"category"
    }
