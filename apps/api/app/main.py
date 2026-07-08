from fastapi import FastAPI

app = FastAPI(
    title="Registration AI API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "Registration AI",
        "version": "0.1.0",
    }