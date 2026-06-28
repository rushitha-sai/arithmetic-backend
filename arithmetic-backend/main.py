from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Arithmetic Backend API")

# Allow the frontend (running on a different port/origin) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Arithmetic backend is running"}


@app.get("/add/{a}/{b}")
def add_numbers(a: float, b: float):
    """
    Add two numbers passed as path parameters.
    Example: GET /add/10/20  ->  {"a": 10, "b": 20, "result": 30}
    """
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }
