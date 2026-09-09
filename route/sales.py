from fastapi import APIRouter

newr = APIRouter()

@newr.get("/sales")
def get_sales():
    return {
        "message": "sales list"
    }