from fastapi import FastAPI
app = FastAPI()
@app.get("/")       # http://localhost:8080/
def root(): return {"message": "hello from ubuntu-dev"}
@app.get("/healthz")
def health(): return {"status": "ok"}
