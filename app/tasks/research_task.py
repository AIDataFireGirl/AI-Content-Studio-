"""
Research Task for AI Content Studio

This task handles research workflows.
"""

from typing import Dict, Any, Optional, List
from .base_task import BaseTask
from app.agents.research_agent import ResearchAgent


class ResearchTask(BaseTask):
    """Task for research and information gathering"""
    
    def __init__(self, research_agent: ResearchAgent):
        """
        Initialize Research Task
        
        Args:
            research_agent: Agent for research
        """
        self.research_agent = research_agent
        
        super().__init__(
            name="Research",
            description="Conduct comprehensive research on topics for content creation",
            agent=research_agent,
            expected_output="Detailed research findings with facts, sources, and insights"
        )
    
    def research_topic(self, 
                      topic: str,
                      research_depth: str = "comprehensive",
                      content_type: str = "article",
                      target_audience: str = "general") -> Dict[str, Any]:
        """
        Research a topic comprehensively
        
        Args:
            topic: Topic to research
            research_depth: Level of research
            content_type: Type of content
            target_audience: Target audience
            
        Returns:
            Dict containing research results
        """
        research_result = self.research_agent.research_topic(
            topic=topic,
            research_depth=research_depth,
            content_type=content_type,
            target_audience=target_audience
        )
        
        return {
            "research_data": research_result,
            "research_timestamp": self._get_timestamp(),
            "status": "researched"
        }
    
    def fact_check_content(self, 
                          content: str,
                          topic: str) -> Dict[str, Any]:
        """
        Fact-check content for accuracy
        
        Args:
            content: Content to fact-check
            topic: Main topic of the content
            
        Returns:
            Dict containing fact-checking results
        """
        fact_check_result = self.research_agent.fact_check_content(
            content=content,
            topic=topic
        )
        
        return {
            "fact_check_data": fact_check_result,
            "content": content,
            "fact_check_timestamp": self._get_timestamp(),
            "status": "fact_checked"
        }
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat() 