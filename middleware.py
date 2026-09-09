from fastapi import FastAPI, Request

obj = FastAPI()


@obj.middleware("http")
async def my_middleware(
    request: Request,
    call_next
):

    print("Request received")

    response = await call_next(request)

    print("Response generated")

    return response