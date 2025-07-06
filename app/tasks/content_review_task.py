"""
Content Review Task for AI Content Studio

This task handles content review, editing, and improvement workflows.
"""

from typing import Dict, Any, Optional, List
from .base_task import BaseTask
from app.agents.editor_agent import EditorAgent


class ContentReviewTask(BaseTask):
    """Task for reviewing and improving content"""
    
    def __init__(self, editor_agent: EditorAgent):
        """
        Initialize Content Review Task
        
        Args:
            editor_agent: Agent for editing and reviewing content
        """
        self.editor_agent = editor_agent
        
        super().__init__(
            name="Content Review",
            description="Review, edit, and improve content for quality, clarity, and engagement",
            agent=editor_agent,
            expected_output="Improved content with detailed review feedback and suggestions"
        )
    
    def review_content(self, 
                      content: str,
                      content_type: str = "article",
                      target_audience: str = "general",
                      review_focus: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Review content comprehensively
        
        Args:
            content: Content to review
            content_type: Type of content
            target_audience: Target audience
            review_focus: Specific areas to focus on
            
        Returns:
            Dict containing review results
        """
        review_result = self.editor_agent.review_content(
            content=content,
            content_type=content_type,
            target_audience=target_audience,
            review_focus=review_focus
        )
        
        return {
            "review_data": review_result,
            "content_original": content,
            "review_timestamp": self._get_timestamp(),
            "status": "reviewed"
        }
    
    def improve_content(self, 
                       content: str,
                       improvement_areas: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Improve content quality
        
        Args:
            content: Content to improve
            improvement_areas: Specific areas to improve
            
        Returns:
            Dict containing improved content
        """
        improved_content = self.editor_agent.improve_content(
            content=content,
            improvement_areas=improvement_areas
        )
        
        return {
            "original_content": content,
            "improved_content": improved_content,
            "improvement_timestamp": self._get_timestamp(),
            "status": "improved"
        }
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat() 