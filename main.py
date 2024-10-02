from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello, World!'}


@app.get('/items')
async def read_items():
    return [{'item_id': i} for i in range(1, 11)]


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app',
                host='localhost',
                port=8000,
                reload=True)
