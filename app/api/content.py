"""
Content creation endpoints for AI Content Studio
"""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from app.agents.writer_agent import WriterAgent
from app.agents.research_agent import ResearchAgent
from app.tasks.content_creation_task import ContentCreationTask

# Security dependency (simple API key for demo)
from fastapi.security.api_key import APIKeyHeader
from app.config import settings

API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != settings.secret_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")
    return api_key

# Request/response models
class ContentRequest(BaseModel):
    topic: str
    content_type: str = "article"
    target_audience: str = "general"
    word_count: int = 1000
    tone: str = "professional"
    keywords: Optional[List[str]] = None
    research_depth: str = "comprehensive"

class ContentResponse(BaseModel):
    topic: str
    content_type: str
    target_audience: str
    word_count: int
    tone: str
    keywords: Optional[List[str]]
    research_data: dict
    content: dict
    creation_timestamp: str
    status: str

router = APIRouter(prefix="/content", tags=["Content"])

# Instantiate agents and task (in production, use dependency injection or a factory)
writer_agent = WriterAgent()
research_agent = ResearchAgent()
content_task = ContentCreationTask(writer_agent, research_agent)

@router.post("/create", response_model=ContentResponse, dependencies=[Depends(get_api_key)])
def create_content(request: ContentRequest):
    """
    Create comprehensive content with research and writing
    """
    if not content_task.validate_input(request.dict()):
        raise HTTPException(status_code=400, detail="Invalid input data")
    result = content_task.create_content(**request.dict())
    return result 