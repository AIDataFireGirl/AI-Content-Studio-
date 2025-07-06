"""
Creative Ideation Task for AI Content Studio

This task handles creative ideation workflows.
"""

from typing import Dict, Any, Optional, List
from .base_task import BaseTask
from app.agents.creative_agent import CreativeAgent


class CreativeIdeationTask(BaseTask):
    """Task for creative ideation and brainstorming"""
    
    def __init__(self, creative_agent: CreativeAgent):
        """
        Initialize Creative Ideation Task
        
        Args:
            creative_agent: Agent for creative ideation
        """
        self.creative_agent = creative_agent
        
        super().__init__(
            name="Creative Ideation",
            description="Generate creative content ideas and innovative approaches",
            agent=creative_agent,
            expected_output="Creative content ideas with engagement potential and implementation strategies"
        )
    
    def generate_content_ideas(self, 
                              topic: str,
                              content_type: str = "article",
                              target_audience: str = "general",
                              idea_count: int = 10,
                              creativity_level: str = "high") -> Dict[str, Any]:
        """
        Generate creative content ideas for a topic
        
        Args:
            topic: Main topic for content ideas
            content_type: Type of content to generate ideas for
            target_audience: Target audience
            idea_count: Number of ideas to generate
            creativity_level: Level of creativity
            
        Returns:
            Dict containing creative content ideas
        """
        ideas_result = self.creative_agent.generate_content_ideas(
            topic=topic,
            content_type=content_type,
            target_audience=target_audience,
            idea_count=idea_count,
            creativity_level=creativity_level
        )
        
        return {
            "ideas_data": ideas_result,
            "ideation_timestamp": self._get_timestamp(),
            "status": "ideas_generated"
        }
    
    def brainstorm_headlines(self, 
                           topic: str,
                           content_type: str = "article",
                           headline_count: int = 15,
                           headline_style: str = "clickbait") -> Dict[str, Any]:
        """
        Brainstorm creative headlines for content
        
        Args:
            topic: Topic for headlines
            content_type: Type of content
            headline_count: Number of headlines to generate
            headline_style: Style of headlines
            
        Returns:
            Dict containing headline ideas
        """
        headlines_result = self.creative_agent.brainstorm_headlines(
            topic=topic,
            content_type=content_type,
            headline_count=headline_count,
            headline_style=headline_style
        )
        
        return {
            "headlines_data": headlines_result,
            "headlines_timestamp": self._get_timestamp(),
            "status": "headlines_generated"
        }
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat() 