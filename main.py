from fastapi import FastAPI
from app.routers import posts

app = FastAPI()
app.include_router(posts.router)

@app.get("/")
def index():
    return {"msg": "It works!"}

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="127.0.0.1", port=3003, reload=True)