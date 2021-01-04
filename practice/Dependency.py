from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()

async def common_parameters(
    q: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    ):
    return {"q":q, "skip":skip, "limit":limit}

# 把所有會用到的參數放進function裡
@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons

# --------

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response= {}
    if commons.q:
        response.update({"q":commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items":items})
    return response


