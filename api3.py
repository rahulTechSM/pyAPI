from fastapi import FastAPI,Field

from routes.employee import router as employee_router

from route.sales import newr as sales


from Url.product import sanjeetP as pro

from Url.category import sanjeetC as cate

obj = FastAPI()


obj.include_router(employee_router)

obj.include_router(sales)


obj.include_router(pro)


obj.include_router(cate)

