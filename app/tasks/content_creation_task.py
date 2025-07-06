"""
Content Creation Task for AI Content Studio

This task handles the main content creation workflow, coordinating between
different agents to create high-quality content.
"""

from typing import Dict, Any, Optional, List
from .base_task import BaseTask
from app.agents.writer_agent import WriterAgent
from app.agents.research_agent import ResearchAgent


class ContentCreationTask(BaseTask):
    """Task for creating comprehensive content"""
    
    def __init__(self, writer_agent: WriterAgent, research_agent: ResearchAgent):
        """
        Initialize Content Creation Task
        
        Args:
            writer_agent: Agent for writing content
            research_agent: Agent for research
        """
        self.writer_agent = writer_agent
        self.research_agent = research_agent
        
        # Use writer agent as primary agent for this task
        super().__init__(
            name="Content Creation",
            description="Create comprehensive, well-researched content based on given topic and requirements",
            agent=writer_agent,
            expected_output="Complete content piece with proper structure, engaging writing, and factual accuracy"
        )
    
    def create_content(self, 
                      topic: str,
                      content_type: str = "article",
                      target_audience: str = "general",
                      word_count: int = 1000,
                      tone: str = "professional",
                      keywords: Optional[List[str]] = None,
                      research_depth: str = "comprehensive") -> Dict[str, Any]:
        """
        Create comprehensive content with research and writing
        
        Args:
            topic: Main topic for content
            content_type: Type of content to create
            target_audience: Target audience
            word_count: Target word count
            tone: Writing tone
            keywords: Target keywords
            research_depth: Depth of research required
            
        Returns:
            Dict containing created content and metadata
        """
        try:
            self.logger.info(f"Starting content creation for topic: {topic}")
            
            # Step 1: Research the topic
            research_result = self._conduct_research(topic, content_type, target_audience, research_depth)
            
            # Step 2: Create content draft
            content_result = self._create_draft(topic, content_type, target_audience, word_count, tone, keywords, research_result)
            
            # Step 3: Compile final result
            final_result = {
                "topic": topic,
                "content_type": content_type,
                "target_audience": target_audience,
                "word_count": word_count,
                "tone": tone,
                "keywords": keywords,
                "research_data": research_result,
                "content": content_result,
                "creation_timestamp": self._get_timestamp(),
                "status": "completed"
            }
            
            self.logger.info(f"Content creation completed successfully")
            return final_result
            
        except Exception as e:
            self.logger.error(f"Error in content creation: {str(e)}")
            raise
    
    def _conduct_research(self, 
                         topic: str,
                         content_type: str,
                         target_audience: str,
                         research_depth: str) -> Dict[str, Any]:
        """
        Conduct research for the topic
        
        Args:
            topic: Topic to research
            content_type: Type of content
            target_audience: Target audience
            research_depth: Depth of research
            
        Returns:
            Dict containing research results
        """
        self.logger.info(f"Conducting research for topic: {topic}")
        
        research_result = self.research_agent.research_topic(
            topic=topic,
            research_depth=research_depth,
            content_type=content_type,
            target_audience=target_audience
        )
        
        return research_result
    
    def _create_draft(self, 
                     topic: str,
                     content_type: str,
                     target_audience: str,
                     word_count: int,
                     tone: str,
                     keywords: Optional[List[str]],
                     research_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create content draft using research data
        
        Args:
            topic: Topic for content
            content_type: Type of content
            target_audience: Target audience
            word_count: Target word count
            tone: Writing tone
            keywords: Target keywords
            research_data: Research data to incorporate
            
        Returns:
            Dict containing content draft
        """
        self.logger.info(f"Creating content draft for topic: {topic}")
        
        # Prepare additional requirements based on research
        additional_requirements = self._prepare_research_requirements(research_data)
        
        content_draft = self.writer_agent.create_content_draft(
            topic=topic,
            content_type=content_type,
            target_audience=target_audience,
            word_count=word_count,
            tone=tone,
            keywords=keywords,
            additional_requirements=additional_requirements
        )
        
        return {
            "draft_content": content_draft,
            "research_incorporated": True,
            "word_count_actual": len(content_draft.split()),
            "keywords_used": keywords or []
        }
    
    def _prepare_research_requirements(self, research_data: Dict[str, Any]) -> str:
        """
        Prepare research requirements for content creation
        
        Args:
            research_data: Research data
            
        Returns:
            str: Formatted research requirements
        """
        requirements = []
        
        if "key_facts" in research_data:
            requirements.append(f"Key Facts: {', '.join(research_data['key_facts'][:5])}")
        
        if "sources" in research_data:
            requirements.append(f"Credible Sources: {', '.join(research_data['sources'][:3])}")
        
        if "insights" in research_data:
            requirements.append(f"Key Insights: {', '.join(research_data['insights'][:3])}")
        
        return "\n".join(requirements) if requirements else ""
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """
        Validate input for content creation task
        
        Args:
            input_data: Data to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        required_fields = ["topic"]
        
        if not isinstance(input_data, dict):
            return False
        
        for field in required_fields:
            if field not in input_data or not input_data[field]:
                return False
        
        return True
    
    def get_task_info(self) -> Dict[str, Any]:
        """
        Get detailed task information
        
        Returns:
            Dict containing task details
        """
        base_info = super().get_task_info()
        base_info.update({
            "agents_involved": [
                self.writer_agent.get_agent_info(),
                self.research_agent.get_agent_info()
            ],
            "workflow_steps": [
                "Research topic thoroughly",
                "Gather key facts and insights",
                "Create comprehensive content draft",
                "Incorporate research findings",
                "Ensure factual accuracy"
            ]
        })
        return base_info 