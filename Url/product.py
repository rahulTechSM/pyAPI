from fastapi import APIRouter

sanjeetP = APIRouter()


@sanjeetP.get("/product")
def get_product():
    return{
        "message":"product"
    }
