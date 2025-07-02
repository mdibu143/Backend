from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow React frontend to call the API (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React default dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/datas")
def get_data():
    return {"message": "Hello from FastAPI backend!"}

@app.get("/")
def health():
    return {"message": "App is Ok"}

@app.get("/api/show")
def health():
    return {"message": "I am going to provide show"}
