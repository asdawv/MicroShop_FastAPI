from fastapi import FastAPI

from views import users

app = FastAPI()

# Добавление обработчиков маршрутов
app.include_router(users.router)  # /users...

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app',
                host='localhost',
                port=8000,
                reload=True)
