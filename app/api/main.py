"""
FastAPI entrypoint for AI Content Studio
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from . import content

app = FastAPI(
    title="AI Content Studio API",
    description="API for modular, secure, and extensible AI content workflows.",
    version="1.0.0"
)

# CORS middleware (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}

# Import and include routers (to be created)
# from . import content, review, seo, research, creative
app.include_router(content.router)
# app.include_router(review.router)
# app.include_router(seo.router)
# app.include_router(research.router)
# app.include_router(creative.router) 