from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.registration import router as registration_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Narvixia API Starting...")
    yield
    print("🛑 Narvixia API Stopped")


app = FastAPI(
    title="Narvixia API",
    description="AI-Powered Document Intelligence Platform",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)


@app.get("/", tags=["System"])
def home():
    return {
        "application": "Narvixia",
        "message": "Welcome to Narvixia API",
        "version": app.version,
    }


@app.get("/health", tags=["System"])
def health():
    return {
        "status": "healthy",
        "application": "Narvixia",
        "version": app.version,
    }


app.include_router(registration_router)