"""
Writer Agent for AI Content Studio

This agent specializes in creating initial content drafts based on given topics,
keywords, and requirements. It focuses on generating engaging, well-structured content.
"""

from typing import Dict, Any, Optional, List
from .base_agent import BaseAgent


class WriterAgent(BaseAgent):
    """Agent specialized in creating initial content drafts"""
    
    def __init__(self, verbose: bool = True):
        """
        Initialize Writer Agent
        
        Args:
            verbose: Whether to enable verbose logging
        """
        super().__init__(
            name="Content Writer",
            role="Expert content writer with years of experience in creating engaging, informative, and well-structured articles, blog posts, and marketing copy. Specializes in adapting writing style to match target audience and brand voice.",
            goal="Create high-quality, engaging content that meets the specified requirements, target audience needs, and maintains consistent tone and style throughout.",
            verbose=verbose
        )
    
    def create_content_draft(self, 
                           topic: str, 
                           content_type: str = "article",
                           target_audience: str = "general",
                           word_count: int = 1000,
                           tone: str = "professional",
                           keywords: Optional[List[str]] = None,
                           additional_requirements: Optional[str] = None) -> str:
        """
        Create a content draft based on given parameters
        
        Args:
            topic: Main topic or subject of the content
            content_type: Type of content (article, blog, social media, etc.)
            target_audience: Target audience for the content
            word_count: Approximate word count for the content
            tone: Writing tone (professional, casual, friendly, etc.)
            keywords: List of keywords to include naturally
            additional_requirements: Any additional requirements or guidelines
            
        Returns:
            str: Generated content draft
        """
        # Validate inputs
        if not self.validate_input(topic):
            raise ValueError("Topic cannot be empty")
        
        # Prepare task description
        task_description = f"""
        Create a {content_type} about "{topic}" with the following specifications:
        
        - Target Audience: {target_audience}
        - Word Count: Approximately {word_count} words
        - Tone: {tone}
        - Content Type: {content_type}
        """
        
        if keywords:
            task_description += f"\n- Keywords to include naturally: {', '.join(keywords)}"
        
        if additional_requirements:
            task_description += f"\n- Additional Requirements: {additional_requirements}"
        
        task_description += """
        
        Please ensure the content is:
        1. Well-structured with clear headings and subheadings
        2. Engaging and informative
        3. Optimized for the target audience
        4. Free of grammatical errors
        5. Original and plagiarism-free
        """
        
        # Execute the task
        result = self.execute_task(task_description)
        return self.postprocess_output(result)
    
    def expand_section(self, 
                      section_content: str, 
                      section_title: str,
                      target_length: int = 300) -> str:
        """
        Expand a specific section of content
        
        Args:
            section_content: Current content of the section
            section_title: Title of the section
            target_length: Target word count for the expanded section
            
        Returns:
            str: Expanded section content
        """
        task_description = f"""
        Expand the following section to approximately {target_length} words while maintaining quality and relevance:
        
        Section Title: {section_title}
        Current Content: {section_content}
        
        Please:
        1. Add more detail and examples
        2. Maintain the original tone and style
        3. Ensure smooth flow and transitions
        4. Keep the content relevant and valuable
        """
        
        result = self.execute_task(task_description)
        return self.postprocess_output(result)
    
    def rewrite_content(self, 
                       original_content: str,
                       new_tone: Optional[str] = None,
                       new_audience: Optional[str] = None,
                       new_length: Optional[int] = None) -> str:
        """
        Rewrite content with different parameters
        
        Args:
            original_content: Original content to rewrite
            new_tone: New tone for the content
            new_audience: New target audience
            new_length: New target word count
            
        Returns:
            str: Rewritten content
        """
        task_description = f"""
        Rewrite the following content with the specified changes:
        
        Original Content:
        {original_content}
        """
        
        if new_tone:
            task_description += f"\n- New Tone: {new_tone}"
        if new_audience:
            task_description += f"\n- New Target Audience: {new_audience}"
        if new_length:
            task_description += f"\n- New Target Length: {new_length} words"
        
        task_description += """
        
        Please ensure the rewritten content:
        1. Maintains the core message and key points
        2. Adapts to the new specifications
        3. Flows naturally and reads well
        4. Is engaging and informative
        """
        
        result = self.execute_task(task_description)
        return self.postprocess_output(result)
    
    def validate_input(self, input_data: Any) -> bool:
        """
        Validate input for writer agent
        
        Args:
            input_data: Data to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if isinstance(input_data, str):
            return len(input_data.strip()) > 0
        return False 