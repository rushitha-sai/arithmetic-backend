# arithmetic-backend

FastAPI backend that adds two numbers.

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

- Health check: http://127.0.0.1:8000/
- Swagger docs: http://127.0.0.1:8000/docs
- Add endpoint: `GET /add/{a}/{b}` → e.g. http://127.0.0.1:8000/add/10/20

## Push to GitHub

```bash
git init
git add .
git commit -m "Initial FastAPI backend"
git branch -M main
git remote add origin https://github.com/<your-username>/arithmetic-backend.git
git push -u origin main
```
